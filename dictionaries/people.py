
people = []

person = {
    'first_name': 'esmeralda',
    'last_name': 'lima',
    'age': '27',
    'city': 'salvador',}

people.append(person)

person = {
    'first_name': 'maria',
    'last_name': 'lima',
    'age': '28',
    'city': 'são paulo',}
people.append(person)

person = {
    'first_name': 'josé',
    'last_name': 'silva',
    'age': '30',
    'city': 'porto alegre',}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city= person['city'].title()

    print(f"{name}, of {city}, is {age} years old")