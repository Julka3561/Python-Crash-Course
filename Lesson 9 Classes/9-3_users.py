class User:
    def __init__(self, first_name, last_name, user_id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
    def describe_user(self):
        print(f'\nName: {self.first_name.title()} {self.last_name.title()}')
        print(f'User ID: {self.user_id}')
        print(f'Age: {self.age}')
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
        
user1 = User('Enrike', 'Iglesias', 45671, 45)
user1.describe_user()
user1.greet_user()

user2 = User('pol', "mac'cartney", 45672, 78)
user2.describe_user()
user2.greet_user()