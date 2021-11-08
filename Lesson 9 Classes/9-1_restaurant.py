class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name.title()} is serving "
              f"{self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
        
some_restaurant = Restaurant('arcobaleno', 'italian')
print(some_restaurant.restaurant_name)
print(some_restaurant.cuisine_type)
some_restaurant.describe_restaurant()
some_restaurant.open_restaurant()