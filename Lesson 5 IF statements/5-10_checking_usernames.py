current_users = ['Goofy', 'natiel', 'marta', 'NooB', 'WalDeN', 'Admin']
new_users = ['betsy', 'admin', 'gOOfY', 'BOOM', 'MaryJane']
current_users_low = [user.lower() for user in current_users]
for new_user in new_users:
    if(new_user.lower() in current_users_low):
        print(f'Username {new_user} is already taken. Please choose another name.')
    else:
        print(f'Username {new_user} is free. Welcome!')