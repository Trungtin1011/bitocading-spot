import boto3
import json

boto3.setup_default_session(profile_name='default')
ec2 = boto3.client('ec2')
instances = ec2.describe_instances(MaxResults=20)

#print(instances['Reservations'][0])
for instance in instances['Reservations']:
    for i in instance['Instances']:
        tagging = []
        if 'Tags' not in i:
            tagging.append("no-tags")
        else:
            for tags in i['Tags']:
                tagging.append(tags['Key'] + ": " + tags['Value'])

        print('[id:', i['InstanceId'], ', type:', i['InstanceType'], \
              ', zone:', i['Placement']['AvailabilityZone'], \
              ', status:', i['State']['Name'], ']')
        print(tagging)
        print("")
