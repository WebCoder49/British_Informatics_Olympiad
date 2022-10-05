# Air Cargo
from collections import deque

class Plane:
    def __init__(self, path):
        self.path = path
        self.len_path = len(path)
        self.port_i = 0
        self.dist = 0
        self.can_have_cargo = False

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


planes = deque()
for i in range(num_planes):
    path = input().split()
    path = list(map(int, path)) # Map to ints
    planes.append(Plane(path))

planes_with_cargo = deque() # Transfer from planes when get cargo

for i in range(len(planes)):
    plane = planes.popleft()
    if(plane.get_port() == 1):
        # Start port
        planes_with_cargo.append(plane)
    else:
        # Keep in `planes`
        planes.append(plane)

# print(planes, planes_with_cargo)

at_dest = False
dist = 0

while(not at_dest): # Don't handle infinite loop = doesn't say what to print if no path
    plane_a = planes_with_cargo.popleft()
    plane_a.step()
    if(planes):
        # Exist planes w/o cargo - can transfer
        plane_b = planes.popleft()
        plane_b.step()
        # Try to transfer cargo to plane b
        if(plane_a.get_port() == plane_b.get_port()):
            # Can transfer
            planes_with_cargo.append(plane_b)
            if (plane_b.get_port() == dest_port):
                at_dest = True
                dist = plane_b.dist
                break
        else:
            planes.append(plane_b)
    if(plane_a.get_port() == dest_port):
        at_dest = True
        dist = plane_a.dist

    planes_with_cargo.append(plane_a)
    # print(planes, planes_with_cargo)

print(dist)