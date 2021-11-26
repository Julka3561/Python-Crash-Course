import random

my_ticket = [62, 'V', 9, 34]
lottery_symbols = [10, 62, 43, 74, 15, 34, 56, 9, 3, 88, 
                   'V', 'A', 'S', 'P', 'R']
lottery_win = []
count = 0
while my_ticket != lottery_win:
    lottery_win = []
    count += 1
    for i in range(4):
        lottery_win.append(random.choice(lottery_symbols))

print (f'This is a winning combination!!! Congratulations!' 
       f'\nIt takes {count} times to win.')