from django.db import models
from dynamodb_json import json_util
import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings

dynamodb = boto3.resource('dynamodb', region_name=settings.AWS_REGION)
table_name = 'Devices_test'
table = dynamodb.Table(table_name)

class Devices_test(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    deviceModel = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    note = models.TextField()
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_to_dynamodb(self):
        data = {
            'id': self.id,
            'deviceModel': self.deviceModel,
            'name': self.name,
            'note': self.note,
            'serial': self.serial,
        }
        item = json_util.dumps(data)
        try:
            table.put_item(Item=json_util.loads(item))
        except NoCredentialsError:
            print("AWS credentials not found. Make sure your credentials are correctly configured.")

    @classmethod
    def get_device_by_id(cls, id):
        response = table.get_item(Key={'id': id})
        item = response.get('Item')
        if item:
            return json_util.loads(item)
        return None

    @classmethod
    def get_all_devices(cls):
        response = table.scan()
        items = response.get('Items', [])
        return [json_util.loads(item) for item in items]
