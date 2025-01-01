import boto3, json, re, ipaddress

session = boto3.Session(profile_name='default')
ec2_resource = session.resource("ec2")
ec2_client = session.client("ec2")

def is_valid_ip(ip: str):
    try:
        ipaddress.ip_address(ip).is_private
        return True
    except ValueError:
        return False

def get_vpc_from_ip():
    ip = input("Enter IPv4 address: ")
    if is_valid_ip(ip):
        valid_ip = ipaddress.ip_address(ip)
        found: int = 0
        for vpc in ec2_resource.vpcs.all():
            cidr = ipaddress.ip_network(vpc.cidr_block)
            if valid_ip in cidr:
                found = 1
                [print(f"VPC Name: {tag['Value']}") for tag in vpc.tags if tag['Key'] == "Name"]
                print(f"VPC ID: {vpc.id}")
                print(f"CIDR: {vpc.cidr_block}")
                print(f"Account ID: {vpc.owner_id}")
        if found == 0:
            print(f"Cannot fetch VPC from IP {valid_ip}")
    else:
        print("IP address is invalid!")
    

get_vpc_from_ip()


