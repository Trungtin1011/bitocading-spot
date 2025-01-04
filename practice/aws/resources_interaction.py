# AWS SDK for Python (Boto3) is used to make API calls to AWS from Python applications
# Client API: Provides a one-to-one mapping with the underlying service HTTP API
# Resource API: An abstraction on top of the service HTTP API
# Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html

import botocore, boto3, os, logging, json
import re, ipaddress

# Init logger
logging.basicConfig(format="[%(levelname)s]\t%(message)s", level=logging.INFO)
logger = logging.getLogger()


# List all available services that can be loaded with a profile
def list_available_services(profile: str):
    try:
        return [
            svc for svc in boto3.Session(profile_name=profile).get_available_services()
        ]
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# Check if provided IP is a valid private IP
def is_valid_private_ip(ip: str):
    try:
        return ipaddress.ip_address(ip).is_private
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# Check if provided AWS VPC ID is in valid format
def is_valid_vpc_id(vpc: str):
    valid_pattern = re.compile(r"vpc-\w{17}$")
    try:
        return True if valid_pattern.match(vpc) is not None else False
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# Get Subnet and VPC ID from provided IP address
def detect_vpc_from_ip(ip: str):
    try:
        if is_valid_private_ip(ip):
            valid_ip = ipaddress.ip_address(ip)
            subnets_list: list = boto3.client("ec2").describe_subnets()["Subnets"]

            for subnet in subnets_list:
                if valid_ip in ipaddress.ip_network(f"{subnet['CidrBlock']}"):
                    return f"Provided IP address belongs to subnet {subnet['SubnetId']}, VPC {subnet['VpcId']}"
                    break
                else:
                    return "Provided IP address not belongs to any subnets"

        else:
            logger.error(f"Invalid IP address {ip}")
            return f"Invalid IP address {ip}"

    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# List all S3 buckets in form of ['bucket']
def list_buckets():
    try:
        buckets: list = boto3.client("s3").list_buckets()["Buckets"]
        # logger.info([bucket["Name"] for bucket in buckets])
        return [bucket["Name"] for bucket in buckets]
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# List all objects from a bucket in form of ['object']
def list_bucket_objects(bucket: str):
    try:
        return [
            object["Key"]
            for object in boto3.client("s3").list_objects(Bucket=bucket)["Contents"]
        ]
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# List all tags from a bucket in form of ['key: value']
def list_bucket_tags(bucket: str):
    try:
        return [
            tags["Key"] + ": " + tags["Value"]
            for tags in boto3.client("s3").get_bucket_tagging(Bucket=bucket)["TagSet"]
        ]
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# List S3 bucket through VPC endpoint URL (eg. "https://bucket.vpce-xxx-yyyy.s3.ap-southeast-1.vpce.amazonaws.com")
def list_bucket_through_vpce(region: str, endpoint: str):
    try:
        s3_client = boto3.client(
            service_name="s3", region_name=region, endpoint_url=endpoint
        )
        return [bucket["Name"] for bucket in s3_client.list_buckets()["Buckets"]]
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# Return a dict in format {"instance-id": {Tags} }
def get_ec2_instance_tags():
    instance_tags: dict = {}
    try:
        instances: list = []
        ec2_instances = boto3.client("ec2").describe_instances()
        [instances.append(ec2["Instances"]) for ec2 in ec2_instances["Reservations"]]

        for instance in instances:
            if "Tags" not in instance[0]:
                # logger.info(f"Instance {instance[0]['InstanceId']} does not contains tags")
                instance_tags[f"{instance[0]['InstanceId']}"] = "No tags"
            else:
                tagsset: dict = {}
                for tag in instance[0]["Tags"]:
                    tagsset[f"{tag['Key']}"] = f"{tag['Value']}"
                # logger.info(f"Instance {instance[0]['InstanceId']} tags-> {tagsset}")
                instance_tags[f"{instance[0]['InstanceId']}"] = f"{tagsset}"

        return instance_tags
    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# Check if each EC2 instance contains a specific tag, return list of result
def check_ec2_tag_comply(tag: str):
    try:
        report: list = []
        instance_tags = get_ec2_instance_tags()

        for instance in instance_tags:
            if tag not in instance_tags[f"{instance}"]:
                # logger.info(f"Instance {instance} does not contain tag {tag}")
                report.append(f"Instance {instance} does not contain tag {tag}")
            else:
                # logger.info(f"Instance {instance} contains tag {tag}")
                report.append(f"Instance {instance} contains tag {tag}")

        return report

    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]


# Check if an EC2 instance contains a specific tag, return 1 or 0
def check_ec2_tag_exist(instance_id: str, tag: str):
    try:
        ec2_instance = boto3.client("ec2").describe_instances(
            InstanceIds=[instance_id]
        )["Reservations"]
        instance_tags = ec2_instance[0]["Instances"][0]["Tags"]

        tagsset: dict = {}
        [tagsset.update({f"{tag['Key']}": f"{tag['Value']}"}) for tag in instance_tags]

        if tag in tagsset:
            # logger.info(f"Tag {tag} exist in instance {instance_id}")
            return 0
        else:
            # logger.info(f"Tag {tag} does not exist in instance {instance_id}")
            return 1

    except Exception as e:
        logger.error(e.args[0])
        return e.args[0]
