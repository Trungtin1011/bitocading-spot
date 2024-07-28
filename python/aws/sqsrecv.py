import boto3

sqs = boto3.client("sqs")   # Establishes a connection to Amazon SQS by using the boto3.client() function
queue_url = 'BackgroundCheckApp'    # sets the URL of the queue to be BackgroundCheckApp.

while True:
    print("Retrieving messages")
    # receive up to two messages at a time from the queue, and it waits up to 7 seconds for a message to become available.
    response = sqs.receive_message( 
        QueueUrl=queue_url,
        MaxNumberOfMessages=2,
        WaitTimeSeconds=7,
    )

    if "Messages" in response:
        for message in response["Messages"]:
            # do your processing
            print(f"Message body: {message['Body']}")
            print(f"Removing message: {message['MessageId']}")
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

