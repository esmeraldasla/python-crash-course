"""
Make several dictionaries, where each dictionary represents a different pet. In each dictionary,
include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet
"""

pets = []

pet = {
    'name': 'gaza',
    'Type': 'bird',
    'Owner': 'Mary',
    'age': '4',
    'vaccinated': 'no',
}
pets.append(pet)

pet = {
    'name': 'moon',
    'Type': 'cat',
    'Owner': 'Joseph',
    'age': '5',
    'vaccinated': 'yes',
}
pets.append(pet)

pet = {
    'name': 'rex',
    'Type': 'dog',
    'Owner': 'Jose',
    'age': '10',
    'vaccinated': 'yes',
}
pets.append(pet)

for pet in pets:
    print(f"\nPlease, find information of {pet['name'].title()}: ")
    for key, value in pet.items():
        print(f"{key}: {value}")
