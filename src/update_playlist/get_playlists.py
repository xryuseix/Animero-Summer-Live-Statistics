import requests, json

def get(playlist_name):
    with open(".OAuth_token") as f:
        token = f.read()
    with open(".playlist_id") as f:
        playlist_id = f.read()

    end_point = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?market=JP"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    playlist = requests.get(end_point, headers=headers).json()
    while playlist["next"] != None:
        end_point = playlist["next"]
        playlist_t = requests.get(end_point, headers=headers).json()
        playlist["items"].extend(playlist_t["items"])
        playlist["next"] = playlist_t["next"]

    with open("playlist.json", mode="w") as f:
        f.write(json.dumps(playlist, ensure_ascii=False))
    return playlist

if __name__ == "__main__":
    playlist_name = "Animero Summer Live 2021 セットリスト予習"
    print(get(playlist_name))
