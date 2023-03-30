#This program will reead the file learning_python.py

#Reading the entire file:

with open('learning_python.txt') as file_object:
    content = file_object.read()
print(content)

#Looping over the file to read line by line:

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#Storing the lines of a file on a list

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

