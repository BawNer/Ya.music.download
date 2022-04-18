from yandex_music import Client
import os
import json
from conf import APP_TOKEN

client = Client(APP_TOKEN).init()


def read_file():
    print('Read local db tracks...')
    if os.path.isfile('db_tracks.json'):
        with open('db_tracks.json', 'r') as db:
            return json.load(db)
    else:
        with open('db_tracks.json', 'w') as db:
            json.dump([], db)
            return []


def write_file(data):
    print('Write local db tracks...')
    with open('db_tracks.json', 'w') as db:
        json.dump(data, db)


def get_artists_info(artists):
    artists_info = []
    for artist in artists:
        artists_info.append({
            'artist_id': artist.id,
            'artist_name': artist.name
        })
    return artists_info


def get_track_info(track):
    return {
        'track_id': track.id,
        'track_name': track.title,
        'artists': get_artists_info(track.artists)
    }


def download_track(meta, track):
    if not os.path.exists('tracks'):
        os.mkdir('tracks')

    meta.download(f'tracks/{track.get("track_name")} - '
                  f'{",".join(list(map(lambda x: x.get("artist_name"), track.get("artists"))))}.mp3')
    return track


track_list_local = read_file()

for pure_track in client.users_likes_tracks():
    track_meta = pure_track.fetch_track()
    if track_meta.id not in list(map(lambda x: x.get('track_id'), track_list_local)):
        print(f'Start download track {track_meta.title}')
        new_track = download_track(track_meta, get_track_info(track_meta))
        track_list_local.append(new_track)
        write_file(track_list_local)
    else:
        print(f'Track {track_meta.title} exist')
        pass



