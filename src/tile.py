from random import randint

class Tile():
    def __init__(self):
        if randint(0,20) == 0:
            self.set_unwalkable()
        else:
            self.set_walkable()

    def set_walkable(self):
        self.walkable = True
        self.set_color((40,40,40))

    def set_unwalkable(self):
        self.walkable = False
        self.set_color((0,0,0))

    def set_color(self,new_color):
        self.color = new_color
