promt = "Please, enter toppings you'd like in your pizza."
promt += "\nTo finish enter'quit'. "
topping = ''
while (topping != 'quit') :
     topping = input(promt) 
     if (topping != 'quit'):
        print(f"You've added {topping.lower()}.")