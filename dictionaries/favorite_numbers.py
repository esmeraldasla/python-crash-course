#This task must creat a dictionary to store people's favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number

favorite_number = {
    'Alicia': '2',
    'Michelle': '3',
    'Anna': '1',
    'Rose': '10',
    'John': '8',
}

number = favorite_number['Alicia'].title()
print(f"Alicia's favorite number is {number}.")

number = favorite_number['Michelle'].title()
print(f"\nMichelle's favorite number is {number}.")

number = favorite_number['Anna'].title()
print(f"\nAnna's favorite number is {number}.")

number = favorite_number['Rose'].title()
print(f"\nRose's favorite number is {number}.")

number = favorite_number['John'].title()
print(f"\nJohn's favorite number is {number}.")