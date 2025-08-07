import hashlib
import boto3
from difflib import SequenceMatcher
from botocore.exceptions import ClientError

def generate_hash(entry: str) -> str:
    return hashlib.sha256(entry.encode()).hexdigest()

def is_duplicate(entry: str, table) -> bool:
    entry_hash = generate_hash(entry)
    try:
        response = table.get_item(Key={'entry_hash': entry_hash})
        return 'Item' in response
    except ClientError as e:
        print(f"Error checking DynamoDB: {e.response['Error']['Message']}")
        return False

def is_false_positive(entry: str, table) -> bool:
    try:
        scan_response = table.scan(
            ProjectionExpression='#d',
            ExpressionAttributeNames={'#d': 'data'}
        )
        for item in scan_response.get('Items', []):
            existing = item.get('data', '')
            similarity = SequenceMatcher(None, entry, existing).ratio()
            if 0.85 < similarity < 1.0:
                return True
    except ClientError as e:
        print(f"Error scanning DynamoDB: {e.response['Error']['Message']}")
    return False

def validate_and_add(entry: str, table=None) -> str:
    if not table:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('UniqueDataTable')

    entry_hash = generate_hash(entry)

    if is_duplicate(entry, table):
        return "❌ Redundant entry detected."

    if is_false_positive(entry, table):
        return "⚠️ Warning: Possible false positive (similar to an existing entry)."

    try:
        table.put_item(Item={'entry_hash': entry_hash, 'data': entry})
        return "✅ Unique entry added successfully."
    except ClientError as e:
        return f"Error inserting into DynamoDB: {e.response['Error']['Message']}"
