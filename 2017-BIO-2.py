# Dots and Boxes

grid_width = 6
grid_height = 6
grid_size = grid_height * grid_width

# Initialise grid as array

vertical_lines = []
for y in range(5):
    row=[]
    for x in range(5):
        row.append(False)
    vertical_lines.append(row)

horizontal_lines = []
for y in range(5):
    row=[]
    for x in range(5):
        row.append(False)
    horizontal_lines.append(row)

def add_line(dot_number, )