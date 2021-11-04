print('Please, enter your age: ')
age = int(input())
if (age < 2):
    print('You are baby.')
elif(age < 4):
    print('You are toddler.')
elif(age < 13):
    print('You are kid.')
elif(age < 20):
    print('You are teenager.')
elif(age < 65):
    print('You are adult.')
else:
    print('You are elder.')