# False plan
from functools import lru_cache


@lru_cache(maxsize=None) # Save previously found combinations
def possible_plans(num_letters, plan_len, repeat_limit, repeats_so_far):
    if(repeats_so_far > repeat_limit):
        return 0
    # Init RC
    repeat_counts = []
    for i in range(repeat_limit): # Item after last is pruned
        repeat_counts.append(0)

    total_branches = 1 # Need to remember to check 0 digs left
    # Add repeats so far - include in first iteration
    if(plan_len > 0):
        total_branches = num_letters
        if(repeats_so_far < repeat_limit):
            repeat_counts[repeats_so_far] += 1 # Becomes one-indexed repeats+1, all others one as in diff. dir - from root
        else:
            total_branches -= 1
        repeat_counts[0] += total_branches - 1  # All other branches become 1 in a row

    # Other iterations (branch growing)
    for i in range(plan_len-1):
        total_branches *= num_letters
        # Update repeat counts - branches of 1 extend to 2, 2 to 3, etc. and left become 1s as diff.
        # Shift across
        repeat_counts.insert(0, total_branches - sum(repeat_counts))
        pruned = repeat_counts.pop() # Prune away branches by subtracting
        total_branches -= pruned

    return total_branches

def nth_plan(plan_index, num_letters, plan_len, repeat_limit):
    plan = []
    plans_left = plan_index - 1 # Becomes zero-indexed
    repeats_so_far = 0
    # For each level of tree:
    for len_left in range(plan_len-1, -1, -1):
        # Batch remove as possible
        can_batch_remove = None
        letter_to_add = -1 # Letter increases as in alphabetical order; first iter will not remove any

        while(can_batch_remove is None or can_batch_remove <= plans_left): # Always <= so plans_left becomes 0
            # Batch-remove
            letter_to_add += 1
            if(not can_batch_remove is None):
                plans_left -= can_batch_remove

            # Repeats so far only matter if repeating same letter
            if(len(plan) == 0 or repeats_so_far == 0):
                current_repeats_so_far = 1
            elif(plan[-1] == letter_to_add):
                current_repeats_so_far = repeats_so_far + 1 # 1 for this time
                if(current_repeats_so_far > repeat_limit):
                    continue
            else:
                current_repeats_so_far = 1
            # Find next batch removal
            can_batch_remove = possible_plans(num_letters, len_left, repeat_limit, current_repeats_so_far)
            # print(plan, len_left, ":", plans_left, can_batch_remove, letter_to_add)

        # Adjust repeats so far
        if (len(plan) == 0 or plan[-1] != letter_to_add):
            # New repetition block
            repeats_so_far = 1
        else:
            # Another repeat of dig
            repeats_so_far += 1

        # print("Add", letter_to_add)
        plan.append(letter_to_add)

    return plan

def to_letters(plan:list):
    letters = ""

    for index in plan:
        letters += chr(65 + index) # A is 65

    return letters

# print(possible_plans(2, 0, 2, 1))

# Take inputs
diff_letters, adjacent_limit, plan_len = map(int, input().split())
index_n = int(input())

plan = nth_plan(index_n, diff_letters, plan_len, adjacent_limit)

print(to_letters(plan))