def make_album(artist, album, number_songs=0):
    album_information = {
        'artist name': artist,
        'album name': album,
    }
    if number_songs:
        album_information['number_songs'] = number_songs
    return album_information

print("(enter 'q' at any time to quit)")

prompt_1 = "\nPlease tell me your favorite artist:"
prompt_2 = "\nWhat is your favorite album?"

while True:
    artist = input(prompt_1)
    if artist =='q':
        break

    album = input(prompt_2)
    if album == 'q':
        break

    answer = make_album(artist, album)
    print(answer)