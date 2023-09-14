import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table_name = dynamodb.Table('Devices_test')
table = dynamodb.Table(table_name)