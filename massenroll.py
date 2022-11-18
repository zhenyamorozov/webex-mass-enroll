"""Simple but useful script to mass enroll users in to Webex space.
Set your accessToken, roomId, and provide a list of emails to enroll.
"""

accessToken = "your access token"
roomId = "your room ID"

emails = [
"user1@example.com",
"user2@example.com",
]

import json
import requests

requests.packages.urllib3.disable_warnings()

headers = {"Authorization": "Bearer " + accessToken,
           "Content-Type": "application/json; charset=utf-8"}

i = 1

for email in emails:
    body_json = {
        "roomId" : roomId,
        "personEmail" : email,
    }

    resp = requests.post("https://api.ciscospark.com/v1/memberships",
                    json.dumps(body_json), headers=headers, verify=False)

    status = resp.status_code
    #print(resp.json())
    if "message" in resp.json():
        message = resp.json()["message"]
    else:
        message = ""
    print(str(i)+" Email: "+email+" Status: "+str(status)+" "+message+"\n")
    i+=1

