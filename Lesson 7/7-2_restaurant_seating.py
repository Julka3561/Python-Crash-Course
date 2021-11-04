number_of_guests = input("Hello! How many people are in your dinner group? ")
number_of_guests = int(number_of_guests)
if (number_of_guests < 8) :
    print(f"Ok, your table is ready. Welcome!")
else:
    print(f"Please wait a moment... Looking for free table for you.")