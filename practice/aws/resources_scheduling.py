import botocore, boto3, os, logging

# Init logger and variables
logging.basicConfig(format="[%(levelname)s]\t%(message)s", level=logging.INFO)
logger = logging.getLogger()


def eventbridge_rules_scheduler(eventbus: str, prefix: str):
    # Init EventBridge boto3 client
    try:
        # evb = boto3.Session(profile_name='').client('events')
        evb = boto3.client("events")
    except Exception as e:
        logger.error(e.args[0])
        return 1

    try:
        for rule in evb.list_rules(NamePrefix=prefix, EventBusName=eventbus)["Rules"]:
            if (rule["State"]) == "ENABLED":
                logger.info("Disabling rule: %s", rule["Name"])
                # evb.disable_rule(Name=rule['Name'], EventBusName=eventbus)
            elif (rule["State"]) == "DISABLED":
                logger.info("Enabling rule: %s", rule["Name"])
                # evb.enable_rule(Name=rule['Name'], EventBusName=eventbus)
            else:
                logger.info("Cannot determine EventBridge rule status")
    except Exception as e:
        logger.error(e.args[0])
        return 1


# Stop/Start provided EC2 instance
def ec2_instance_scheduler(id: str):
    try:
        ec2 = boto3.client("ec2")
        instance_info = ec2.describe_instances(InstanceIds=[id])["Reservations"][0]
        instance_status = instance_info["Instances"][0]["State"]["Name"]
        # logger.info(f"Instance status: {instance_status}")

        if instance_status == "running":
            logger.info(f"Instance {id} is running, shuting down...")
            ec2.stop_instances(InstanceIds=[id], Force=True)
        elif instance_status == "stopped":
            logger.info(f"Instance {id} is stopped, starting up...")
            ec2.start_instances(InstanceIds=[id])
        else:
            logger.error(f"EC2 instance {id} is not in 'stopped' or 'running' state")

    except Exception as e:
        logger.error(e.args[0])


# Stop/Start provided RDS instance
def rds_instance_scheduler(name: str):
    try:
        rds = boto3.client("rds")
        rds_instance = rds.describe_db_instances(DBInstanceIdentifier=name)
        # logger.info(rds_instance['DBInstances'][0])

        db_status = rds_instance["DBInstances"][0].get("DBInstanceStatus")
        if db_status == "available":
            logger.info(
                "Stopping RDS instance: %s",
                rds_instance["DBInstances"][0].get("DBInstanceIdentifier"),
            )
            rds.stop_db_instance(DBInstanceIdentifier=name)
        elif db_status == "stopped":
            logger.info(
                "Starting RDS instance: %s",
                rds_instance["DBInstances"][0].get("DBInstanceIdentifier"),
            )
            rds.start_db_instance(DBInstanceIdentifier=name)
        else:
            logger.error("RDS instance is not in 'stopped' or 'available' state")

    except Exception as e:
        logger.error(e.args[0])


# Stop/Start provided RDS cluster
def rds_cluster_scheduler(name: str):
    try:
        rds = boto3.client("rds")

        rds_cluster = rds.describe_db_clusters(DBClusterIdentifier=name)
        # logger.info(rds_cluster['DBClusters'][0])

        db_status = rds_cluster["DBClusters"][0].get("Status")
        if db_status == "available":
            logger.info(
                "Stopping RDS cluster: %s",
                rds_cluster["DBClusters"][0].get("DBClusterIdentifier"),
            )
            rds.stop_db_cluster(DBClusterIdentifier=name)
        elif db_status == "stopped":
            logger.info(
                "Starting RDS cluster: %s",
                rds_cluster["DBClusters"][0].get("DBClusterIdentifier"),
            )
            rds.start_db_cluster(DBClusterIdentifier=name)
        else:
            logger.error("RDS cluster is not in 'stopped' or 'available' state")

    except Exception as e:
        logger.error(e.args[0])


# Stop/Start provided ECS cluster between 0 and count
def ecs_cluster_scheduler(name: str, count: int):
    try:
        ecs = boto3.client("ecs")
        service_list = ecs.list_services(cluster=name)["serviceArns"]
        # logger.info(json.dumps(service_list))

        for service in service_list:
            service_details = ecs.describe_services(cluster=name, services=[service])[
                "services"
            ][0]

            status = service_details["status"]
            desired = service_details["desiredCount"]
            running = service_details["runningCount"]
            pending = service_details["pendingCount"]

            if status == "ACTIVE" and desired != 0:
                logger.info(f"Scaling down service {service} from {desired} to 0")
                ecs.update_service(cluster=name, service=service, desiredCount=0)

            elif status == "ACTIVE" and desired == 0:
                logger.info(f"Scaling up service {service} from 0 to {count}")
                ecs.update_service(cluster=name, service=service, desiredCount=count)

            else:
                logger.error(f"Cannot detect current state of service {name}")

    except Exception as e:
        logger.error(e.args[0])


# Change ECS service desired count
def update_ecs_services_replicas(cluster: str, service: str, replicas: int):
    try:
        ecs = boto3.client("ecs")
        service_details = ecs.describe_services(cluster=cluster, services=[service])[
            "services"
        ][0]

        status = service_details["status"]

        if status == "ACTIVE":
            logger.info(f"Updating service {service} replicas to {replicas}")
            ecs.update_service(cluster=cluster, service=service, desiredCount=replicas)

        else:
            logger.error(f"ECS service {service} is not running")

    except Exception as e:
        logger.error(e.args[0])


def main():
    eventbus = os.environ.get("BUS_NAME")
    prefix = os.environ.get("NAME_PREFIX")

    eventbridge_rules_scheduler(f"{eventbus}", f"{prefix}")
