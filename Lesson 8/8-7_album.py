def make_album(name, title, number_of_songs=None):
    album = {
        'Artist name' : name,
        'Album title' : title,
        'Number of songs' : number_of_songs,
    }
    return album


print(make_album('Elton John', 'Lion King'))
print(make_album('Sting', 'Desert Rose', '12'))