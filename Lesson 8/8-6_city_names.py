def city_country(city, country):
    text = f'{city}, {country}'
    return text.title()
city = input("Enter city name: ")
country = input("Enter country name: ")
print(city_country(city, country))