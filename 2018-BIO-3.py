# Serial Numbers

class SerialNumberGraph:
    distances = {}

    def __init__(self, digits, starting_number):
        print(self.transformations(starting_number, [starting_number], 0))

    def transformations(self, serial_number:list, already_visited, level):

        transformations = []
        for i in range(len(serial_number)-2):

            transformation = []
            for digit in serial_number:
                transformation.append(digit)

            min_digit = min(serial_number[i], serial_number[i+1])
            max_digit = max(serial_number[i], serial_number[i+1])

            if(serial_number[i-1] > min_digit and serial_number[i-1] < max_digit) or (serial_number[i+2] > min_digit and serial_number[i+2] < max_digit):
                # Adjacent digit lies between
                # Swap indexes i and i+1
                transformation[i] = serial_number[i+1]
                transformation[i+1] = serial_number[i]

                transformations.append(transformation)


        max_distance = 1
        already_visited_next_level = already_visited+transformations

        print(">" * level, serial_number)
        for transformation in transformations:
            if(not transformation in already_visited):
                distance = 1+self.transformations(transformation, already_visited_next_level, level+1)
                if(distance > max_distance):
                    max_distance = distance

        self.distances["".join(serial_number)] = max_distance
        print("<"*level, serial_number, max_distance, self.distances, transformations)

        return max_distance


serial_number = list(input("Serial Number: "))
serial_number_graph = SerialNumberGraph(len(serial_number), serial_number)