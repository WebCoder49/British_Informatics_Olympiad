from collections import deque

# Window Dressing

# 2022-11-30 Marking (1 right, 0 wrong, * bug):
# 111111111111111 24/24

def alphabet_to_numerical(word:str):
    """Convert an uppercase string to a list of alphabet indexes"""
    result = []
    for char in word:
        result.append(ord(char)-65)
    return result

def generate_neighbours(order:list, max_len):
    next_box = len(order)
    result = []
    if(next_box < max_len):
        # Add
        result.append(order + [next_box])
    if(next_box >= 3):
        # Swap; difft. to rotate
        result.append([order[1], order[0]] + order[2:])
    if(next_box >= 2):
        # Rotate
        result.append(order[1:] + [order[0]])
    return result

def min_operations(desired_order):
    order = [] # No boxes at first
    max_len = len(desired_order)

    # BFS
    visited = set()
    order_q = deque([(order,0)]) # (order, dist)
    while(order_q):
        order, dist = order_q.popleft()
        order_tuple = tuple(order)
        if(not order_tuple in visited):
            visited.add(order_tuple)
            for neighbour in generate_neighbours(order, max_len):
                order_q.append((neighbour,dist+1))
                # print(order_tuple, neighbour, dist)
                if(neighbour == desired_order):
                    return dist+1
    return -1 # Cannot be transformed to

# Take inputs
desired_order = input()
desired_order = alphabet_to_numerical(desired_order.upper())

print(min_operations(desired_order))

# TODO: Fix; remove increasing length if unnecessary