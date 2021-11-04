def make_tshirt(size, text):
    """Prints message about T-shirt of users size and text on it"""
    print(f"Your T-shirt is {size} size. A text on it is: {text}")
user_size = int(input("What size do you have? "))
user_text = input("What text do you wish to see on your T-shirt? ")
make_tshirt(user_size, user_text)