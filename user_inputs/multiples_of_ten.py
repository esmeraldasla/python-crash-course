"""Ask the user for a number, and then report whether the number is a multiple of 10 or not."""

number = input("Lets figure out if the number is a multiple of 10?")

number = int(number)

if number % 10 == 0:
    print(f"\n {number} is a multiple of 10")

else:
    print(f"\n{number} is not a multiple of 10")