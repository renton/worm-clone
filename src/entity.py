from random import randint,shuffle

class Entity():

    MAX_TILE_LOOKAHEADS = 100

    def __init__(self,name,color):
        self.x = None
        self.y = None
        self.alive = True
        self.name = name
        self.color = color

    def place_on_map(self,map):
        while(1):
            x = randint(0,map.size_x-1)
            y = randint(0,map.size_y-1)
            if map.tiles[x][y].walkable == True:
                self.x = x
                self.y = y
                break

    def step(self,map):
        if self.alive == True:

            map.tiles[self.x][self.y].set_unwalkable()
            map.tiles[self.x][self.y].set_color(self.color)

            order = {
                0:lambda x,y:(x+1,y),
                1:lambda x,y:(x-1,y),
                2:lambda x,y:(x,y+1),
                3:lambda x,y:(x,y-1),
            }
            paths = {}
            scores = {}
            for direction in order:
                paths[direction] = {}
                scores[direction] = 0


            # some crappy ai
            for dirn_k,dirn_v in order.items():
                lookahead_count = 0
                tiles_to_check = [dirn_v(self.x,self.y)]

                while(len(tiles_to_check) > 0):
                    cur_tile = tiles_to_check.pop()

                    if map.tiles[cur_tile[0]][cur_tile[1]].walkable == True:

                        paths[dirn_k][str(cur_tile[0])+"|"+str(cur_tile[1])] = map.get_number_walkable_neighbours(cur_tile[0],cur_tile[1])

                        for dirn_k2,dirn_v2 in order.items():
                            check_x,check_y = dirn_v2(cur_tile[0],cur_tile[1])
                            if str(check_x)+"|"+str(check_y) not in paths[dirn_k] and lookahead_count <= Entity.MAX_TILE_LOOKAHEADS:
                                tiles_to_check.append((check_x,check_y))
                                lookahead_count +=1
                    else:
                        paths[dirn_k][str(cur_tile[0])+"|"+str(cur_tile[1])] = 0


            for k,v in paths.items():
                for node_k,node_v in v.items():
                    scores[k] += node_v

            highest_dir = 0
            for k,v in scores.items():
                if v > scores[highest_dir]:
                    highest_dir = k

            (new_x,new_y) = order[highest_dir](self.x,self.y)
            if map.tiles[new_x][new_y].walkable == True:
                self.x = new_x
                self.y = new_y

            if map.tiles[self.x][self.y].walkable == False:
                self.alive = False
