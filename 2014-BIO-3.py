# Increasing Passwords

# Next Char must be > previous
# e.g. out of digits 0, 1, 2 and 3:
# 0, 1, 2, 3, 0(1-3), 1(2-3), 23, 012, 013, 023, 123
# 1+1+1+1=4 with 1 digit, 3+2+1=6 with 2 digits, (2+1)+(1)=4 with 3 digits
import math

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def number_of_passwords(digits_usable, spaces_available):
    number = 1

    # Find number of diff. orders
    for choices_left in range(digits_usable, digits_usable-spaces_available, -1):
        # e.g. for 5 digits in 3 spaces, 5 for first, 4 for second, 3 for third: 5x4x3
        number *= choices_left
    # Only alphabetical order means only one order per combo.
    # Combos of spaces digits = spaces!
    # Therefore div by spaces!
    number /= math.factorial(spaces_available)

    return int(number)


def to_alphabet(password):
    string = ""
    for char in password:
        if len(alphabet) > char:
            string += alphabet[char]
        else:
            print(string, char)
    return string

while True:

    ALPHABET_DIGITS = 36  # 26+10
    permutations_remaining = int(input("PWD Index: "))-1  # 0-indexed

    # Get number of digits in password = length
    to_use_up = 0
    length = 0
    while(to_use_up <= permutations_remaining):
        # Batch-remove permutations
        permutations_remaining -= to_use_up
        length += 1
        # Discard permutations of length if possible
        to_use_up = number_of_passwords(ALPHABET_DIGITS, length)

    # Find password by moving down tree and batch-removing groups
    permutation = []
    digit_to_use = -1
    for spaces_left in range(length-1, -1, -1): # Down to 0
        # Batch-remove
        to_use_up = 0
        print(spaces_left, permutation, digit_to_use)

        while (to_use_up <= permutations_remaining):
            # Batch-remove permutations
            permutations_remaining -= to_use_up
            digit_to_use += 1  # Next letter in alphabet at end means 1 fewer digits as in alphabetical order
            # Discard permutations if possible
            to_use_up = number_of_passwords(ALPHABET_DIGITS-1 - digit_to_use, spaces_left) # AB_DIGITS-1 - digs_to_use to remove duplicates
            print("Use", to_use_up, "for", ALPHABET_DIGITS-1 - digit_to_use, "in", spaces_left, permutations_remaining, "Remaining")

        permutation.append(digit_to_use)

    print("Password:", to_alphabet(permutation))