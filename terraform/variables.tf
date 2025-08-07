variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "table_name" {
  description = "Name of the DynamoDB table"
  default     = "UniqueDataTable"
}
