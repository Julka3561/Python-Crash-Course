
number1 = input('Please, enter first number: ')
try:
    number1 = int(number1)
except ValueError:
    print(f'It is not a number')
else:
    number2 = input('Please, enter second number: ')
    try:
        number2 = int(number2)
    except ValueError:
        print(f'It is not a number')
    else:
        result = number1 + number2
        print(result)
