fav_numbers ={
    'Коля' : [7, 5, 12],
    'Дима' : [7],
    'Юля' : [9, 23],
    'Саша' : [11],
    }
for person, numbers in fav_numbers.items():
    if (len(numbers) > 1):
        print(f"\n{person.title()} favorite numbers are:")
        for number in numbers:
            print (f'\t{number}')
    else:
        print(f"\n{person.title()} favorite number is {numbers[0]}")