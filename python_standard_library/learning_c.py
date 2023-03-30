#This program replaces the word Python for C.

filename = 'learning_python.txt'

with open(filename) as file_object:
    line = file_object.read()
    print(line.replace('Python', 'C'))