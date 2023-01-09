"""
A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

prompt = "\nHow old are you?"
prompt += "\nYou can enter 'quit' when you are done"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age <= 3:
        print("It's free!")

    elif age <= 12:
        print("It's 10 USD")

    else:
        print("It's 15 USD")
