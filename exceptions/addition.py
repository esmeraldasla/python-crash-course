#This program intends to handle exceptions avoiding error messages.

print("Choose two numbers to add and see the result")
print("enter 'q' when you are done")

while True:
    number_1 = input("Choose one number:")
    if number_1 == 'q':
        break
    number_2 = input("Choose another number")
    if number_2 == 'q':
        break

    try:
        answer = int(number_1) + int(number_2)
    except ValueError:
        print("You have to enter a valid number, not written form")
    else:
        print(answer)

