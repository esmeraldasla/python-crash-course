#The program must prompt the user favorite number and to store it in a file.
#And the program must return the user's favorite number
import json

numbers = input("What is your favorite number?")

filename = 'numbers.json'
with open (filename, 'w') as f:
    json.dump(numbers, f)

print(f"Your favorite number is {numbers}")