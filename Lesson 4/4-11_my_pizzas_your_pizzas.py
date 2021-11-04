pizzas = ['Маргарита', "Четыре сыра", "Пепперони"]
for pizza in pizzas:
    print(f'Я люблю {pizza}!')
print(f'\nЯ очень люблю пиццу!!!')
friend_pizzas = pizzas[:]
friend_pizzas.append('С креветками')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print('\nMy friend favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)