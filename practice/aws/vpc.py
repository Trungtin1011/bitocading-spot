import boto3
import re
import json

session = boto3.Session(profile_name='default')

pattern = re.compile('vpc-\w{8}$')

def get_input():
    found = input("vpc id:")
    match = pattern.match(found)
    while not match:
        found = input('vpc id:')
        match = pattern.match(found)
    return found

ec2_resource = session.resource("ec2")
ec2_client = session.client("ec2")
subnet_ids = []
for vpc in ec2_resource.vpcs.all():
    # here you can choose which subnet based on the id
    if vpc.id == 'vpc-xxx':
        for subnet in vpc.subnets.all():
            subnet_ids.append(subnet.id)
# the result of this call has the data you're looking for
res_json = ec2_client.describe_subnets(SubnetIds=subnet_ids)["Subnets"]
print(json.dumps(res_json, indent=4))
