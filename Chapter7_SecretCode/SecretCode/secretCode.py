"""
For this program, you will use parallel arrays to make a secret code creator.
The first array (alpha array) will hold all upper and lower case letters, space,
period, comma, and exclamation point. You will create a second array of the same
size (code array) to hold your secret code characters. Make sure you do not duplicate
any characters. In other words, the letter 'm' might appear in both arrays, but no more
than once in each array.

Example:

alpha = ['a', 'A', 'b', 'B' . . . ]   # partial array for the first array

code = ['%', 'm', '#', '='  . . .]   # partial array for corresponding coded characters

With this example, lower-case 'a' would be encoded as '%' since both are found at subscript
position zero.

You will ask the user for a secret phrase and encode each character by finding it in the
alpha array and displaying the corresponding character from the code array. You will display
the encoded message on-screen as a list and also write it to a file, one character per line.
"""

# Global
alpha = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I",
         "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R",
         "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", " ", ".",
         ",", "!"]

code = ["F", "W", "a", "b", "q", "Q", "C", "w", "D", "e", "R", "f", "S", "", "G", "h", "g", "i",
        "J", "X", "E", "k", "K", "l", "L", "B", "u", "n", "j", "o", "O", "p", "c", "M", "d", "r",
        "I", "s", "H", "t", "T", "P", "U", "v", "V", "m", "A", "x", "N", "y", "Y", "z", "Z", " ",
        ".", ","]


# Main function - get user's phrase
def main():
    message = input("Enter a phrase to encode: ")
    encoded_message = encode(message)
    print(encoded_message)
    print_to_file(encoded_message)


# Loop through message, match character in alpha array and match it to the encoded array
def encode(message):
    encoded_message = []
    for char in message:
        for i in range(0, len(alpha)):
            if char == alpha[i]:
                encoded_message.append(code[i])
    return encoded_message


# Receive encoded message, loop through array, and print to file
def print_to_file(message):
    file = open('encoded.txt', 'w')
    for char in message:
        file.write(char + '\n')
    file.close()

# ======= START PROGRAM ==================
main()
