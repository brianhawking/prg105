"""
Find a simple recipe online. Display the ingredients with amounts and list the servings that will be
made with the recipe. Ask the user to enter how many servings they would like to make, and display
the required amount of ingredients they will need. Format to one decimal place.
"""

# Ingredients for Chocolate Chip Cookies

BUTTER = 1
SUGAR = 1
BROWN_SUGAR = 1
EGGS = 2
VANILLA_EXTRACT = 2
BAKING_SODA = 1
HOT_WATER = 2
SALT = 0.5
FLOUR = 3
CHOCOLATE_CHIPS = 2
CHOPPED_WALNUTS = 1

# Makes a total of
SERVINGS = 24

# Get the required servings from the user
number_of_servings = int(input("Please enter the number of servings you want of these chocolate chip cookies: "))

# Multiply ingredients by this number to adjust the ingredients
scaling_factor = number_of_servings / 24

# Output
print(f"For {number_of_servings} servings of chocolate chip cookies, you will need:")
print(f"{(BUTTER * scaling_factor):.1f} cups of butter")
print(f"{(SUGAR * scaling_factor):.1f} cups of sugar")
print(f"{(BROWN_SUGAR * scaling_factor):.1f} cups of brown sugar")
print(f"{(EGGS * scaling_factor):.1f} eggs")
print(f"{(VANILLA_EXTRACT * scaling_factor):.1f} teaspoons of vanilla extract ")
print(f"{(BAKING_SODA * scaling_factor):.1f} teaspoons of baking soda")
print(f"{(HOT_WATER * scaling_factor):.1f} teaspoons of hot water")
print(f"{(SALT * scaling_factor):.1f} teaspoons of salt")
print(f"{(FLOUR * scaling_factor):.1f} cups of flour")
print(f"{(CHOCOLATE_CHIPS * scaling_factor):.1f} cups of chocolate chips")
print(f"{(CHOPPED_WALNUTS * scaling_factor):.1f} cups of chopped walnuts")
