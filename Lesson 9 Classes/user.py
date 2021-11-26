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
