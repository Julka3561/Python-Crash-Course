def make_sandwiches(*toppings):
    print(f"\nYou order sandwich with:")
    for topping in toppings:
        print(f'\t- {topping}')


make_sandwiches('onions', 'ham', 'pickles', 'mayo', 'mustard')

make_sandwiches('salmon', 'tartar sause', 'dill', 'avocado')

make_sandwiches('grilled chicken breast', 'honey sause', 'apple')