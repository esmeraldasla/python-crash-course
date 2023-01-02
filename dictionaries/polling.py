"""
Use the code in favorite_languages.py (page 97).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.

•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.

"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n")

survey_participants = ["sarah", "phill", "mary", "jenny", "karen"]

for participant in survey_participants:
    if participant in favorite_languages.keys():
        print(f"{participant.title()}, thank you for taking our survey")

    else:
        print(f"{participant.title()}, Please, take our survey")
