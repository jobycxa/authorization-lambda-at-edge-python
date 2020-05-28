#!/usr/bin/python3
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.create_table(
    TableName='Authentication',
    KeySchema=[{'AttributeName': 'username', 'KeyType': 'HASH'}], 
    AttributeDefinitions=[{'AttributeName': 'username', 'AttributeType': 'S'}], 
    ProvisionedThroughput={'ReadCapacityUnits': 1,'WriteCapacityUnits': 1})
table.meta.client.get_waiter('table_exists').wait(TableName='Authentication')
print(table.item_count)