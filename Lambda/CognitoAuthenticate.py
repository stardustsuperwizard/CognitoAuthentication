import boto3
import json

# ClientId is taken from Cognito fill in the variable here.
client_id = ''

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    
    if type(event['body']) is str:
        user_creds = json.loads(event['body'])
    else:
        user_creds = event['body']
    
    try:
        response = client.initiate_auth(
            ClientId=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters=user_creds
            )
    except:
        response = { u'AuthenticationResult': False }
        
    return { 'statusCode': 200,
             'headers': {'Content-Type': 'application/json'},
             'body': json.dumps(response)
            }