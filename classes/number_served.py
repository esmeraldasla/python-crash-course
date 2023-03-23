class Restaurant:
    """An attempt to describe a restaurant"""
    def __init__(self, name, cuisine_type):
       """Initialize name and cuisine type attributes"""
       self.name = name.title()
       self.cuisine_type = cuisine_type
       self.number_served = 0


    def describe_restaurant(self):
        """Description of restaurant"""
        print(f"The {self.name} is a restaurant of {self.cuisine_type} cuisine")
        print(f"We have served {self.number_served} people.")

    def open_restaurant(self):
        """Information the restaurant is open."""
        print(f"{self.name} is already open. Would you like to book a table?")

    def set_number_served(self, number):
        """Changing the number of people served"""
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('temax', 'mexican')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 23
print(f"\nNumber served: {restaurant.number_served}")

restaurant.set_number_served(40)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increment_number_served(40)
print(f"\nNumber served: {restaurant.number_served}")



