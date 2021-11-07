def describe_city(city, country='Russia'):
    """Prints city name and country"""
    print(f"{city.title()} is in {country.title()}")

describe_city('Samara')
describe_city(city= 'Moscow')
describe_city('London', 'Great Britain')
describe_city(city='Coln', country='Germany')