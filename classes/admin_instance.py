"""This program is to import the program module_user_privileges_admin to see if it is working properly"""

import module_user_privileges_admin

mary = module_user_privileges_admin.Admin('mary', 'lima', '28', 'female', 'brazil', ['can add post', 'can delete post', 'can ban'])
mary.describe_user()

mary.privileges.show_privileges()