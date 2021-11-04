users = ['Goofy', 'WalDeN', 'natiel', 'Admin']
for user in users:
    if(user.lower() == 'admin'):
        print(f'Hello, {user}! Would you like to see a status report?')
    else:
        print(f'Hello, {user}! Thank you for logging in again.')