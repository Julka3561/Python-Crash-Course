users = []
if users:   
    for user in users:    
        if(user.lower() == 'admin'):
            print(f'Hello, {user}! Would you like to see a status report?')
        else:
            print(f'Hello, {user}! Thank you for logging in again.')
else:
    print('We need to find some users!')