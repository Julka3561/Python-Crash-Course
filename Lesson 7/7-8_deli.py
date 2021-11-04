sandwich_orders = ['salsa', 'chili', 'pepperoni', 'turkey', 'ham', 'tuna', 
                   'chicken', 'veggie', 'egg & mayo']
finished_sandwiches = []
while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
print ("-----Finished orders-----")
for order in finished_sandwiches:
    print(f'Sandwich with {order}')
