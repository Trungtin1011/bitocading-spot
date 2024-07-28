# AWS SDK for Python (Boto3) is used to make API calls to AWS from Python applications
# Client API: Provides a one-to-one mapping with the underlying service HTTP API
# Resource API: An abstraction on top of the service HTTP API

### Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html

import boto3

### List of available services that can be loaded as low-level clients via Session.client()
session = boto3.Session(profile_name='default')
services = session.get_available_services()
for svc in services:
    print(svc)

