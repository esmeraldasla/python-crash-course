"""Combine two programs from Favorite_number and if the number is already
stored, report the favorite number to the user. If not, prompt for the user's
favorite number and store it in a file."""

import json

filename = 'numbers.json'

#Load the number if already stored
try:
    with open(filename) as f:
        numbers = json.load(f)
#if not stored, prompt for a number
except FileNotFoundError:
    numbers = input("What is your favorite number?")
    with open(filename, 'w') as f:
        json.dump(numbers, f)
        print(f"Your favorite number is {numbers}")
else:
    print(f"We already know your favorite number. It is {numbers}")