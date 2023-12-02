from SnakeClass import *


class Pomme():

    def __init__(self):
        self.GRID_SIZE = 40
        self.position = (0, 0)
        self.temps = 10
        self.couleur = RED

    def change_size(self, size):
        self.GRID_SIZE = size

    def pos_random(self):
        pos_x = random.randint(0, SCREEN_WIDTH//self.GRID_SIZE-1)
        pos_y = random.randint(0, SCREEN_HEIGHT//self.GRID_SIZE-1)
        self.position = (pos_x*self.GRID_SIZE, pos_y*self.GRID_SIZE)
    
    def dessin(self, screen):
        pg.draw.rect(screen, self.couleur, (self.position[0], self.position[1], self.GRID_SIZE,self.GRID_SIZE))