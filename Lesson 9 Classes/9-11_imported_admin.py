import admin
user1 = admin.User('Nikolay', 'vasilev', 2345, 10)
user1.describe_user()
user1.greet_user()

user2 = admin.Admin('julia', 'vasileva', 1, 38)
user2.describe_user()
user2.greet_user()
user2.show_privileges()