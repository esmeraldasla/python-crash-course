import json

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(f"Your favorite number is {numbers}")