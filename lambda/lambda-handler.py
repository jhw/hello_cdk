import boto3, logging, json

logger=logging.getLogger()
logger.setLevel(logging.INFO)    

logging.getLogger('botocore').setLevel(logging.WARNING)

def handler(event, context):
    logging.info(event)
    return {'statusCode': 200,
            'body': json.dumps(event)}
