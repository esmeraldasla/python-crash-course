"""
Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

prompt = "\nPlease, write down the toppin you would like."
prompt += "\n(When you are done, write 'quit')"

while True:
    topping = input(prompt)

    if topping != 'quit':
        print(f"{topping.title()} was added.")

    else:
       break