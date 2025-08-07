import unittest
from app import main
from moto import mock_aws
import boto3

@mock_aws
class TestDeduplicationLogic(unittest.TestCase):

    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = self.dynamodb.create_table(
            TableName='UniqueDataTable',
            KeySchema=[{'AttributeName': 'entry_hash', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'entry_hash', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        self.table.wait_until_exists()

    def test_unique_entry(self):
        response = main.validate_and_add("Unique User, 100 Test Lane", table=self.table)
        self.assertIn("✅", response)

    def test_duplicate_entry(self):
        entry = "Duplicate User, 101 Test Ave"
        main.validate_and_add(entry, table=self.table)
        response = main.validate_and_add(entry, table=self.table)
        self.assertIn("❌", response)

    def test_false_positive(self):
        main.validate_and_add("John Doe, 123 Main Street", table=self.table)
        response = main.validate_and_add("Jon Doe, 123 Main St.", table=self.table)
        self.assertIn("⚠️", response)

if __name__ == '__main__':
    unittest.main()
