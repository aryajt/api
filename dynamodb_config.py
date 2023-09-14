
APPEND_SLASH = True
AWS_ACCESS_KEY_ID = 'AKIAZ2M4P6U7TCAUFRWL'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'eu-north-1'

dynamodb_client = boto3.client(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)