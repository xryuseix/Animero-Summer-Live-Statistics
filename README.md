# Animero Summer Live Statistics

This repository is **unofficial**.  
The official website is [here](https://anisama.tv/).

## [Dataset](./Dataset)

Dataset for the following years are currently available.

[2008](./Dataset/2008-Challenge-)

### Setlist Dataset (setlist\_{year}.csv)

This is the set list of the songs performed at the live.

| Column     | Type    | Content                                                                |
| ---------- | ------- | ---------------------------------------------------------------------- |
| Year       | INTEGER | Year.                                                                  |
| Day        | INTEGER | Day.                                                                   |
| Number     | INTEGER | Song number.                                                           |
| Medlay     | INTEGER | If it is a medley, the number of the song.                             |
| TrackName  | STRING  | Song titles.                                                           |
| ArtistName | STRING  | Singer Name. If there are multiple singers, they are separated by `/`. |
