"""Process some integers.

usage: cli.py [-h] [--pull] [--add]

options:
    -h, --help  Show this help message and exit
    -p, --pull  Get the data on Spotify and reflect it locally
    -a, --add   Add a song to the playlist
    -s, --push  Reflects the local playlist to the remote
"""

from docopt import docopt
import refresh

if __name__ == '__main__':
    args = docopt(__doc__)
    refresh.update()
    if args["--pull"] :
        import pull_playlist
        path = "../../Dataset/2021 -COLORS-/2021_expected_spotify.csv"
        pull_playlist.get(path)