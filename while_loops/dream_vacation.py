#Write a program that polls users about their dream vacation.

poll = {}

while True:
    name = input("What's your name?")
    response = input("What is your dream vacation place?")

    #store the response:
    poll[name] = response

    another_person = input(
        "Would you like your friend to answer this question?"
    )
    if another_person != 'yes':
        break

for name, response in poll.items():
    print(f"The dream vacation place of {name} is {response}")

