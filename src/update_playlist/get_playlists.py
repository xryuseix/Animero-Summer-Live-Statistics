import requests, json

def get(playlist_name):
    with open(".OAuth_token") as f:
        token = f.read()
    with open(".playlist_id") as f:
        playlist_id = f.read()

    end_point = "https://api.spotify.com/v1/playlists/{}".format(playlist_id)
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    playlist = requests.get(end_point, headers=headers).json()

    with open("playlist.json", mode="w") as f:
        f.write(json.dumps(playlist, ensure_ascii=False))

if __name__ == "__main__":
    playlist_name = "Animero Summer Live 2021 セットリスト予習"
    get(playlist_name)
