"""This is a program to describe a restaurant"""

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