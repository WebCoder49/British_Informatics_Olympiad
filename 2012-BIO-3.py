# Number Ladder

# 2023-01-03 Marking (1 right, 0 wrong, * bug):
# 11100000 = 5/23

from collections import deque
from functools import lru_cache

DIGIT_WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
for i in range(len(DIGIT_WORDS)):
    # To list of letter indices
    DIGIT_WORDS[i] = list(map(lambda letter: ord(letter)-65, DIGIT_WORDS[i]))

@lru_cache(maxsize=None) # Memoise
def int2letterCounts(num:str):
    # print(num)
    letter_counts = [0 for _ in range(26)]
    for char in num:
        digit = ord(char)-48 # To int
        for letter_ind in DIGIT_WORDS[digit]:
            letter_counts[letter_ind] += 1
    return tuple(letter_counts)

@lru_cache(maxsize=None)
def isTransformation(num1:tuple, num2:tuple): # Both letter counts
    letter_changes = 0
    for i in range(26):
        if num1[i] != num2[i]:
            # Letter added/deleted
            if letter_changes == 5:
                return False # Too many changes

            # print("Changed", chr(i+65), abs(num1[i]-num2[i]))
            letter_changes += abs(num1[i]-num2[i])
    return True

def getTransformations(num1:tuple): # In and Out as letter counts
    transformations = []
    # "only uses numbers between 1 and 999 inclusive"
    for i in range(1, 1000):
        num2 = int2letterCounts(str(i))
        if isTransformation(num1, num2):
            transformations.append(num2)
    return transformations

def bfsShortestLadder(num1:str, num2:str):
    num1 = int2letterCounts(num1)
    num2 = int2letterCounts(num2)
    q = deque([(num1,0)]) # Each letter count, dist

    visited = set()
    while(q):
        node, dist = q.popleft()
        for neighbour in getTransformations(node):
            if neighbour == num2:
                return dist+1
            if not neighbour in visited:
                visited.add(neighbour)
                q.append((neighbour, dist+1))

# Main
start1, finish1 = input().split() # Strings
start2, finish2 = input().split() # Strings
start3, finish3 = input().split() # Strings
print(bfsShortestLadder(start1, finish1))
print(bfsShortestLadder(start2, finish2))
print(bfsShortestLadder(start3, finish3))