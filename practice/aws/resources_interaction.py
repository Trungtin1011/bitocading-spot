# AWS SDK for Python (Boto3) is used to make API calls to AWS from Python applications
# Client API: Provides a one-to-one mapping with the underlying service HTTP API
# Resource API: An abstraction on top of the service HTTP API
# Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html

import botocore, boto3, os, logging

# Init logger and variables
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# List of available services that can be loaded as low-level clients via Session.client()
def fetch_available_services(profile:str):
  try:
    session = boto3.Session(profile_name=profile)
  except Exception as e:
    logger.error(e.args[0])
    return 1

  logger.info([svc for svc in session.get_available_services()])
  return 0

# List S3 bucket through VPC endpoint URL (eg. "https://bucket.vpce-xxx-yyyy.s3.ap-southeast-1.vpce.amazonaws.com")
def list_bucket_through_vpce(profile:str,region:str,endpoint:str):
  try:
    s3_client = boto3.Session(profile_name=profile).client(service_name="s3", region_name=region, endpoint_url=endpoint)
  except Exception as e:
    logger.error(e.args[0])
    return 1

  try:
    logger.info([bucket["Name"] for bucket in s3_client.list_buckets()['Buckets']])
    return 0
  except Exception as e:
    logger.error(e.args[0])
    return 1
