import requests
import base64
import json


with open(".client_id") as f:
    client_id = f.read()
with open(".client_secret") as f:
    client_secret = f.read()
with open(".refresh_token") as f:
    refresh_token = f.read()

token = base64.urlsafe_b64encode((client_id + ":" + client_secret).encode()).decode()

headers = {"Authorization": "Basic " + token}
data = {
    "refresh_token": refresh_token,
    "grant_type": "refresh_token",
}

response = requests.post(
    "https://accounts.spotify.com/api/token", data=data, headers=headers
).json()

access_token = response['access_token']

with open(".OAuth_token", mode="w") as f:
    f.write(access_token)

if 'refresh_token' in response:
    with open(".refresh_token", mode="w") as f:
        f.write(response['refresh_token'])