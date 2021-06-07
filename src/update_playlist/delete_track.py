import requests, json

with open(".client_id") as f:
    client_id = f.read()
with open(".playlist_id") as f:
    playlist_id = f.read()
with open(".OAuth_token") as f:
    token = f.read()

tracks = [{"id": "2fJxU3u51B99Z3brrsOTTa", "positions": 25}]

headers = {
    "Authorization": "Bearer {}".format(token),
    "Content-Type": "application/json",
    "Accept": "application/json",
}

data = {"tracks": []}

for track in tracks:
    data["tracks"].append(
        {"uri": "spotify:track:" + track["id"], "positions": [track["positions"]]}
    )

url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

response = requests.delete(url, data=json.dumps(data), headers=headers).json()

print(response)