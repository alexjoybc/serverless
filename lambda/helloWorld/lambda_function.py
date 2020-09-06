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
    
    requestBody = json.loads(event['body'])['pull_request']

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

    pullRequestTemplate = "{}\n Pull Request #{} is {} on [{} {}] branch by {}: \n{}"
    
    pullRequestBody = pullRequestTemplate.format(\
        requestBody['title'],\
        requestBody['number'],\
        requestBody['state'],\
        requestBody['base']['repo']['name'],\
        requestBody['base']['ref'],\
        requestBody['user']['login'],\
        requestBody['html_url'])

    print(requestBody)

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": TWILIO_DEST_NUMBER, "From": TWILIO_FROM_NUMBER, "Body": pullRequestBody}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }  

    return {
        'statusCode': 200,
        'body': json.dumps("SMS sent successfully!")
    }
