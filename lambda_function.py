import json
import logging
import base64
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Authentication')

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    headers = request['headers']
    response = {
        "status": "401",
        "statusDescription": "Unauthorized",
        "body": "body",
        "headers": {
            "www-authenticate": [{
            "key": "WWW-Authenticate",
            "value": "Basic"
            }]
            },
        }
    if headers.get('authorization', 'None') != 'None':
        base64_message = headers['authorization'][0]['value'].split()[1]
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        cf_credentials = message.split(':')
        cf_password_en = cf_credentials[1].encode('ascii')
        cf_password_en_byte = base64.b64encode(cf_password_en)
        cf_password_encoded = cf_password_en_byte.decode('ascii')
        item = table.get_item(Key={"username": cf_credentials[0]})
        if item.get('Item') is not None:
            ddb_password = item.get('Item').get('password')
            if ddb_password is not None:
                ddb_password_encode = ddb_password.encode('ascii')
                message_en_bytes = base64.b64decode(ddb_password_encode)
                ddb_password_en = message_en_bytes.decode('ascii')
                if ddb_password_en == cf_credentials[1]:
                    print("Successful Log in for the USER", cf_credentials[0])
                    return request
                else:
                    print("Incorrect password", ddb_password_en)
                    return response
            else:
                print("password is empty")
                return response
        else:
            print("User credentials are empty or not valid")
            return response
    
    if headers.get('authorization', 'None') == 'None':
        print("Credentials are not given")
        return response
  
