# Juggl(ug)ing
from collections import deque
from copy import copy


def possible_steps(total_capacities:tuple, current_capacities:tuple, no_of_jugs):
    print("Finding ")
    dests = []
    for src_i in range(no_of_jugs):
        src_current_capacity = current_capacities[src_i]
        src_total_capacity = total_capacities[src_i]

        if(src_current_capacity < src_total_capacity):
            # Fill up
            next_capacities = list(current_capacities)
            next_capacities[src_i] = src_total_capacity
            yield tuple(next_capacities) # Only generate when needed
        if(src_current_capacity > 0):
            # Empty
            next_capacities = list(current_capacities)
            next_capacities[src_i] = 0
            yield tuple(next_capacities)
        for dest_i in range(no_of_jugs):
            if(dest_i != src_i):
                # Transfer
                next_capacities = list(current_capacities)
                dest_current_capacity = current_capacities[dest_i]
                dest_total_capacity = total_capacities[dest_i]

                if(src_current_capacity > 0 and dest_current_capacity < dest_total_capacity):
                    # Can be filled up more
                    dest_current_capacity += src_current_capacity
                    if(dest_current_capacity > dest_total_capacity):
                        # Overflow back to src
                        src_next_capacity = dest_current_capacity - dest_total_capacity # After marking - Don't use current capacity as one of multiple next steps
                        dest_current_capacity = dest_total_capacity
                    else:
                        src_next_capacity = 0 # Completely emptied
                    next_capacities[src_i] = src_next_capacity
                    next_capacities[dest_i] = dest_current_capacity

                    yield tuple(next_capacities)

# Breadth-first search
def search_capacity(jug_capacities:tuple, target_capacity:int):
    # Return number of steps taken to reach an arrangement w/ target capacity
    no_of_jugs = len(jug_capacities)
    starting_capacities = (0,)*no_of_jugs
    # Init Breadth-First Search
    visited = {starting_capacities} # Set
    queue = deque((
        (0, starting_capacities),
    )) # Distance, data

    not_found = True
    while not_found:
        dist, current_node = queue.pop()
        # print(dist, current_node) # After
        dist = dist + 1
        for next_node in possible_steps(jug_capacities, current_node, no_of_jugs):
            # print("-->", next_node)
            if(target_capacity in next_node):
                not_found = False
                break # No need to find other

            if(next_node not in visited):
                # Unvisited so add to queue
                visited.add(next_node)
                queue.appendleft((dist, next_node))

    return dist

no_of_jugs, target_capacity = tuple(
    map(int, input().split())  # Turn space-separated input into tuple of ints
)
jug_capacities = tuple(
    map(int, input().split())  # Turn space-separated input into tuple of ints
)[:no_of_jugs]

# After marking
print("{} steps".format(search_capacity(jug_capacities, target_capacity))) # Careless error: Needed to pass in inputs here
