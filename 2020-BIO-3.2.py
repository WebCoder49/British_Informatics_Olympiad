# False Plan
import math

# 2022-11-21 Marking (1 right, 0 wrong, * bug):
# 1111111111111111 27/27

def num_plans(adjacent_before, num_chars:int, max_adjacent:int, plan_len:int):
    result = 1

    # This approach failed. TODO:EBI: Don't let efficiency get too much in the way of functionality
    # for i in range(plan_len):
    #     result *= num_chars
    #     if (i >= max_adjacent):
    #         # Remove many adjacent
    #         print("Remove",num_chars)
    #         result -= num_chars
    #     elif((i+adjacent_before) >= max_adjacent):
    #         # Remove one adjacent
    #         print("Remove 1")
    #         result -= 1
    # return result

    if(adjacent_before > max_adjacent):
        return 0
    if(plan_len == 0): return 1


    # [Looked at Last Time] - store list of number of branches w/ n adjacent and use it as a queue
    branches_by_adjacent = [0 for _ in range(max_adjacent+1)] # Last is max

    total_branches = num_chars
    branches_by_adjacent[0] = num_chars-1 # 1 repeat
    if(adjacent_before != max_adjacent):
        branches_by_adjacent[adjacent_before] += 1 # 1 repeat
    else:
        total_branches -= 1

    for i in range(plan_len-1):
        # print(branches_by_adjacent, total_branches)
        total_branches *= num_chars


        num_one_adjacent = 0
        for adjacent_i in range(max_adjacent-1, -1, -1):
            # Extend each branch: 1 w/ one more adjacent; rest with 1 adjacent
            branches_by_adjacent[adjacent_i+1] = branches_by_adjacent[adjacent_i]
            num_one_adjacent += branches_by_adjacent[adjacent_i]*(num_chars-1)

        branches_by_adjacent[0] = num_one_adjacent

        # Prune too long branches
        to_prune = branches_by_adjacent[-1] # too many adjacent
        total_branches -= to_prune

    # print(branches_by_adjacent, total_branches)

    return total_branches

# print(num_plans(0, 2, 2, 0))

def to_alphabet(letters:list):
    """Convert list of alphabet i to string"""
    result = ""
    for letter_i in letters:
        result += chr(letter_i+65) # Capital letters
    return result


num_chars, max_adjacent, plan_len = map(int, input().split())
n_left = int(input())-1 # 0-indexed

# print(num_chars, max_adjacent, plan_len, n_left)

plan = [] # In alphabet-integers
adjacent_before = 0
for len_left in range(plan_len-1, -1, -1):
    # print(plan, n_left)
    # "Batch-remove" one branch of plans
    to_batch_remove = 0
    this_char = -1
    while(to_batch_remove <= n_left):
        # Next char - can batch remove all possibilities for last char
        # if(to_batch_remove > 0): print("-", to_batch_remove)
        n_left -= to_batch_remove
        this_char += 1

        if(len(plan) > 0 and this_char == plan[-1]):
            # Adjacent
            # print("Adjacent", adjacent_before+1)
            to_batch_remove = num_plans(adjacent_before+1, num_chars, max_adjacent, len_left)
        else:
            # Not adjacent
            to_batch_remove = num_plans(1, num_chars, max_adjacent, len_left)

        # print(to_batch_remove, "starting with", plan+[this_char], len_left)
    # print(plan, "!", to_batch_remove)

    # Keep track of adjacent length
    if(len(plan) > 0 and this_char == plan[-1]):
        # print("Repeated ", this_char)
        adjacent_before += 1
    else:
        adjacent_before = 1

    plan.append(this_char)
print(to_alphabet(plan))