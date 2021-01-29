# Varun Suresh
# 873569280
# This program counts the frequency of the characters that appear in the files that it is fed.

import sys

from string import ascii_lowercase

import csv

# add_frequencies is a function that adds the frequency counts of the characters to the dictionary d.
def add_frequencies(d, file, remove_case):
    initial_text = str(file.read)

# The following if-statement tests if remove_case is True or False, so that the text can either be changed or remain as is.
    if remove_case:
        working_text = initial_text.lower()
    else:
        working_text = initial_text

# The following loop checks iterates through all the characters in the text, checks that each character is contained within the alphabet, and then updates the dictionary. 
    for character in working_text:
        if((ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122)):
            if character in d:
                d[character] += 1
            else:
                d[character] = 1
        else:
            continue

def main():
# The following line creates an empty dictionary.
    d = dict()

# The following variable tells us whether the '-c' flag was entered or not. The following line initializes the variable.
    remove_case = True

# The following variable tells the program whether the '-l' was entered or not. Will be used later. The following line initializes the variable.
    l_is_true = False

# The following loop iterates through the arguments given.
    for i in range(1,len(sys.argv)):
        name = sys.argv[i]
        # print(name)
# The following if-statement tests if the '-c' flag is used and makes the corresponding adjustment.
        if name=='-c':
            remove_case = False
# The following if-statement tests if the '-l' flag is used and makes the corresponding adjustment.
        if name=='-l':
        # The following line defines the variable that tells us later whether the '-l' flag was entered or not
            l_is_true = True
            name2 = sys.argv[i+1]
            print(name2)

# The following if-statement tests if the '-z' flag is used and makes the corresponding adjustment.
        if name=='-z':
# The following loop initializes the key-value pairs for the entire alphabet, as is requested by the -z flag.
            for letter in ascii_lowercase:
                d[letter]=0

# The following if-statement checks if we have finally reached a file to read.
        if name.__contains__('.txt'):
            file = open(str(name), mode='r', encoding='ASCII')
            # print(file.read())
            add_frequencies(d, file, remove_case)

# The following line creates the dictionary that will serve as the final answer.
    d_final = dict()

# The final edit of the dictionary, in case the '-l' flag was entered.
    if l_is_true:
        for i in name2:
            if i in d:
                d_final[i] = d[i]
    else:
        d_final = d

    print(d_final)

    with open('data.csv', 'w') as f:
        for key in d_final.keys():
            f.write("%s, %s\n" % (key, d_final[key]))
        print(f)

main()
