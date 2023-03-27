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
    def __init__(self, first_name, last_name, age, gender, country):
        """Initialize attributes"""
        super().__init__(first_name, last_name, age, gender, country)
        self.privileges = [ 'can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """"Show privileges that Admins have"""
        print("""Those are the priveleges an Admin has:""")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_privileges = Admin('esmeralda', 'lima', '28', 'female', 'brazil')

admin_privileges.show_privileges()