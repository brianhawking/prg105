"""
For this program you will get a phrase from the user, split the phrase into a list,
and use the first letter of each word to create an acronym. Display the acronym using
all capital letters.
"""


# Main function. Will get user's phrase
def main():
    print("This program will take in a phrase and return an acronym.")
    phrase = input("Please enter a phrase to convert: ")
    print(convertToAcronym(phrase))


# Receives a string and returns the acronym string
def convertToAcronym(phrase):
    acronym_array = phrase.split()
    acronym_string = ""
    for word in acronym_array:
        acronym_string += word[0].upper()
    return acronym_string


# ===== START PROGRAM =======================
main()
