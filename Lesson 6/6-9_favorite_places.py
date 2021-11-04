favorite_places = {
    'julia' : ['italy', 'bulgaria', 'finland'],
    'dmitry' : ['iran', 'italy'],
    'nikolay' : ['italy'],
}
for person, places in favorite_places.items():
    if (len(places) > 1):
        print(f"\n{person.title()} favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{person.title()} favorite place is {places[0].title()}.")