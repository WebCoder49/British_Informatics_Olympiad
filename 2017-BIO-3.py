# Mystery Parcel
from functools import lru_cache


def unique_items_with_sum(num_items, sum_needed, max_item, found_set=None, current=tuple(), visited_set=None):
    # After mark
    if(found_set == None):
        found_set = set()
    if (visited_set == None):
        visited_set = set()

    # Ensure unique
    sort_current = sort(current)
    if(sort_current in visited_set):
        return 0 # Reached this combination already; looking for unique
    visited_set.add(sort_current)

    if(num_items == 0):
        if(sum_needed == 0):
            found_set.add(current)
            return 1 # found
        else:
            return 0
    # Recursively find combinations of items w/ given sum
    max_possible = sum_needed-num_items+2 # Assuming other symbols all 1s - <max_possible
    min_possible = sum_needed-max_item*(num_items-1)
    count = 0
    for i in range(max(min_possible, 1), min(max_possible, max_item+1)):
        count += unique_items_with_sum(num_items-1, sum_needed-i, max_item, found_set, current+(i,), visited_set)
        # Reference holds for set
    return count


# All orders, but e.g. if 2 2s will count as separate (1, 2a, 1) or (1, 2b, 1) = x2, or: (2a, 2a), ab, ba, bb = x4
def countable_items_with_sum(num_items, sum_needed, max_item, counts, found_set=set(), current=tuple()):

    if(num_items == 0):
        if(sum_needed == 0):
            found_set.add(current)
            return 1 # found
        else:
            return 0
    # Recursively find combinations of items w/ given sum
    max_possible = sum_needed-num_items+2 # Assuming other symbols all 1s - <max_possible
    min_possible = sum_needed-max_item*(num_items-1)
    count = 0
    for i in range(max(min_possible, 1), min(max_possible, max_item+1)):
        # Multiply by diff. values @ i (2a, 2b...)
        count += counts[i-1] * countable_items_with_sum(num_items-1, sum_needed-i, max_item, counts, found_set, current+(i,))
        # Reference holds for set
    return count

@lru_cache(maxsize=None)
def sort(arr:tuple):
    arr = list(arr)
    arr_len = len(arr)
    i = 0
    while(i < arr_len-1):
        if(arr[i]>arr[i+1]):
            # Swap
            temp_i = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp_i
            # Move back as swapped
            if(i > 0):
                i -= 1
                continue
        i += 1

    arr = tuple(arr)
    return arr

def num_distributions(num_parcels, max_item, total_items, weight_per_parcel):
    parcel_counts = []
    for num_items in range(1, total_items+1):
        print(num_items, weight_per_parcel, max_item)
        # Parcels must be unique - combinations indistinguishable
        parcel_counts.append(unique_items_with_sum(num_items, weight_per_parcel, max_item))
    print(parcel_counts)
    parcels = set()
    return countable_items_with_sum(num_parcels, total_items, total_items, [1, 1, 1, 1], parcels)

# Take inputs
num_parcels, max_item, total_items, weight_per_parcel = map(int, input().split())

found = set()
print(unique_items_with_sum(2, 3, 3, found))
print(found)

print(num_distributions(num_parcels, max_item, total_items, weight_per_parcel))