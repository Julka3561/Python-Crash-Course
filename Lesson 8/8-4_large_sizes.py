def make_tshirt(size = "XXXL", text = 'I love Python!'):
    """Prints message about T-shirt of users size and text on it"""
    print(f"Your T-shirt is {size} size. A text on it is: {text}")
    
make_tshirt()
make_tshirt(size='M')
make_tshirt(size='S', text='I love C++')
