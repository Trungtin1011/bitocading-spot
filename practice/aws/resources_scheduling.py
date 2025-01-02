import botocore, boto3, os, logging

# Init logger and variables
logging.basicConfig(format="[%(levelname)s]\t%(message)s",level=logging.INFO)
logger = logging.getLogger()

def eventbridge_rules_scheduler(eventbus:str,prefix:str):
    # Init EventBridge boto3 client
    try:
      #evb = boto3.Session(profile_name='').client('events')
      evb = boto3.client('events')
    except Exception as e:
      logger.error(e.args[0])
      return 1

    try:
      for rule in evb.list_rules(NamePrefix=prefix, EventBusName=eventbus)['Rules']:
          if (rule['State']) == "ENABLED":
              logger.info('Disabling rule: %s', rule['Name'])
              #evb.disable_rule(Name=rule['Name'], EventBusName=eventbus)
          elif (rule['State']) == "DISABLED":
              logger.info('Enabling rule: %s', rule['Name'])
              #evb.enable_rule(Name=rule['Name'], EventBusName=eventbus)
          else:
              logger.info('Cannot determine EventBridge rule status')
    except Exception as e:
        logger.error(e.args[0])
        return 1



def main():
  eventbus = os.environ.get('BUS_NAME')
  prefix = os.environ.get('NAME_PREFIX')

  eventbridge_rules_scheduler(f"{eventbus}",f"{prefix}")
