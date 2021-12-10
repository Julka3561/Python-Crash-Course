filename = 'guest.txt'
user_name = input('Please, input your name: ')

with open(filename, 'w') as file_object:
    file_object.write(user_name)
