filename = 'guestbook.txt'
name = ''
with open(filename, 'w') as file_object:
    while name != 'quit':
        name = input('Enter your name, or quit to exit: ')
        file_object.write(f'{name}\n')
