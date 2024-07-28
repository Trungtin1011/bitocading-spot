import boto3

sqs = boto3.client("sqs")

#####
# Challenge: complete the send_message to write a "hello world" message to the MessagesQueue
#####
response = sqs.send_message(
    QueueUrl='BackgroundCheckApp',
    MessageBody='Hello World'
)

