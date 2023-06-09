"""The program will read files and print to the screen,
also it will fail silently if a file is missing"""

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            list = f.read()

    except FileNotFoundError:
        pass

    else:
        print(f"\nReading file: {filename}")
        print(list)
