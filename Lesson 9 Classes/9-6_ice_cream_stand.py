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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = 'ice-cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = ['vanilla', 'chocolate', 'lemon', 'nuts']
    def flavors(self):
        print("Flavors of ice-cream:")
        for f in self.flavor:
            print(f"\t-{f}")

icecream = IceCreamStand('Happy Hour') 
icecream.describe_restaurant()
icecream.flavors()


    