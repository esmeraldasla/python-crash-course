"""This is another program similar to admin.py but with the purpose
of doing the same task in another way."""

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

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, country, privileges):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, gender, country)

        """Initialize an empty set of privileges"""
        self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """"Show privileges that Admins have"""
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges.")



mary = Admin('mary', 'lima', '28', 'female', 'brazil', ['can add post', 'can delete post', 'can ban'])
mary.describe_user()

mary.privileges.show_privileges()

