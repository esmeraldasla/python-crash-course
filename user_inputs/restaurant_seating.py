"""Write a program that asks the user how many people are in their dinner group. If the answer is more than eight,
print a message saying they’ll have to wait for a table. """

print("Welcome to Esmeralda Restaurant")
seats = input('To provide you with the best experience, '
              'would you let me know how many of you are there?')
seats = int(seats)

if seats <=5:
    print(f"\nThank you! Table confirmed for {seats}")

else:
    print(f"\nSorry, we don't have seat for {seats} today. Our maximum number today is 5.")

