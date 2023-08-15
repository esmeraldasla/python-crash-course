import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def check_user():
    """Check if the username is correct"""
    username = get_stored_username()
    check_username = input(f"Is your name {username}. Say Yes or No:")
    if check_username == 'Yes':
        print(f"Welcome back, {username}!")

    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


check_user()

