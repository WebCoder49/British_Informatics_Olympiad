# Alpha Complex

class Spy:
    def __init__(self, adj_list:dict, start):
        # Convert adjacency list and add odd/even markers
        self.rooms = self.save_adj_list(adj_list)
        self.loc = start

    def save_adj_list(self, adj_list:dict):
        # Add odd/even markers to adj. list
        for room in adj_list:
            exits = adj_list[room]
            for i in range(len(exits)):
                exits[i] = [False, exits[i]] # False for even, True for odd marker, then exit data

            adj_list[room] = [False, exits] # False for even, True for odd marker, then room data

        return adj_list

    def n_moves(self, num_moves):
        # Get location
        loc = self.loc
        # Move
        for i in range(num_moves):
            # Toggle odd/even for room
            self.rooms[loc][0] = not self.rooms[loc][0]
            odd_visits = self.rooms[loc][0]
            # Choose exit and exit room
            exits = self.rooms[loc][1] # Adjacent exits in alphabetical order
            if(odd_visits):
                # Odd no. of visits
                chosen_exit = 0 # First letter alphabetically
            else:
                # Even no. of visits
                len_exits = len(exits)
                for i in range(len_exits):
                    exit = exits[i]
                    if(exit[0] == True):
                        # Odd number of exits -> choose one after or this if none after
                        chosen_exit = i+1
                        if(chosen_exit >= len_exits):
                            # Range error as overflow past end of exits (none after) - choose this
                            chosen_exit = i
                        break
            # Toggle odd/even for exit
            exits[chosen_exit][0] = not exits[chosen_exit][0]
            # Update location
            loc = exits[chosen_exit][1]
        # Set location
        self.loc = loc
        return loc

def append_sorted(arr:list, item_to_app):
    for i in range(len(arr)):
        item = arr[i]
        if(item >= item_to_app):
            # Have reached place to put i - all before were too small
            arr.insert(i, item_to_app)
            break
    else:
        # All too small - place at end
        arr.append(item_to_app)
    return arr

def decode_plan(plan:str):
    # Create adj_list as result
    result = {
    }

    # Get number of rooms so rooms can be chosen
    num_rooms = len(plan) + 2
    available_rooms = [] # Cannot choose same to connect twice - in index from 0 to num_rooms; ordered

    a_ord = ord("A")
    for i in range(num_rooms):
        char = chr(a_ord + i)
        # Check if in plan in main loop as what is in plan will change
        available_rooms.append(char)
        result[char] = []


    for plan_i in range(len(plan)):
        room_a = plan[plan_i]
        for i in range(len(available_rooms)):
            room = available_rooms[i]
            if(not room in plan[plan_i:]): # Remaining plan
                # Is not in plan so can be used; first alphabetically
                available_rooms.pop(i) # as chosen, remove from not chosen
                room_b = room
                break
        # Join rooms a and b
        result[room_a] = append_sorted(result[room_a], room_b)  # 1 way; alphabetical order
        result[room_b] = append_sorted(result[room_b], room_a)  # other way
    # Join 2 remaining rooms
    room_a = available_rooms[0]
    room_b = available_rooms[1]
    result[room_a] = append_sorted(result[room_a], room_b)  # 1 way; alphabetical order
    result[room_b] = append_sorted(result[room_b], room_a)  # other way

    return result

# Take inputs
plan, p, q = input().split()
p = int(p)
q = int(q)

adj = decode_plan("EAED")

# Output decoded plan
print("\n".join(
    map("".join, adj.values()) # Turn each adj.list into ""-sep string
))

spy = Spy(adj, "A") # Always start at A

# Output pos at p and q, p < q
pos_at_p = spy.n_moves(p)
pos_at_q = spy.n_moves(q-p) # More to reach q

print("".join((pos_at_p, pos_at_q)))