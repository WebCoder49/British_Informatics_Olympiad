# Child's Play

# 2022-11-07 Marking (1 right, 0 wrong, * bug):
# 11111100000 11/23
# TODO: EBI: Check why not working

from functools import lru_cache

# @lru_cache(maxsize=None)
# def num_arrangements(sum:int):
#     if sum == 1: return 1 # (1)
#     if sum <= 0: return 0
#
#     result = 1 # (sum)
#     for first_block in range(1, sum):
#         result += num_arrangements(sum-first_block)
#     return result


# Pattern spotted
def num_arrangements(sum:int):
    return 2 ** (sum-1)

def get_nth(n_left:int, sum_left:int):
    arrangement = []
    while sum_left > 0:
        next_block = 0
        to_batch_remove = 0
        # None w/ 0 - for first iter
        while(to_batch_remove <= n_left):
            n_left -= to_batch_remove # Prune

            # Calc. next
            next_block += 1
            sum_left -= 1
            to_batch_remove = num_arrangements(sum_left)
        arrangement.append(next_block)
    return arrangement

# sum, n = map(int, input().split())
# n -= 1 # 0-ind
#
# print(" ".join(map(str, get_nth(n, sum))))

for n in range(0, 2 ** 13):
    print(get_nth(n, 14))