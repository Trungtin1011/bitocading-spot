# export RDSs="database-1,aws-sg-poc-postgresql" 
# export EC2s="i-08426f77ec0ffc042,i-00822e3324879c535"

import boto3, os, botocore

session = boto3.Session(profile_name='poc')
rds = session.client('rds')
ec2 = session.client('ec2')

db_instances = os.environ.get('RDSs').split(",")
ec2_instances = os.environ.get('EC2s').split(",")

# print (db_instances)
# print (ec2_instances)

for db_instance in db_instances:
    print ('Stopping DB instance with identifier: %s'%db_instance)
    #rds.stop_db_instance(DBInstanceIdentifier=db_instance)

for ec2_instance in ec2_instances:
    print ('Stopping EC2 instance with identifier: %s'%ec2_instance)
    #ec2.stop_instances(InstanceIds=[ec2_instance], Force=True)