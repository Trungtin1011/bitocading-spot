import boto3
import botocore

### Print out all S3 buckets and its objects
session = boto3.Session(profile_name='default')
client = session.client("s3")
for bucket in client.list_buckets()['Buckets']:
    #print('#BUCKET_NAME: ', bucket["Name"])
    try:
        for objects in client.list_objects(Bucket=bucket["Name"])['Contents']:
            print(objects['Key'])
    except KeyError:
        print("--- Bucket is empty")

    try:
        for tags in client.get_bucket_tagging(Bucket=bucket["Name"])['TagSet']:
            print(tags['Key'] + ": " + tags['Value'])
    except botocore.exceptions.ClientError:
        print("--- No tags in Bucket")

    print("---")


