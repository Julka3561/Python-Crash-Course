promt = "Please, enter your age."
promt += "\nTo finish enter'quit'. "
isActive = True

while (isActive):
    age = input(promt)
    if (age == 'quit'):
        isActive = False
    else:
        age = int(age)
        if (age < 3) :
            print(f"Your ticket is free!")
        elif (age < 12):
             print(f"Your ticket is $10.")
        else:
             print(f"Your ticket is $15.")