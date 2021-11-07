guests = ["Коля", "Сеня", "Оля", "Дима", "Ира", "Сережа", "Вова", "Люда", "Аня", "Слава"]

guests.insert(0, 'Маша')
guests.insert(5, 'Петя')
guests.append('Паша')
del guests[0]
del guests[0]
print(f'В итоге {len(guests)} гостей.')