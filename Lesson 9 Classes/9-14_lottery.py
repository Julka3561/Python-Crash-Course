import random

lottery_symbols = [10, 62, 43, 74, 15, 34, 56, 9, 3, 88, 
                   'V', 'A', 'S', 'P', 'R']
for i in range(4):
    lottery_win = random.choice(lottery_symbols)
    print(lottery_win, end=' ')
print ('\nThis is a winning combination!!! Congratulations!')