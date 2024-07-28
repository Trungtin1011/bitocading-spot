import boto3, os, botocore

session = boto3.Session(profile_name='np-pva')
evb = session.client('events')    
rds = session.client('rds')

#bus = os.environ.get('eventbus')
#prefix = os.environ.get('prefix')
bus = "aws-sg-pva-nprod-eventbus-1"
prefix = "aws_sg_pva_nprod"
cluster= 'aws-sg-pva-nprod-rds-postgres-001'


rds_cluster = rds.describe_db_clusters(DBClusterIdentifier=cluster)
db_status = rds_cluster['DBClusters'][0].get('Status')
if db_status == 'available':
    print ('Stopping RDS cluster', rds_cluster['DBClusters'][0].get('DBClusterIdentifier') )
    #rds.stop_db_cluster(DBClusterIdentifier=cluster)
elif db_status == 'stopped':
    print ('Starting RDS cluster', rds_cluster['DBClusters'][0].get('DBClusterIdentifier') )
else:
    print('RDS Cluster is not in \'stopped\' or \'available\' state')  


evb_rules = evb.list_rules(NamePrefix=prefix, EventBusName=bus)['Rules']
    
for rule in evb_rules:
    if (rule['State']) == "ENABLED":
        print('Disabling rule:', rule['Name'])
        evb.disable_rule(Name=rule['Name'], EventBusName=bus)
    elif (rule['State']) == "DISABLED":
        print('Enabling rule:', rule['Name'])
        evb.enable_rule(Name=rule['Name'], EventBusName=bus)
    else:
        print('Cannot determine EventBridge rule status')




