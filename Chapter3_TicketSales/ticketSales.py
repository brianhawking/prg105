"""
Description: For this assignment, you will be providing the logic (plan) for
the following program:
You are writing a program to sell tickets to the school play. If the person
buying the tickets is a student, their price is $5.00 per ticket. If the
person buying the tickets is a veteran, their price is $7.00 per ticket.
If the person buying the ticket is a sponsor of the play, the price
is $2.00 per ticket. If the person buying the ticket is a part of the
public, the price is $10.00.
"""

# Set constants
student_price = 5.00
veteran_price = 7.00
sponsor_price = 2.00
retiree_price = 6.00
general_public_price = 10.00

# Display info to user
print("PLAY PRICES PER TICKET")
print(f"   1. Student ${student_price:.2f}")
print(f"   2. Veteran ${veteran_price:.2f}")
print(f"   3. Show Sponsor ${sponsor_price:.2f}")
print(f"   4. Retiree ${retiree_price:.2f}")
print(f"   5. General Public ${general_public_price:.2f}\n")

# Get use input
ticket_type = int(input("Please enter the number for the category you fit for purchasing tickets: "))
num_of_tickets = int(input("How many tickets would you like to buy? "))

# Set and calculate ticket price based on user input
if ticket_type == 1:
    ticket_price = student_price
elif ticket_type == 2:
    ticket_price = veteran_price
elif ticket_type == 3:
    ticket_price = sponsor_price
elif ticket_type == 4:
    ticket_price = retiree_price
elif ticket_type == 5:
    ticket_price = general_public_price
else:
    ticket_price = 0.0

# Set discount percentage based on number of tickets
if num_of_tickets > 15:
    discount = 0.20
elif num_of_tickets >= 9:
    discount = 0.15
elif num_of_tickets >= 4:
    discount = 0.10
else:
    discount = 0.00

# Calculate costs
cost_before_discount = ticket_price * num_of_tickets
cost_after_discount = cost_before_discount * (1 - discount)
price_per_ticket = cost_after_discount / num_of_tickets

print(f"\nCost before any discounts are applied: ${cost_before_discount:.2f}")
print(f"Your cost after all discounts are applied: ${cost_after_discount:.2f}")
print(f"Your price is ${price_per_ticket:.2f} per ticket.")

