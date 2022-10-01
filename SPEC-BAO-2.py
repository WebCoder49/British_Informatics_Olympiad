# Box constellations
import math
import time

stars_len = int(input())
stars_inputted = input().split()
stars = []
for i in range(stars_len):
    stars.append((int(stars_inputted[2*i]),int(stars_inputted[2*i+1])))

# stars = [(1,2),(2,0),(2,3),(3,1),(3,4),(4,2)] # Area 6.00
# stars = [(0,0),(0,1),(1,0),(1,2)] # Area 1.50

lines_by_gradient = {} # grad: [[star1,star2]...]

# Get lines
for first_i in range(stars_len):
    for second_i in range(first_i):
        # Pair of stars
        first_star = stars[first_i]
        second_star = stars[second_i]
        if(second_star[0] == first_star[0]):
            gradient = float("inf")
        else:
            gradient = ((second_star[1]-first_star[1])/(second_star[0]-first_star[0])) # deltay/deltax
        if(gradient in lines_by_gradient):
            lines_by_gradient[gradient].append((first_star,second_star))
        else:
            lines_by_gradient[gradient] = [(first_star,second_star)]

max_area = 0
# Check for max area
for gradient in lines_by_gradient:
    if (gradient == float("inf")):
        area_denom = 2
    else:
        area_denom = 2*math.sqrt(1 + gradient*gradient)
    max_area_num = 0
    max_area_lines = []

    lines = lines_by_gradient[gradient]
    for first_line_i in range(len(lines)):
        for second_line_i in range(first_line_i):
            # Check area num
            first_line = lines[first_line_i]
            second_line = lines[second_line_i]
            if(gradient == float("inf")):
                # print(first_line,second_line)
                x_diff = first_line[0][0]-second_line[0][0]
                first_len = math.fabs(first_line[1][1]-first_line[0][1])# y diff
                second_len = math.fabs(second_line[1][1] - second_line[0][1])  # y diff
                area_num = x_diff * (first_len + second_len)
                # print(area_num, "x diff", x_diff, "l", first_len, second_len)
            else:
                c_diff = math.fabs((first_line[0][1]-gradient*first_line[0][0]) - # y-mx1
                             (second_line[0][1]-gradient*second_line[0][0])) # y-mx2 - diff in c

                first_len = math.sqrt(math.fabs(first_line[0][0]-first_line[1][0])**2 + # deltax^2
                             math.fabs(first_line[0][1]-first_line[1][1])**2) # deltay^2

                second_len = math.sqrt(math.fabs(second_line[0][0] - second_line[1][0]) ** 2 +  # deltax^2
                                      math.fabs(second_line[0][1] - second_line[1][1]) ** 2)  # deltay^2

                area_num = c_diff * (first_len + second_len)
                # print("area", area_num/area_denom, "lines", first_line, first_len, second_line, second_len)

            if (area_num > max_area_num):
                max_area_num = area_num

    area = max_area_num / area_denom
    if(area > max_area):
        max_area = area

# Round to 2dp
max_area = round(max_area * 100)/100
print(max_area)