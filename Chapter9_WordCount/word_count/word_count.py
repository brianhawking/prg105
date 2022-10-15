"""
Create a program to read the words in the given file and add them
to a dictionary along with a count of how many times each word
appears in the file. When all words in the file have been added,
display the unique words in the dictionary (i.e. words with a count of 1).
"""


def main():
    words = {}

    try:
        file = open('tale_of_two_cities.txt', 'r')

        # Loop through file. If the word hasn't been added yet to dictionary
        # add it and set the value to 1
        # If it's been added already, increment its value by 1
        for line in file:
            word = line.rstrip('\n')
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

        file.close()

        # Print only keys whose value is 1 (i.e., unique word)
        for key, value in words.items():
            if value == 1:
                print(key)

    except Exception:
        print("There was a problem opening the file.")


# ===== START =============
main()
