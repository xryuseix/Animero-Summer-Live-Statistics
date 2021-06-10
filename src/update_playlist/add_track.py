# プレイリストに曲を追加する
# @param track_ids ... 曲のID一覧

import requests
import json
import re


def add(track_ids):
    with open(".client_id") as f:
        client_id = f.read()
    with open(".playlist_id") as f:
        playlist_id = f.read()
    with open(".OAuth_token") as f:
        token = f.read()

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

    response = requests.post(url, headers=headers).json()

    print(response)


# track_idの表記揺れを修正
def shaping(track_id):
    is_url = re.fullmatch(r"^https://open.spotify.com/track/\w*(\?si=\w*)?$", track_id)
    if is_url != None:
        return re.findall(
            r"^https://open.spotify.com/track/(\w*)(\?si=\w*)?$", track_id
        )[0][0]
    is_id = re.fullmatch(r"^\w*$", track_id)
    if is_id != None:
        return track_id
    else:
        return None


# 曲が存在するか確認する
def is_exist(track_id):
    with open(".OAuth_token") as f:
        token = f.read()
    end_point = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    track_info = requests.get(end_point, headers=headers).json()
    if "error" in track_info:
        return False
    else:
        return True


def test():
    track_id = "2fJxU3u51B99Z3brrsOTTa"

    assert shaping(track_id) == track_id
    assert (
        shaping(f"https://open.spotify.com/track/{track_id}?si=duhfskafdk") == track_id
    )
    assert shaping(f"https://open.spotify.com/track/{track_id}") == track_id
    assert shaping("https://") == None

    assert is_exist(track_id) == True
    assert is_exist(track_id + "skjhdfskl") == False


if __name__ == "__main__":
    track_ids = ["2fJxU3u51B99Z3brrsOTTa"]
    # add(track_ids)
    test()
