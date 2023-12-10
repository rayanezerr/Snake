from SnakeClass import *
from AppleClass import *
from Button import *

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Snake')

#images
TitleScreen = pg.image.load("images/TitleScreen.png").convert()
TitleScreen2 = pg.image.load("images/TitleScreen2.png").convert()
background = pg.image.load("images/background.png").convert_alpha()
startimg = pg.image.load("images/play.png").convert_alpha()
exitimg = pg.image.load('images/exit.png').convert_alpha()
easyimg = pg.image.load('images/easy.png').convert_alpha()
normalimg = pg.image.load('images/normal.png').convert_alpha()
hardimg = pg.image.load('images/hard.png').convert_alpha()
font = pg.font.Font("I-pixel-u.ttf", 40)

#boutons
startbtn = Bouton(249, 100, startimg,1.5)
exitbtn = Bouton(250, 500, exitimg, 1.5)
easybtn = Bouton(50, 300, easyimg)
normalbtn = Bouton(300, 300, normalimg)
hardbtn = Bouton(550, 300, hardimg)
running = True
titlescreen = True

def main():
    global titlescreen, mainscreen, running
    FPS = 13
    clock = pg.time.Clock()
    GRID_SIZE = 40
    snake = Snake()
    pomme = Pomme(GRID_SIZE)
    
    while titlescreen:
        screen.blit(TitleScreen, (0,0))
        pg.display.update()
        time.sleep(0.5)
        screen.blit(TitleScreen2, (0,0))
        pg.display.flip()
        time.sleep(0.5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                titlescreen = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    titlescreen = False
                    mainscreen = True
        clock.tick(10)

    while mainscreen:
        screen.blit(background, (0,0))
        if startbtn.dessin(screen):
            mainscreen = False
            running = True
        if exitbtn.dessin(screen):
            pg.quit()
            sys.exit()
        if easybtn.dessin(screen):
            GRID_SIZE = 50
            snake.change_size(GRID_SIZE)
            pomme = Pomme(GRID_SIZE)
            FPS = 8
        if normalbtn.dessin(screen):
            GRID_SIZE = 40
            snake.change_size(GRID_SIZE)
            pomme = Pomme(GRID_SIZE)
            FPS = 13
        if hardbtn.dessin(screen):
            GRID_SIZE = 20
            snake.change_size(GRID_SIZE)
            pomme = Pomme(GRID_SIZE)
            FPS = 20
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                mainscreen = False
                sys.exit()
        clock.tick(60)

    while running:
        # timestart = time.time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pg.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pg.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pg.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT  

        if snake.get_head_pos() == pomme.position:
            pomme = Pomme(GRID_SIZE)
            snake.taille +=1
        if snake.update():
            titlescreen = False
            mainscreen = True
            main()
            
        screen.blit(background, (0,0))
        text = f'SCORE: {snake.taille-1}'
        text_render = font.render(text, True, (0,0,0))
        text_rect = text_render.get_rect()
        text_rect.center = (682, 25)
        snake.dessin(screen)
        pomme.dessin(screen)
        screen.blit(text_render, text_rect)
        pg.display.update()
        #timeend = time.time()
        clock.tick(FPS)

    pg.quit()

main()