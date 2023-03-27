from random import choice

#Selecting a number or letter randomly. The winners win a prize.

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what are the winning tickets")

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"The ticket pulled was {pulled_item}")
        winning_ticket.append(pulled_item)