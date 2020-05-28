#!/usr/bin/python3
import boto3
import base64

username = "admin"
password = "admin"
password_en = password.encode('ascii')
password_en_byte = base64.b64encode(password_en)
password_encoded = password_en_byte.decode('ascii')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Authentication')
table.put_item(Item={'username': username,'password': password_encoded })