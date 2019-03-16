import json
import requests

# enter API link from API Gateway and username and password from Cognito. 
api = ''
event = {
    "USERNAME": "",
    "PASSWORD": ""
}

response = requests.post(api, data=json.dumps(event)).json()

if response['AuthenticationResult'] is False:
    print("Incorrect username or password.")
else:
    print(response['AuthenticationResult']['IdToken'])
