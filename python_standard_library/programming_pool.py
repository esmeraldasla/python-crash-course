"""Prompt: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

file = 'responses.txt'

responses = []

while True:
    answer = input('\nWhy do you like programming?')
    responses.append(answer)

    continue_pool = input("Would you like to let someone else respond? (y/n)")
    if continue_pool != 'y':
        break


with open(file, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")

