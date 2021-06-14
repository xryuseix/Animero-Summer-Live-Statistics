"""Process some integers.

usage: cli.py [-h] [-p] [-a] [-d]

options:
    -h, --help    Show this help message and exit
    -p, --pull    Get the data on Spotify and reflect it locally
    -a, --add     Add a song to the playlist
    -d, --delete  Delete a song to the playlist
"""

from docopt import docopt
import re
import refresh
import pull_playlist, add_track, delete_track

path = "../../Dataset/2021 -COLORS-/2021_expected_spotify.csv"

if __name__ == "__main__":
    args = docopt(__doc__)
    refresh.update()
    if args["--pull"]:
        pull_playlist.get(path)
        print("Seccessful for pull playlist!")
    if args["--add"]:
        pull_playlist.get(path)

        print("[Add] Input track_id or Spotify URL.")
        track_ids = re.split(r"\s|(, )", input("> "))

        any_added = False
        for track_id in track_ids:
            format_track_id = add_track.shaping(track_id)
            if track_id == None:
                print(f'[ERROR] track_id "{track_id}" is invalid format.')
                continue
            track_id = format_track_id
            if not add_track.is_exist(track_id):
                print(f'[ERROR] Track "{track_id}" doesn\'t exist.')
                continue
            if add_track.add(track_id):
                any_added |= True
                print(f"Seccessful for add track! ({track_id})")
        if any_added:
            pull_playlist.get(path)
    if args["--delete"]:
        pull_playlist.get(path)

        print("[Delete] Input track_id or Spotify URL.")
        track_ids = re.split(r"\s|(, )", input("> "))
        print("[Delete] Input delete track positions.(0-indexed)")
        positions = [int(x) for x in re.split(r"\s|(, )", input("> "))]

        if len(track_ids) == len(positions):
            any_deleted = False
            for track_id, position in zip(track_ids, positions):
                format_track_id = add_track.shaping(track_id)
                if track_id == None:
                    print(f'[ERROR] track_id "{track_id}" is invalid format.')
                    continue
                track_id = format_track_id
                if not delete_track.is_exist(track_id, position, "./playlist.json"):
                    print(f'[ERROR] Track "{track_id}" doesn\'t exist.')
                    continue
                if delete_track.delete(track_id, position):
                    any_deleted |= True
                    print(f"Seccessful for delete track! ({track_id})")
            if any_deleted:
                pull_playlist.get(path)
        else:
            print(
                f"[ERROR] track_ids length({len(track_ids)}) and positions({len(positions)}) length is different."
            )
