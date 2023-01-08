"""
Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person.
Loop through the dictionary, and print  each person’s name and their favorite places.
"""

favorite_places = {
    'jhonny': ['floripa', 'goiás', 'bahia'],
    'rose': ['rio de janeiro', 'paris', 'spain'],
    'joshua': ['new york', 'dublin', 'dubai'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")