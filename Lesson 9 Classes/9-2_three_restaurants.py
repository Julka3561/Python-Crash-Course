class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"\nRestaurant {self.restaurant_name.title()} is serving "
              f"{self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")
        
restaurant1 = Restaurant('arcobaleno', 'italian')
#print(restaurant1.restaurant_name)
#print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('cloude monet', 'french')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('gre4ka', 'russian')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()