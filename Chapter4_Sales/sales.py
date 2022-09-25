"""
Create a program that will have the user enter the total sales amount for the day at
a coffee shop. The program should ask the user for the total amount of sales and
include the day in the request. At the end of data entry, tell the user the total
sales for the week, and the average sales per day. You must create a list of the days
of the week for the user to step through.
"""

# Set up days of week
daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Initialize total
total = 0

# Instructions to user
print("Please enter the amount of sales for each day of the week.\n")

# Process
for day in daysOfWeek:
    sales = float(input(f"What were the sales for {day}? "))
    total += sales

# Final display to user
print(f"The total amount of sales for the week was ${total:.2f}")
print(f"The average amount of sales per day was ${(total / len(daysOfWeek)):.2f}")
