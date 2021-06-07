import requests, json

with open(".client_id") as f:
    client_id = f.read()
with open(".playlist_id") as f:
    playlist_id = f.read()
with open(".OAuth_token") as f:
    token = f.read()

track_ids = ["2fJxU3u51B99Z3brrsOTTa"]

uris = ["spotify:track:" + track_id for track_id in track_ids]


headers = {
    "Authorization": "Bearer {}".format(token),
    "Content-Type": "application/json",
    "Accept": "application/json",
}


url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

for i, uri in enumerate(uris):
    url += "?uris=" if i == 0 else ","
    url += uri

# TODO 消す
url += "&position=25"

response = requests.post(url, headers=headers).json()

print(response)
