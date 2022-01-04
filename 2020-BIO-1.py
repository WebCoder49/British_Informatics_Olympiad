# Roman Look-and-Say
import math
import time
from functools import lru_cache


@lru_cache(maxsize=None) # Save found numerals
def to_numerals(number:int):
    result = ""
    numerals = [("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)] # Greatest > Smallest
    num_numerals = 7
    subtraction_i = 0
    for i in range(len(numerals)):
        if(i % 2 == 0): # Change power-of-ten smaller than current numeral subtracted to prevent four-in-a-row
            subtraction_i += 2

        numeral, value = numerals[i]
        numeral_count = number // value
        if(numeral_count != 0):
            # Occurences of this numeral - subtract from number and add to numeral
            result += numeral*numeral_count
            number = number % value

        if(subtraction_i < num_numerals):
            sub_numeral, sub_value = numerals[subtraction_i]
            subtracted_value = value - sub_value
            if(number >= subtracted_value):
                # e.g. IX/CL to prevent 3-in-a-row
                result += sub_numeral + numeral
                number -= subtracted_value

        if(number == 0): break

    return result


def look_and_say(numerals:str):
    result = ""
    # Subtraction pairs only occur with I(V-X), X(C-D), C(D-M) (smaller power of ten placed before to prevent 3+-in-a-row)

    previous = ""
    count = 0
    for numeral in numerals:
        if(numeral == previous):
            # Build up block of numerals
            count += 1
        else:
            # Save previous block
            result += to_numerals(count) + previous
            # Start new block
            previous = numeral
            count = 1

    # Save previous block
    result += to_numerals(count) + previous

    return result

def apply_rlas_n_times(numeral, num_times):
    for i in range(num_times):
        numeral = look_and_say(numeral)

    # Get I- and V- counts
    i_count = 0
    v_count = 0
    for char in numeral:
        if(char == "I"):
            i_count += 1
        elif(char == "V"):
            v_count += 1

    return i_count, v_count

# Take inputs
numeral, num_times = input().split()
numeral = numeral.upper()
num_times = int(num_times)

# Process
i_count, v_count = apply_rlas_n_times(numeral, num_times)

# Output no. of Is then no.of Vs
print(i_count, v_count)