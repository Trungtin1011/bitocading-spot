import boto3
s3 = boto3.client('s3')


def lambda_handler(event, context):
    obj = s3.get_object(Bucket='sourcefiles-us-west-2-6289125524846841', Key='object1')
    contents = "These are not the contents you are looking for."

    return {"result": contents}

