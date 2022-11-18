"""Simple but useful script to mass enroll users into a Webex space.
Set your accessToken, roomId, and provide emails to enroll as a list, or as a string one email per line
"""

accessToken = "your access token"
roomId = "your room ID"

emails = [
    "user1@example.com",
    "user2@example.com",
]

emails = """
user1@example.com

user2@example.com
"""


if type(emails) == str:
    emails = list(filter(lambda s: s, map(lambda s: s.strip(), emails.splitlines())))

import requests

headers = {
    'Authorization': "Bearer " + accessToken,
    'Content-Type': "application/json; charset=utf-8"
}

i = 0

for email in emails:
    i+=1

    body = {
        'roomId' : roomId,
        'personEmail' : email,
    }

    resp = requests.post(
        "https://webexapis.com/v1/memberships", 
        json = body, 
        headers = headers
    )

    print("{} Email: {} Status: {} {}".format(i, email, resp.status_code, resp.json()["message"] if "message" in resp.json() else ""))
