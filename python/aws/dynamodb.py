import boto3

client = boto3.client("secretsmanager", region_name=REGION_NAME)
response = client.get_secret_value(SecretId=SECRET_NAME)
secret_data = json.loads(response["SecretString"])

dynamodb = boto3.client("dynamodb")
put_response = dynamodb.put_item(
        TableName="ZipcodeWeather",
        Item={
            "Zipcode": {"S": "90210"},
            'TempF' : {'N': '62'}
        })

scan_response = dynamodb.scan(TableName="ZipcodeWeather")
print(scan_response)

query_response = dynamodb.query(
    TableName="ZipcodeWeather",
    KeyConditionExpression="Zipcode = :zipcode",
    ExpressionAttributeValues={
        ":zipcode": {"S": "90210"}
    })
