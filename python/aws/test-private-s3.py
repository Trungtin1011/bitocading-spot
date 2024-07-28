import boto3
import botocore

### Print out all S3 buckets and its objects
session = boto3.Session(profile_name='np-pva')
client = session.client(service_name="s3", region_name="ap-southeast-1", endpoint_url="https://bucket.vpce-0be592faecedbce61-u24864de.s3.ap-southeast-1.vpce.amazonaws.com")
for bucket in client.list_buckets()['Buckets']:
    print('---BUCKET_NAME: ', bucket["Name"])
    print("---")
