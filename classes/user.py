"""Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user"""


class User:

    def __init__(self, first_name, last_name, age, gender, country):
        """Initialize attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.country = country.title()

    def describe_user(self):
        """Displaying user's information"""
        print(f"\nUsername: {self.first_name} {self.last_name}.")
        print( f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Country: {self.country}")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello {self.first_name} {self.last_name}. Welcome!")

mary = User('Mary', 'Maldonado', 22, 'female', 'mexico')
mary.describe_user()
mary.greet_user()

esmeralda = User('esmeralda', 'lima', 28, 'female', 'brazil')
esmeralda.describe_user()
esmeralda.greet_user()