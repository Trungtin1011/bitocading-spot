import boto3
import botocore
import json

ecs = boto3.client("ecs", region_name="ap-southeast-1")

cluster = "aws-sg-trungtin-rnd-ecs-001"

service_list = ecs.list_services(cluster=cluster)['serviceArns']

#print(json.dumps(service_list))


for service in service_list:
    service_details = ecs.describe_services(cluster=cluster, services=[service])['services'][0]

    status = service_details['status']
    desired = service_details['desiredCount']
    running = service_details['runningCount']
    pending = service_details['pendingCount']


