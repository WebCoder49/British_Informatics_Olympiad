# Question 2: Trail
import random


class Trail:

    trail = [[0, 0]] # Contain initial square

    def __init__(self, trail_len):
        self.trail_len = trail_len

    def move(self, coords):
        # Add coords to trail then move
        self.trail.append(coords)

    def fade(self):
        while (len(self.trail) > self.trail_len):  # Fade
            # Remove oldest square
            self.trail.pop(0)

    def is_blocked(self, coords):
        # print(coords, self.trail)
        return coords in self.trail

class Explorer:
    coords = [0, 0]
    direction = 0  # 0 = Up, 1 = Right, 2 = Down, 3 = Left

    def __init__(self, trail_len, instructions):
        self.instructions = instructions
        self.instruction_len = len(instructions)

        self.trail = Trail(trail_len)

    def final_coordinates(self, n_of_moves):
        for i in range(n_of_moves):
            # print(i, "***")
            # Follow instructions
            instruction = self.instructions[i % self.instruction_len]
            if(instruction == "R"):
                self.direction += 1
                self.direction %= 4
            elif(instruction == "L"):
                self.direction += 3
                self.direction %= 4
            # Move
            if(not self.move()): # Cannot move
                break

        return self.coords

    def next_square(self, coords, direction):
        if(direction == 0): # Up
            return [coords[0], coords[1]+1]
        elif(direction == 1): # Right
            return [coords[0]+1, coords[1]]
        elif(direction == 2): # Down
            return [coords[0], coords[1]-1]
        elif(direction == 3): # Left
            return [coords[0]-1, coords[1]]

    def move(self):
        next_square = self.next_square(self.coords, self.direction)
        # print(self.coords, ">", self.direction, ">", next_square)
        if(self.trail.is_blocked(next_square)):
            self.direction += 1 # 90deg right
            self.direction %= 4
            # print("BLOCKED", self.direction)
            return self.move()
        else:
            self.trail.move(next_square)
            self.coords = next_square
            self.trail.fade()
            return True


explorer = Explorer(int(input("Trail length: ")), input("Instructions: ").upper())
print(explorer.final_coordinates(int(input("Number of moves: "))))