import json
import requests

# fill in the api of the helloworld Lambda function
# fill in the JWT from step 1 in the authorization dictionary.
api = ''
event = {
    "AUTHORIZATION": ""
}

response = requests.get(api, headers=event).json()

print(response)