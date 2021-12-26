# Modern Art
import math
from copy import copy

def possible_arrangements(artists):
    total_paintings = 0
    duplicates_per_arrangement = 1
    # Find all arrangements, then remove duplicates
    for artist in artists:
        total_paintings += artist
        duplicates_per_arrangement *= math.factorial(artist) # Different orders of indistinguishable = same
    return math.factorial(total_paintings) // duplicates_per_arrangement

def alphabet(arrangement):
    result = ""
    for index in arrangement:
        result += chr(65 + index) # From A
    return result

inputted = list(map(int, input().split()))
artists = inputted[:-1]
find_nth = inputted[-1]
print(possible_arrangements(artists), "arrangements")
length = sum(artists)

arrangement = []

for spaces_left in range(length-1, -1, -1): # Down to 0
    # Choose next digit - batch remove subtrees
    can_batch_remove = 0
    digit_to_use = -1
    while(can_batch_remove < find_nth):
        # Batch remove
        find_nth -= can_batch_remove
        digit_to_use += 1
        # Find size of next batch remove
        temp_artists = copy(artists)
        temp_artists[digit_to_use] -= 1
        if(temp_artists[digit_to_use] >= 0):
            can_batch_remove = possible_arrangements(temp_artists)
        else:
            can_batch_remove = 0 # None left from artist
        # print(digit_to_use, "temp", temp_artists, can_batch_remove, find_nth)

    artists = temp_artists
    # print(artists)

    arrangement.append(digit_to_use)

print("Arrangement: ", alphabet(arrangement))