# Unlock
import copy
from collections import deque

# TODO: EBI: This wasn't BFS - It didn't ask for shortest path; My program doesn't work (greedy not proven) but good try as works on some

# 2022-12-28 Marking (1 right, 0 wrong, * bug):
# 011110000 8/24

SIZE = 5

def letter2indexAndCase(letter):
   """Convert a letter into its 0-indexed alphabet index and boolean case=upper"""
   letter = ord(letter)
   if(letter < 97):
        # Uppercase
        return letter-65, True
   else:
       # Lowercase
       return letter - 97, False

def indexAndCase2letter(isUppercase, index):
   """Convert a 0-indexed alphabet index and boolean case=upper into a letter"""
   if isUppercase:
       # Uppercase
       return chr(index+65)
   else:
       # Lowercase
       return chr(index+97)

def repr2matrix(repr:str):
    """Convert the string repr to a 1D list of states 0off/1dim/2bright"""
    matrix = [0 for i in range(SIZE**2)]
    for char in repr:
        # matrix[]
        index, bright = letter2indexAndCase(char)
        if(bright):
            matrix[index] = 2
        else: # Dim
            matrix[index] = 1
    return matrix

def matrix2repr(matrix:list):
    """Convert the 1D list of states 0off/1dim/2bright to a string repr"""
    repr = ""
    for i in range(SIZE**2):
        if(matrix[i] != 0):
            # Dim = lowercase; Bright = uppercase
            repr += indexAndCase2letter(matrix[i] == 2, i)
    return repr

def showMatrix(matrix:list):
    for i in range(0, len(matrix), SIZE):
        print(matrix[i:i+SIZE])

def pressButton(i:int,nextMatrix:list):
    """Change matrix to press button at i"""
    directions = [i]  # deltaindex
    if (i % SIZE > 0):
        # Left
        directions.append(i - 1)
    if (i % SIZE < SIZE - 1):
        # Right
        directions.append(i + 1)
    if (i < SIZE * (SIZE - 1)):
        # Down
        directions.append(i + SIZE)
    if (i >= SIZE):
        # Up
        directions.append(i - SIZE)

    for button in directions:
        # print(">", button, nextMatrix[button], "vvv")
        nextMatrix[button] += 1
        nextMatrix[button] %= 3
        # print(nextMatrix[button])

# 1. 45m
# BFS - Too slow
# def bfsPathToOff(firstMatrix:list):
#     if(sum(firstMatrix) == 0): return ""
#     # BFS
#     q = deque([(firstMatrix, "")])  # (matrix,path)
#     visited = set()
#     while q:
#         matrix, path = q.popleft()
#         for i, nextMatrix in enumerate(nextMatrices(matrix)):
#             nextButton = indexAndCase2letter(False, i)
#             if (not tuple(nextMatrix) in visited and (nextButton != matrix[-1] or nextButton != matrix[-2])): # No 3 consec
#                 visited.add(tuple(nextMatrix))
#                 # print(path + nextButton, matrix2repr(nextMatrix))
#                 if (sum(nextMatrix) == 0): return path + nextButton
#                 q.append((nextMatrix, path + nextButton))

# 2. 10m
def getPathToOff(matrix:list):
    """"""
    path = ""

    visited = set()

    lastPressed = None  # Can't press (/double-press) same index twice
    while True:
        # Greedily check all possible pressed sqs
        maxToImprove = 0 # Max equal non-zero
        maxIsOne = False # Max is one
        maxIndex = False # Press this button

        for i in range(SIZE**2):
            directions = [i]  # index
            if (i % SIZE > 0):
                # Left
                directions.append(i - 1)
            if (i % SIZE < SIZE - 1):
                # Right
                directions.append(i + 1)
            if (i < SIZE * (SIZE - 1)):
                # Down
                directions.append(i + SIZE)
            if (i >= SIZE):
                # Up
                directions.append(i - SIZE)

            oneCount = 0
            twoCount = 0
            for node in directions:
                if(matrix[node] == 1):
                    oneCount += 1
                elif(matrix[node] == 2):
                    twoCount += 1

            if i != lastPressed:
                # Get max number of same non-zero sqs
                if oneCount > maxToImprove and oneCount > twoCount:
                    maxToImprove = oneCount
                    maxIsOne = True
                    maxIndex = i
                elif twoCount > maxToImprove:
                    maxToImprove = twoCount
                    maxIsOne = False
                    maxIndex = i

        tuple_matrix = tuple(matrix)
        if sum(matrix) == 0:
            # Solved
            return path
        elif tuple_matrix in visited:
            return "IMPOSSIBLE"
        visited.add(tuple_matrix)

        # Press/double-press best
        if(maxIsOne):
            # Double-press
            pressButton(maxIndex,matrix)
            pressButton(maxIndex, matrix)
            # showMatrix(matrix)
            # print()
            path += (indexAndCase2letter(True, maxIndex))
        else:
            # Press once
            pressButton(maxIndex, matrix)
            # showMatrix(matrix)
            # print()
            path += (indexAndCase2letter(False, maxIndex))
        lastPressed = maxIndex

repr = input()
# repr = "mqrsw"

matrix = repr2matrix(repr)

print(getPathToOff(matrix))

# showMatrix(matrix)