def make_car(manuf, model, **car_info):
    """Make dictionary with information about car"""
    car_info['manufacturer'] = manuf
    car_info['model'] = model
    return car_info

car = make_car('skoda', 'yeti', color = 'silver', owner = 'dimkin')

for i, v in car.items():
    print(f'{i}: {v.title()}')
    