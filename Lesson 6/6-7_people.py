person1 ={
    'first_name' : 'julia',
    'last_name' : 'vasileva',
    'age' : 38,
    'city' : 'Uspenskoe'
    }
person2 ={
    'first_name' : 'dmitry',
    'last_name' : 'klimkin',
    'age' : 45,
    'city' : 'Leningrad'
    }
person3 ={
    'first_name' : 'nikolay',
    'last_name' : 'vasilev',
    'age' : 10,
    'city' : 'Saint-Petersburg'
    }
people =[person1, person2, person3]
for person in people:
    print(f"\n{person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity of birth: {person['city']}")