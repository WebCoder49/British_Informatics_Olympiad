# Palindromic Numbers
import math

def next_palindrome(initial_number:str):
    # A palindrome consists of:
    # first_half middle_digit? first_half_reversed
    half_length = math.floor(len(initial_number)/2)
    first_half = initial_number[:half_length]

    if(len(initial_number) % 2 == 0):
        # Even length - no middle_digit
        middle_digit = ""
    else:
        # Odd length
        middle_digit = initial_number[half_length:half_length+1]

    # Check for palindromes, increase until is larger than number
    initial_number = int(initial_number)
    palindrome = first_half + middle_digit + first_half[::-1]
    stay_in_loop = True

    while (int(palindrome) <= initial_number or stay_in_loop):

        stay_in_loop = False
        if(middle_digit == ""):
            # No middle digit, so increase first half
            initial_length = len(first_half)
            first_half = str(int(first_half)+1)
            new_length = len(first_half)

            if (new_length > initial_length):
                # length of number increased - now even len, add middle digit
                middle_digit = first_half[-1:]  # Final digit
                first_half = first_half[:-1]
        else:
            # Increase middle_digit and first half as one number - changed after seeing markscheme
            first_half_with_middle_digit = first_half + middle_digit

            initial_length = len(first_half_with_middle_digit)

            first_half_with_middle_digit = str(int(first_half_with_middle_digit) + 1)

            new_length = len(first_half_with_middle_digit)

            if(new_length == initial_length):
                middle_digit = first_half_with_middle_digit[-1:] # Final digit
            else:
                # length of number increased - now even len, no middle digit
                middle_digit = ""
            first_half = first_half_with_middle_digit[:-1]


        palindrome = first_half + middle_digit + first_half[::-1]

    return palindrome


print("Next higest palindrome:", next_palindrome(input("Positive integer: ")))