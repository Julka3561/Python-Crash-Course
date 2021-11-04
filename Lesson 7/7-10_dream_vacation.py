#print(f'Please enter your name')
vacations = {}

while (True):
    name = input ('\nPlease enter your name: ')
    country = input (f'{name.title()}, what country would you like to visit? ')
    vacations[name] = country
    repeat = input ('Would you like to let another person respond? (yes/no): ')
    if (repeat == 'no'):
        break
    

print ("\n----- Dream Vacations -----")
for name, country in vacations.items():
    print (f"{name.title()} wishes to visit {country.title()}")
