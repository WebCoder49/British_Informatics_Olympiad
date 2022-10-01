# String Theory
# DO NOT TRY TO OPTIMISE CODE IF OPTIMISATION BECOMES TOO COMPLICATED.

# # Too complicated - should use iterative method
#
# string = input()
# chars = list(string)
#
# def alphabet_i(uppercase_letter):
#     return ord(uppercase_letter)-65;
#
# def check_portal(chars: list, i, iterate: bool, past_strs=set()):
#     if(i >= (len(chars) - 1) or i < 0 or tuple(chars) in past_strs):
#         # Pair out of range / previously found so inf. loop
#         return
#     past_strs.add(tuple(chars));
#     print(chars[i:])
#     # Check and act for portals at i
#     first_i = alphabet_i(chars[i])
#     second_i = alphabet_i(chars[i + 1])
#     if (first_i == 25 - second_i):
#         # portal at i
#         first_letter = None
#         second_letter = None
#
#         if(i != len(chars)-1):
#             # Previously i+1
#             second_letter = chars[i+1]
#             del chars[i+1]
#         if(i != 0):
#             first_letter = chars[i-1]
#             del chars[i-1]
#
#         if (first_i > second_i):
#             # Teleport to start & check first 2 to here
#             num_letters_teleported = 0
#             if(second_letter is not None):
#                 chars.insert(0, second_letter)
#                 num_letters_teleported += 1
#             if(first_letter is not None):
#                 chars.insert(0, first_letter)
#                 num_letters_teleported += 1
#             print("start")
#             print(chars)
#
#             check_portal(chars, 0, False, past_strs)
#             check_portal(chars, 1, False, past_strs)
#             # 2 chars removed before
#             # Pair from across first teleported, with index shifted
#             check_portal(chars, max(2, i+num_letters_teleported-2), False, past_strs)
#             check_portal(chars, max(2, i + num_letters_teleported-1), False, past_strs)
#             check_portal(chars, max(2, i + num_letters_teleported), False, past_strs)
#         else:
#             # Don't need to check before; teleport to end
#             if (first_letter is not None):
#                 chars.append(first_letter)
#             if (second_letter is not None):
#                 chars.append(second_letter)
#             print("end")
#             print(chars)
#
#             # Pair from across first teleported
#             check_portal(chars, i - 2, False)
#             check_portal(chars, i - 1, False)
#             check_portal(chars, i, False)
#     if(iterate):
#         # Try next pair
#         check_portal(chars, i+1, True)
# check_portal(chars, 0, True)
# print("".join(chars))

# Simpler - more foolproof, but less optimisation

# string = input().upper()
string = "AZCYB"
chars = list(string)

def alphabet_i(uppercase_letter):
    return ord(uppercase_letter)-65

has_portals = True
visited_words = set()

len_chars = len(chars)

while(has_portals):
    has_portals = False
    if (tuple(chars) in visited_words):
        print("Infinite")
        break
    visited_words.add(tuple(chars))

    for i in range(0, len_chars-1):
        first_i = alphabet_i(chars[i])
        second_i = alphabet_i(chars[i + 1])
        if (first_i == 25 - second_i):
            # portal at i
            first_letter = None
            second_letter = None

            # Previously i+1; not last char as must have second to be pair
            second_letter = chars[i+1]
            del chars[i+1]
            if(i != 0):
                first_letter = chars[i-1]
                del chars[i-1]

            if (first_i > second_i):
                # Teleport to start & check first 2 to here
                num_letters_teleported = 0
                if(second_letter is not None):
                    chars.insert(0, second_letter)
                if(first_letter is not None):
                    chars.insert(0, first_letter)
                # print("start")
                # print(chars)
            else:
                # Don't need to check before; teleport to end
                if (first_letter is not None):
                    chars.append(first_letter)
                if (second_letter is not None):
                    chars.append(second_letter)
                # print("end")
                # print(chars)
            has_portals = True
            break
else:
    # Not infinite loop
    print("".join(chars))