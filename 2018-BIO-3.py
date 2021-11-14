# Serial Numbers

from collections import deque

class SerialNumberGraph:
    visited_set = set()
    unvisited_queue = deque()

    def __init__(self, digits):
        self.digits = digits

    def to_string(self, arr:list):
        string = ""
        for i in arr:
            string += i

        return string

    def transformations(self, serial_number:str):

        transformations = []
        for i in range(self.digits-2):
            # Traverse string;

            transformation = []
            for digit in serial_number:
                transformation.append(digit)

            min_digit = min(serial_number[i], serial_number[i+1])
            max_digit = max(serial_number[i], serial_number[i+1])

            if(serial_number[i-1] > min_digit and serial_number[i-1] < max_digit and i > 0) or (serial_number[i+2] > min_digit and serial_number[i+2] < max_digit and i < self.digits-2):
                # Adjacent digit lies between
                # Swap indexes i and i+1
                transformation[i] = serial_number[i+1]
                transformation[i+1] = serial_number[i]

                transformations.append(self.to_string(transformation))

        return transformations

    def longest_path(self, current_number:str):
        self.unvisited_queue = deque() # Empty
        self.unvisited_queue.append((current_number, 0))
        self.visited_set = set() # Empty
        self.visited_set.add(current_number)

        # Breadth-first search

        while(len(self.unvisited_queue) > 0):
            current = self.unvisited_queue.popleft()
            dist = current[1]
            current = current[0]
            for t in self.transformations(current):
                if(not t in self.visited_set):
                    self.unvisited_queue.append((t, dist+1))
                    self.visited_set.add(t)
            print(self.unvisited_queue)
        print(len(self.visited_set), self.visited_set)
        return dist

while True:
    digits = int(input("Number of Digits: "))
    serial_number = input("Serial Number: ")
    graph = SerialNumberGraph(digits)
    print(graph.longest_path(serial_number))