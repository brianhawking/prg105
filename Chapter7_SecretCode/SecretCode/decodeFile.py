"""
For this assignment, you will be providing the logic (plan) for the following program:

For this assignment, you will decode the coded message file you created in the Parallel Arrays program:

Create your new program in the same folder used for the Parallel Arrays program.
This will give you access to the file you created in your Parallel Arrays program.
Copy the parallel arrays you used in the original program into your new program --
you will need to use the same parallel arrays in order to decode the message.
Ask the user for the name of the file to import (the file you created in your previous
assignment)
Use try and except statements to ensure the file is there (Use a variable to store the
file name, don't hard code it.)
Use readlines to read the file into a list
Step through the list (strip the \n!)
Convert the coded message back into English and display the message on the screen (This
can be concatenated to a string as you decode)
"""

# Global Constants
alpha = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I",
         "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R",
         "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", " ", ".",
         ",", "!"]

code = ["F", "W", "a", "b", "q", "Q", "C", "w", "D", "e", "R", "f", "S", "", "G", "h", "g", "i",
        "J", "X", "E", "k", "K", "l", "L", "B", "u", "n", "j", "o", "O", "p", "c", "M", "d", "r",
        "I", "s", "H", "t", "T", "P", "U", "v", "V", "m", "A", "x", "N", "y", "Y", "z", "Z", " ",
        ".", ","]

# Receive file name from user, read lines in from file, convert them from a coded character to
# to an alpha (decoded) character
def main():
    print("This program will decode a coded text file.")
    file_name = input("What is the name of the file to decode? ")
    decoded_message = ""
    try:
        file = open(file_name, 'r')
        for line in file:
            index = code.index(line.rstrip('\n'))
            decoded_message += alpha[index]
        file.close()
        print(decoded_message)

    # File either didn't exist or failed to open
    except Exception:
        print(f"There was a problem with {file_name}. Try again.\n")
        main()

# ======== START PROGRAM ===================
main()
