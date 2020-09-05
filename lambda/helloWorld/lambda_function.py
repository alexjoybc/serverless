import json
import os

def lambda_handler(event, context):
    # TODO implement
    print("Hello from Lambda!")
    
    DB_HOST = os.environ["DB_HOST"]
    DB_USER = os.environ["DB_USER"]
    DB_PASS = os.environ["DB_PASS"]
    print("Connected to %s as %s" % (DB_HOST, DB_PASS))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
