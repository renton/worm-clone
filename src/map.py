from tile import *

class Map():
    def __init__(self,size_x,size_y):
    
        self.tiles = []
        self.size_x = size_x
        self.size_y = size_y

        for i in range(self.size_x):
            self.tiles.append([])
            for j in range(self.size_y):
                self.tiles[i].append(Tile())

        self._make_edges_unwalkable()

    def _make_edges_unwalkable(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                if i == 0 or j == 0 or i == (self.size_x-1) or j == (self.size_y-1):
                    self.tiles[i][j].set_unwalkable()

    def get_neighbour_walkable_tiles(self,x,y):
        tiles = []
        dirs = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for dirn in dirs:
            if self.tiles[dirn[0]][dirn[1]].walkable == True:
                tiles.append(self.tiles[dirn[0]][dirn[1]])
        return tiles

    def get_number_walkable_neighbours(self,x,y):
        return len(self.get_neighbour_walkable_tiles(x,y))
