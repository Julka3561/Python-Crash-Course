cities = {
    'saint-petersburg' : {
        'country' : 'russia',
        'population' : '5 384 342', 
        'fact' : 'is situated on the Neva River'
    },
    'london' : {
        'country' : 'england',
        'population' : '8 961 989', 
        'fact' : 'is situated on the River Thames'
    },
     'new york' : {
        'country' : 'united states',
        'population' : '8 804 190', 
        'fact' : 'is situated on the Hudson River'
    },
}
for city, inform in cities.items():
    print (f"\nCity name: {city.title()}")
    for name, value in inform.items():
        print(f"\t {name}: {value.title()}") 