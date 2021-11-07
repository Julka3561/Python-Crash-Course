def make_album(name, title, number_of_songs=None):
    album = {
        'Artist name' : name,
        'Album title' : title,
        'Number of songs' : number_of_songs,
    }
    return album

while (True):
    token = input("Continue? (y/n) ")
    if( token == 'n'):
        break
    name = input('Enter artist name: ')
    title = input ('Enter album title: ')
    num_of_songs = input('Enter number of songs in album: ')
    print(make_album(name, title, num_of_songs))