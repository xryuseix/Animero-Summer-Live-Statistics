# Spotifyのプレイリストをローカルへpullする
import get_playlists
import refresh
import csv


def get(path):
    refresh.update()
    playlist_name = "Animero Summer Live 2021 セットリスト予習"
    playlist_name_en = "Animero Summer Live 2021"
    playlist = get_playlists.get(playlist_name)
    items = playlist["tracks"]["items"]


    with open(path, "w") as f:
        writer = csv.writer(f)
        # ヘッダー
        writer.writerow(
            ["Track name", "Artist name", "Album", "Playlist name", "Type", "ISRC"]
        )
        for item in items:
            uri = item["track"]["uri"]
            track_id = item["track"]["id"]
            isrc = item["track"]["external_ids"]["isrc"]
            name = item["track"]["name"]
            artists = item["track"]["artists"][0]["name"]
            album = item["track"]["album"]["name"]

            writer.writerow(
                [name, artists, album, playlist_name_en, "Playlist track", isrc]
            )

if __name__ == "__main__":
    get("../../Dataset/2021 -COLORS-/2021_expected_spotify.csv")