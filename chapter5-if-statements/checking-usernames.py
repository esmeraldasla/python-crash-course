# Program to ensure that everyone has a unique username

current_users = ['paul', 'esmeralda', 'Alicia', 'john', 'mary']

new_users = ['Esmeralda', 'alicia', 'brian']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Invalid user name")
    else:
        print("Valid user name")