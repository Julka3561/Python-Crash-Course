from user import User

class Admin(User):
    def __init__(self, first_name, last_name, user_id, age):
        super().__init__(first_name, last_name, user_id, age)
        self.privileges = ['can add posts', 'can delete post', 'can ban user']
    def show_privileges(self):
        print('Admin have this privileges:')
        for priv in self.privileges:
            print(f"\t-{priv}")