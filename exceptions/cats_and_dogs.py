#The program will read files and print to the screen, also it will handle file errors.

def names (filename):
    """Write a try-except block to catch a FileNotFound error"""
    try:
        with open(filename) as f:
            list = f.read()
            print(f"{list}\n")
    except FileNotFoundError:
            print(f"Sorry, the file {filename} doesn't exist.")



filename = 'cats.txt'
names(filename)

filename = 'dogs.txt'
names(filename)


