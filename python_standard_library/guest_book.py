"""Prompt: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file."""

file = 'guest_book.txt'

print("Enter 'quit' when you are finished")

while True:
    name = input('\nWhat is your name?')
    if name == 'quit':
        break
    else:
        with open(file, 'a') as f:
          f.write(f"{name}\n")
        print(f"Hello {name}, you are now part of our guest book")
