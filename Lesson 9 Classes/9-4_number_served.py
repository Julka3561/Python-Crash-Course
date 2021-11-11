class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name.title()} is serving "
              f"{self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, inc_num):
        self.number_served += inc_num
        
        
some_restaurant = Restaurant('claude monet', 'french')
print(some_restaurant.number_served)
some_restaurant.number_served = 10
print(some_restaurant.number_served)
some_restaurant.set_number_served(23)
print(some_restaurant.number_served)
some_restaurant.increment_number_served(7)
print(some_restaurant.number_served)
