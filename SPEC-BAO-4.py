# Air Cargo

# [TODO:] EBI: Don't use unsuitable data structures (e.g. queue - cannot know when get to end; use set rather than list if want to often remove)

# 2022-11-08 Marking (1 right, 0 wrong, * bug):
# 11111 18/18

# 2022-11-07 Marking (1 right, 0 wrong, * bug):
# 11100 12/18

from collections import deque

class Plane:
    def __init__(self, path, plane_i):
        self.path = path
        self.len_path = len(path)
        self.port_i = 0
        self.dist = 0
        self.can_have_cargo = False

        self.plane_i = plane_i # DEBUG

    def step(self):
        self.port_i += 1
        self.dist += 1
        self.port_i %= self.len_path

    def get_port(self):
        return self.path[self.port_i]

    def __repr__(self):
        return str(self.path) + "@" + str(self.port_i) + "dist" + str(self.dist)

dest_port = int(input())
num_planes = int(input())

paths = []

for i in range(num_planes):
    path = input().split()
    paths.append(list(map(int, path)))

planes = set() # Set as unordered

for i, path in enumerate(paths):
    planes.add(Plane(path, i))

planes_with_cargo = [] # Transfer from planes when get cargo

# Check start port for possible planes
for plane in planes.copy():
    if plane.get_port() == 1:
        # Start port
        planes_with_cargo.append(plane)
        planes.remove(plane)

# print(planes, planes_with_cargo)

at_dest = False
dist = 0

# print(planes, planes_with_cargo)

not_arrived = True
while(not_arrived): # Don't handle infinite loop = doesn't say what to print if no path
    dist += 1 # Before as (1) first port already checked and (2) don't increment before getting dist
    for plane in planes:
        plane.step()
    # print(dist, planes, planes_with_cargo)
    for plane_a in planes_with_cargo.copy():
        # print(plane_a.plane_i, plane_a.get_port())
        plane_a.step()
        if(plane_a.get_port() == dest_port):
            # print(dist, plane_a.plane_i, "!")
            # Arrived
            not_arrived = False
            break

        for plane_b in list(planes): # Copy so still mutable
            if(plane_b.get_port() == plane_a.get_port()):
                # print(dist, plane_a.plane_i, ">", plane_b.plane_i)
                # Can transfer - same port
                planes.remove(plane_b)
                planes_with_cargo.append(plane_b)
            # else: print(dist, plane_a.plane_i, plane_a.get_port(), "!", plane_b.plane_i, plane_b.get_port())

print(dist)