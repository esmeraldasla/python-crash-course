"""
Make a dictionary containing three major rivers and the country each river runs through
 key-value pair might be 'nile': 'egypt'.

 •	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    'nile': 'egypt',
    'amazonas': 'brazil',
    'seine': 'france',
    'colorado river': 'unites states',
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

print("\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for country in rivers.values():
    print(country.title())