# Tri-iso-grid
# 80m done
import copy


class BidirArray: # Bidirectional - 2 arrs; 1 r2l for neg; 1 l2r for pos (and 0)
    def __init__(self, default_val, def_needs_deepcopy):
        self.default_val = default_val
        self.def_needs_deepcopy = def_needs_deepcopy
        self.negative_arr = []
        self.positive_arr = []
    def get(self, i:int):
        if i < 0:
            neg_index = (-1)-i
            while len(self.negative_arr) <= neg_index:
                # Expand arr
                if (self.def_needs_deepcopy):
                    self.negative_arr.append(copy.deepcopy(self.default_val))
                else:
                    self.negative_arr.append(self.default_val)
            return self.negative_arr[neg_index]
        else:
            while len(self.positive_arr) <= i:
                # Expand arr
                if (self.def_needs_deepcopy):
                    self.positive_arr.append(copy.deepcopy(self.default_val))
                else:
                    self.positive_arr.append(self.default_val)
            return self.positive_arr[i]

    def set(self, i:int, val):
        if i < 0:
            neg_index = (-1)-i
            while len(self.negative_arr) <= neg_index:
                # Expand arr
                if (self.def_needs_deepcopy):
                    self.negative_arr.append(copy.deepcopy(self.default_val))
                else:
                    self.negative_arr.append(self.default_val)
            self.negative_arr[neg_index] = val
        else:
            while len(self.positive_arr) <= i:
                # Expand arr
                if(self.def_needs_deepcopy):
                    self.positive_arr.append(copy.deepcopy(self.default_val))
                else:
                    self.positive_arr.append(self.default_val)
            self.positive_arr[i] = val

    def __repr__(self):
        return str(self.negative_arr[::-1]) + "_" + str(self.positive_arr)
    def repr_multiline(self):
        return "\n".join(map(str, self.negative_arr[::-1])) + "\n---\n" + "\n".join(map(str, self.positive_arr))

class Grid:
    def __init__(self):
        self.grid = BidirArray(BidirArray(None, False), True) # 2D
        self.perimeter = [(-1,0,True),(1,0,False),(0,1,False)] # (x,y,is_left flag) of empty triangles

        self.grid.get(0).set(0, 0) # Set 0,0 to 0


    def is_downwards(self, x:int, y:int):
        """Is the triangle at (x,y) pointing down?"""
        return (x + y) % 2 == 1
    def is_filled(self, x:int, y:int):
        """Is the triangle at (x,y) filled?"""
        return self.grid.get(y).get(x) is not None

    # def next_perim_i(self):

    def fill(self, perim_i:int, player:int):
        """& return difference in length to perimeter"""
        coords = self.perimeter[perim_i]
        x, y, _ = coords

        new_edges = self.get_free_edges(x, y)

        self.grid.get(y).set(x, player)

        if(self.perimeter[perim_i-1][0] == x and self.perimeter[perim_i-1][1] == y):
            # Replace both
            self.perimeter[perim_i-1:perim_i+1] = new_edges
            return len(new_edges) - 2
        elif (self.perimeter[perim_i + 1][0] == x and self.perimeter[perim_i + 1][1] == y):
            # Replace both
            self.perimeter[perim_i:perim_i+2] = new_edges
            return len(new_edges) - 2
        else:
            self.perimeter[perim_i:perim_i+1] = new_edges
            return len(new_edges) - 1

    def get_free_edges(self, x:int, y:int):
        """Return the coordinates of adjacent edge triangles that are not filled in; clockwise from first edge; (x,y,is_left flag)"""
        if(self.is_downwards(x, y)):
            coords_adj = [(x,y-1,False),(x+1,y,False),(x-1,y,True)] # Up;Right;Left
        else:
            coords_adj = [(x+1,y,False),(x,y+1,False),(x-1,y,True)]  # Right;Down;Left

        # Find filled tri
        filled_i = 0
        for filled_i,coord in enumerate(coords_adj):
            if self.is_filled(coord[0], coord[1]):
                # Start here
                break

        # Process in order and append if free
        free_edges = []
        for i in range(filled_i+1,3):
            if not self.is_filled(coords_adj[i][0],coords_adj[i][1]):
                # Free
                free_edges.append(coords_adj[i])
        for i in range(0, filled_i):
            if not self.is_filled(coords_adj[i][0],coords_adj[i][1]):
                # Free
                free_edges.append(coords_adj[i])

        return free_edges

    def get_top_left(self):
        """Get furthest left perim i in top row"""
        min_y = None # Precedence
        min_x = None
        topleft_i = None
        for i, coords in enumerate(self.perimeter):
            x, y, is_left = coords
            if is_left and (min_y is None or y < min_y or (y == min_y and x < min_x)): # Only works for left edges
                # Best so far
                min_y = y
                min_x = y
                topleft_i = i

        return topleft_i


class Game:
    def __init__(self, num_players:int, traversals_per_move:list):
        self.traversals_per_move = traversals_per_move
        self.num_players = num_players
        self.perim_i = [0 for i in range(num_players)]
        self.grid = Grid()

    def move(self, player:int):
        # Fill starting pos
        perim_len_before = len(self.grid.perimeter)
        perim_added = self.grid.fill(self.perim_i[player], player+1)
        # Move
        self.perim_i[player] += self.traversals_per_move[player] + perim_added
        self.perim_i[player] %= perim_len_before
        print(player, self.perim_i[player])

        for each_player in range(self.num_players):
            if each_player != player:
                if(self.perim_i[each_player] > self.perim_i[player]):
                    self.perim_i[each_player] += perim_added
                elif(self.perim_i[each_player] == self.perim_i[player]):
                    # Move to left side of top-left perimeter space
                    self.perim_i[each_player] = self.grid.get_top_left()

        print(self.perim_i, self.grid.perimeter)



# num_players, num_moves = map(int, input().split())
# max_traversals_per_player = tuple(map(int, input().split()))
num_players = 2
num_moves = 5 # Total of all players
max_traversals_per_player = [16, 2]

game = Game(num_players, max_traversals_per_player)
game.move(0)
game.move(1)
game.move(0)
print(game.grid.grid.repr_multiline())