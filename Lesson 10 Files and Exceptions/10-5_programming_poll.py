filename = 'poll.txt'

while True:
    name = input('Please, write why do you love programming for exit enter '
                 '"quit": ')
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')
