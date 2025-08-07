output "dynamodb_table_name" {
  value = aws_dynamodb_table.unique_data_table.name
}
