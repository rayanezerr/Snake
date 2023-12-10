from Constants import *


class Snake():

    def __init__(self):
        self.GRID_SIZE = 40    
        self.taille = 1
        self.position = [(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.couleur = GREEN
        
    def change_size(self, size):
        self.GRID_SIZE = size

    def get_head_pos(self):
        return self.position[0]
    
    def get_tail(self):
        return self.position[-1]

    def update(self):
        tete = self.get_head_pos()
        dir_x = self.direction[0]
        dir_y = self.direction[1]
        nvl_tete = ((tete[0]+dir_x*self.GRID_SIZE)%SCREEN_WIDTH, (tete[1] + dir_y*self.GRID_SIZE)%SCREEN_HEIGHT)
        if nvl_tete in self.position and len(self.position)>4:
            print('Game Over')
            return True
        else:
            self.position.insert(0, nvl_tete)
            if len(self.position) > self.taille:
                del self.position[-1]
    
    def dessin(self, screen):
        pg.draw.rect(screen, (0, 255, 75),(self.position[0][0], self.position[0][1], (self.GRID_SIZE), (self.GRID_SIZE)))
        for pos in self.position[1:]:
            pg.draw.rect(screen, self.couleur,(pos[0], pos[1], (self.GRID_SIZE), (self.GRID_SIZE)))