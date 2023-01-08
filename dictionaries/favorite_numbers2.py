"""
Modify your program favorite_numbers so each person can have more than one favorite number.
Then print each person’s name along with their favorite numbers
"""

favorite_number_2 = {
    'Alicia': ['2', '9', '5'],
    'Michelle': ['3', '7', '12'],
    'Anna': ['1', '55', '23'],
    'Rose': ['10', '98', '100'],
    'John': ['8', '22', '45'],
}

for name, numbers in favorite_number_2.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(number)