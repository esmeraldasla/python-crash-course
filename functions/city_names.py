def city_country (city, country):
    return f"{city.title()}, {country.title()}"

location = city_country('brasilia', 'brazil')
print(location)

location = city_country('New york', 'The United States')
print(location)

location = city_country('dubai', 'United Arab Emirates')
print(location)