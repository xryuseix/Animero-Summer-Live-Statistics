import requests, json

with open(".OAuth_token") as f:
    token = f.read()
with open(".userID") as f:
    userID = f.read()

end_point = "https://api.spotify.com/v1/users/{}/playlists".format(userID)
headers = {"Authorization": "Bearer {}".format(token)}

playlist = requests.get(end_point, headers=headers).json()

with open("playlist.json", mode="w") as f:
    f.write(json.dumps(playlist, ensure_ascii=False))

for item in playlist["items"]:
    if item["name"] == "Animero Summer Live 2021 セットリスト予習":
        with open(".playlistID", mode="w") as f:
            f.write(item["id"])
        break
