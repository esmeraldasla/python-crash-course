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