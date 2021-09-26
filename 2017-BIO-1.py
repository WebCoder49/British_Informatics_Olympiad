#  Coloured Triangles

def last_row(row):
    next_row = []

    if (len(row) == 1): return row[0] # Edited after

    for i in range(len(row)-1):
        if(row[i] == row[i+1]):
            # Identical
            next_row.append(row[i])
        else:
            # Different
            two_colours = [row[i], row[i + 1]]
            if (not "R" in two_colours): next_row.append("R")
            if (not "G" in two_colours): next_row.append("G")
            if (not "B" in two_colours): next_row.append("B")

    if(len(next_row) == 1): return next_row[0]
    else: return last_row(next_row)

print(last_row(input("Starting row: ").upper()))