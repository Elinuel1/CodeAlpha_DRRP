provider "aws" {
  region = var.aws_region
}

resource "aws_dynamodb_table" "unique_data_table" {
  name           = var.table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "entry_hash"

  attribute {
    name = "entry_hash"
    type = "S"
  }

  tags = {
    Name        = "DataRedundancyRemovalTable"
    Environment = "Dev"
  }
}
