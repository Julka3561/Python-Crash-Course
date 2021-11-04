rivers = {
    'amazon' : 'brazil',
    'lena' : 'russia',
    'missisipi' : 'america',
}
for river, country in rivers.items():
    print(f'River {river.title()} runs trough {country.title()}')
print ('\n')
for river in rivers:
    print(river.title())
print ('\n')
for country in rivers.values():
    print(country.title())