"""Using the same code from the program user.py, add an attribute called login_attempts to your User
class. Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""


class User:

    def __init__(self, first_name, last_name, age, gender, country):
        """Initialize attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.country = country.title()
        self.login_attempts = 0

    def describe_user(self):
        """Displaying user's information"""
        print(f"\nUsername: {self.first_name} {self.last_name}.")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Country: {self.country}")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello {self.first_name} {self.last_name}. Welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts > 3:
            print("\nYou have to reset your password")

    def reset_login_attempts(self):
        self.login_attempts = 0



mary = User('Mary', 'Maldonado', 22, 'female', 'mexico')
mary.describe_user()
mary.greet_user()

print(f"\nThe user did 4 logins attempts:")
mary.increment_login_attempts()
mary.increment_login_attempts()
mary.increment_login_attempts()
mary.increment_login_attempts()
print(f"The number of login attempts are {mary.login_attempts}")

print(f"\nLogin attempts resetted.")
mary.reset_login_attempts()
print(f"The number of login attempts are {mary.login_attempts}")


