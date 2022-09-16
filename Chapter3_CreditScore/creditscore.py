"""
Ask your user for their credit score. Tell them if they have Bad,
Fair, Good, or Excellent credit.
Excellent = 720 - 850
Good = 690 - 719
Fair = 630 - 689
Bad = 300 - 629
"""

# Get user input
credit_score = int(input("What is your credit score? "))

# Set credit_description
credit_description = ""

# Determine the type of credit based on above directions
if credit_score >= 720:
    credit_description = "Excellent"
elif credit_score >= 690:
    credit_description = "Good"
elif credit_score >= 630:
    credit_description = "Fair"
else:
    credit_description = "Bad"

# Output to user
print(f"With a credit score of {credit_score}, you have {credit_description} credit.769")
