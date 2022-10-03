# Tests for equality and inequality with strings

shoes = 'boots'
if shoes == 'boots':
    print("These are boots")
else:
    print("These are not boots")

if shoes == 'sandals':
    print("These are boots")
else:
    print("These are not boots")

if shoes.lower() == 'Boots':
    print("These are boots")
else:
    print("These are not boots.")

if shoes != 'sandals':
    print("Those are sandals not boots.")

# Testing numerical comparisons

age = 27
if age == 27:
    print("True")
else:
    print("False")

if age == 29:
    print("True")
else:
    print("False")

#Checking multiple conditions with "and" and "or" with mathematical comparisons.

my_age = 27
mom_age = 50

if my_age >= 27 and mom_age >= 49:
    print("True")
else:
    print("False")

if my_age <26 and mom_age <49:
    print ("True")
else:
    print("False")

if my_age > 10 or mom_age <40:
    print(True)
else:
    print("False")

#Checking whether a value is in a list

brands = ['Lenovo', 'Samsung', 'Apple']

if 'Apple' in brands:
    print("\nYes, we sell Apple products.")
else:
    print("\nNo, we don't sell Apple products.")

#Checking whether a value is not in a list
fired_employees = ['paul', 'peter', "marie"]
employee = 'rose'
employee_1 = 'paul'

if employee not in fired_employees:
    print(f"\n{employee.title()} was not fired.")

if employee_1 not in fired_employees:
    print(f"\n{employee_1.title()} was not fired")

else:
    print(f"\n{employee_1.title()} was fired")