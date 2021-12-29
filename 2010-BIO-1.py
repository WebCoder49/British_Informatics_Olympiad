# Anagram Numbers

def is_anagram(a, b):
    a = str(a)
    b = str(b)
    # Set count of each digit in a - faster than popping
    a_count = [0] * 10
    for digit in a:
        a_count[int(digit)] += 1
    for digit in b:
        digit = int(digit)
        if(a_count[digit] <= 0):
            # None of this digit
            return False
        else:
            a_count[digit] -= 1

    for left_over in a_count:
        if left_over != 0:
            # Whole count not used up
            return False
    return True

def find_anagram_multipliers(number):
    # Only 8 digits (2->9) so quicker to try all
    multipliers = []

    for multiplier in range(2, 10):
        product = number * multiplier
        if(is_anagram(number, product)):
            multipliers.append(multiplier)

    return multipliers

def printed_list(li):
    if(len(li) == 0):
        return ("NO")
    else:
        return (" ".join(map(str, li)))

number = int(input("Number to Test: "))

print(printed_list(find_anagram_multipliers(number)))