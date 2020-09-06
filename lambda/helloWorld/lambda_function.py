import base64
import json
import os
import urllib
from urllib import request, parse

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

    TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"

    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
    TWILIO_DEST_NUMBER = os.environ.get("TWILIO_DEST_NUMBER")
    TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")

    if not TWILIO_ACCOUNT_SID:
        return {
            'statusCode': 400,
            'body': json.dumps("Unable to access Twilio Account SID.")
        }
    elif not TWILIO_AUTH_TOKEN:
        return {
            'statusCode': 400,
            'body': json.dumps("Unable to access Twilio Auth Token.")
        }
    elif not TWILIO_DEST_NUMBER:
        return {
            'statusCode': 400,
            'body': json.dumps("Unable to access destination number.")
        }
        return "The function needs a 'To' number in the format +12023351493"
    elif not TWILIO_FROM_NUMBER:
        return {
            'statusCode': 400,
            'body': json.dumps("Unable to access destination number.")
        }
    elif not requestBody:
         return {
            'statusCode': 400,
            'body': json.dumps("Invalid body.")
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(requestBody['pull_request'])
    }
