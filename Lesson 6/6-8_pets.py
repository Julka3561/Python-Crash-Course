pet1 ={
    'name' : 'pumpkin',
    'owner_name' : 'mr. Yotkins',
    'age' : 2,
    'specie' : 'hamster'
    }
pet2 ={
    'name' : 'viola',
    'owner_name' : 'mrs. Klarins',
    'age' : 10,
    'specie' : 'dog'
    }
pet3 ={
    'name' : 'smokey',
    'owner_name' : 'miss Bellview',
    'age' : 3,
    'specie' : 'cat'
    }
pet4 ={
    'name' : 'harry',
    'owner_name' : 'mr. Statem',
    'age' : 15,
    'specie' : 'dog'
    }

pets =[pet1, pet2, pet3, pet4,]

for pet in pets:
    print(f"\n{pet['name'].title()}")
    print(f"\tOwner: {pet['owner_name']}")
    print(f"\tAge: {pet['age']}")
    print(f"\tSpecie: {pet['specie']}")