"""Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of
information about each city and include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print
the name of each city and all of the information you have stored about it. """

cities = {
    'rio de janeiro': {
        'country': 'brazil',
        'population': '6.7 million',
        'fact': 'The statue of Christ the Redeemer was elected one of the world’s new seven wonders',
    },
    'new york': {
        'country': 'the united states',
        'population': '8.4 million',
        'fact': "The City's Original Name Was New Amsterdam.",
    },

    'dubai': {
        'country': 'united arab emirates',
        'population': '3.3 million',
        'fact': 'Dubai weekend is 2.5 days',
    },

}

for city, facts in cities.items():
    place = facts['country']
    population = facts['population']
    fact = facts['fact']

    print(f"{city.title()}:")
    print(f"{city.title()} is located in {place.title()}. Its population is about {population}.")
    print(f"Here is an important fact about {city.title()}: {fact}.\n")