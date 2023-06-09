"""This program will analyze how many times a word appears in a text"""

def count_words(filename):
    """This program will find how many time a word appears in a text"""
    try:
        with open(filename, encoding='utf-8') as f:
            number = f.read()
    except FileNotFoundError:
        pass
    else:
        number_words = number.lower().count('the ')
        print(f"{filename} has the words 'the' {number_words} times")

filenames = ['romeoandjuliet.txt', 'hamlet.txt']
for filename in filenames:
    count_words(filename)