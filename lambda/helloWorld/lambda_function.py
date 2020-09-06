import json
import os

def lambda_handler(event, context):
    
    if "body" not in event:
        return {
            'statusCode': 400,
            'body': json.dumps("body is required")
    }

    # TODO implement
    print("Hello from Lambda!")
    
    print(event['body'])
    
    requestBody = json.loads(event['body'])

    DB_HOST = os.environ["DB_HOST"]
    DB_USER = os.environ["DB_USER"]
    DB_PASS = os.environ["DB_PASS"]
    print("Connected to %s as %s" % (DB_HOST, DB_PASS))
    
    return {
        'statusCode': 200,
        'body': json.dumps(requestBody['pull_request'])
    }
