def make_album(artist, album, number_songs=0):
    album_information = {
        'artist name': artist,
        'album name': album,
    }
    if number_songs:
        album_information['number_songs'] = number_songs
    return album_information

music_album = make_album('David', 'bethel album')
print(music_album)

music_album = make_album('John', 'paradise album')
print(music_album)

music_album = make_album('John', 'paradise album',4)
print(music_album)