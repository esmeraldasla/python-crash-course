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


class IceCreamStand(Restaurant):
    """This represents an icecream stand"""
    def __init__(self,  name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(name, cuisine_type)
        self.icecream_flavors = ['chocolate', 'vanilla', 'oreo']

    def list_flavors(self):
        """Print a statement describing icecream flavors"""
        print(f"Icecream flavors available:\n {self.icecream_flavors}")


icecream_shop = IceCreamStand('Coco Cold', 'icecream shop')

icecream_shop.list_flavors()

