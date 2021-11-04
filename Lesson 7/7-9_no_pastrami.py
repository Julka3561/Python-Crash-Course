sandwich_orders = ['pastrami','salsa', 'chili', 'pastrami', 'pepperoni', 
                   'turkey', 'ham', 'tuna', 'chicken', 'veggie', 'pastrami',
                   'egg & mayo']
finished_sandwiches = []

print (f'Sorry we run out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:

    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
print ("-----Finished orders-----")
for order in finished_sandwiches:
    print(f'Sandwich with {order}')
