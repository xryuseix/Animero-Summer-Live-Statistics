"""Process some integers.

usage: cli.py [-h] [-p] [-a] [-s]

options:
    -h, --help  Show this help message and exit
    -p, --pull  Get the data on Spotify and reflect it locally
    -a, --add   Add a song to the playlist
    -s, --push  Reflects the local playlist to the remote
"""

from docopt import docopt
import re
import refresh

if __name__ == "__main__":
    args = docopt(__doc__)
    refresh.update()
    if args["--pull"]:
        import pull_playlist

        path = "../../Dataset/2021 -COLORS-/2021_expected_spotify.csv"
        pull_playlist.get(path)
        print("Seccessful for pull playlist!")
    if args["--add"]:
        import pull_playlist, add_track

        path = "../../Dataset/2021 -COLORS-/2021_expected_spotify.csv"
        pull_playlist.get(path)

        print("Input track_id or Spotify URL.")
        track_ids = add_track.shaping(input("> "))

        any_added = False
        for track_id in re.split("\s|(, )", track_ids):
            if track_id == None:
                print("[ERROR] track_id is invalid format.")
                exit()
            if not add_track.is_exist(track_id):
                print("[ERROR] That track doesn't exist.")
                exit()
            if add_track.add(track_id):
                any_added |= True
                print("Seccessful for add playlist!")
        if any_added:
            pull_playlist.get(path)
