import boto3, ipaddress

aws_accounts = [""] #, ""]

def role_arn_to_session(**args):
    client = boto3.client("sts")
    response = client.assume_role(**args)
    return boto3.Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
    )

def set_boto3_clients(account_id):
    return role_arn_to_session(
        RoleArn="arn:aws:iam::" + account_id + ":role/aws-sg-trungtin-readonly-role",
        RoleSessionName=f"{account_id}-crossaccount-role",
    )

def is_valid_ip(ip: str):
    try:
        ipaddress.ip_address(ip).is_private
        return True
    except ValueError:
        return False

def fetch_vpc_from_ip(ip: str):
    if is_valid_ip(ip):
        valid_ip = ipaddress.ip_address(ip)
        found: int = 0
        for account in aws_accounts:
            execution_session = set_boto3_clients(account)
            ec2_resource = execution_session.resource("ec2")
            for vpc in ec2_resource.vpcs.all():
                cidr = ipaddress.ip_network(vpc.cidr_block)
                if valid_ip in cidr:
                    found = 1
                    print(f"Found on account: {vpc.owner_id}")
                    [print(f"VPC Name: {tag['Value']} ({vpc.id})") for tag in vpc.tags if tag['Key'] == "Name"]
                    print(f"CIDR: {vpc.cidr_block}")
                    break
        if found == 0:
            print(f"Cannot fetch VPC from IP {valid_ip}")
    else:
        print("IP address is invalid!")

def main():
    ip = input("Enter IPv4 address: ")
    fetch_vpc_from_ip(ip)
main()
