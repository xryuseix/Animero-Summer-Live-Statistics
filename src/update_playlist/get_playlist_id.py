import requests, json

def get(playlist_name):
    with open(".OAuth_token") as f:
        token = f.read()
    with open(".userID") as f:
        userID = f.read()

    end_point = "https://api.spotify.com/v1/users/{}/playlists".format(userID)
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/json",
    }

    playlist = requests.get(end_point, headers=headers).json()

    with open("playlist_info.json", mode="w") as f:
        f.write(json.dumps(playlist, ensure_ascii=False))

    for item in playlist["items"]:
        if item["name"] == playlist_name:
            with open(".playlist_id", mode="w") as f:
                f.write(item["id"])
            break

if __name__ == "__main__":
    playlist_name = "Animero Summer Live 2021 セットリスト予習"
    get(playlist_name)