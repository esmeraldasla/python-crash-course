from module_user import User

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


