# プレイリストに曲を追加する
# @param tracks ... 曲のID一覧

import requests, json


def delete(track, position):
    with open(".client_id") as f:
        client_id = f.read()
    with open(".playlist_id") as f:
        playlist_id = f.read()
    with open(".OAuth_token") as f:
        token = f.read()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {"tracks": [{"uri": f"spotify:track:{track}", "positions": [position]}]}

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    response = requests.delete(url, data=json.dumps(data), headers=headers).json()
    # 0-indexと1-indexを間違えた時用
    if "error" in response:
        data["tracks"][0]["positions"][0] -= 1
        response = requests.delete(url, data=json.dumps(data), headers=headers).json()
    
    if "error" in response:
        return False
    else:
        return True


# 曲が存在するか確認する
def is_exist(track_id, position, playlist_path):
    with open(playlist_path) as f:
        playlist = json.load(f)
    items = playlist["tracks"]["items"]
    if position < len(items) and track_id == items[position]["track"]["id"]:
        return True
    else:
        return False


if __name__ == "__main__":
    delete("2fJxU3u51B99Z3brrsOTTa", 135)
