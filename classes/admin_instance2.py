from module_privileges_admin import Admin


mary = Admin('mary', 'lima', '28', 'female', 'brazil', ['can add post', 'can delete post', 'can ban'])
mary.describe_user()

mary.privileges.show_privileges()