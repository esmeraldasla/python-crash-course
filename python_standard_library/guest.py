"""Prompt: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt"""

username = input("What is your name?")
print("Username is:" + username)

filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(username)