"""This program must make a class with 2 attributes, 2 methods
and an instance. The 2 attributes must be printed individually and
both methods must be called."""

class Restaurant:
    """An attempt to describe a restaurant"""
    def __init__(self, name, cuisine_type):
       """Initialize name and cuisine type attributes"""
       self.name = name.title()
       self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Description of restaurant"""
        print(f"The {self.name} is a restaurant of {self.cuisine_type} cuisine")

    def open_restaurant(self):
        """Information the restaurant is open."""
        print(f"{self.name} is already open. Would you like to book a table?")


restaurant = Restaurant('temax', 'mexican')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")
restaurant_2 = Restaurant('japa', 'japanese')
restaurant_2.describe_restaurant()

print("\n")
restaurant_3 = Restaurant('masalama','arab')
restaurant_3.describe_restaurant()