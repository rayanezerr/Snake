from pyparsing import C
from SnakeClass import *
from ClassPomme import *
from bouton import *

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Snake')

#images
TitleScreen = pg.image.load("images\TitleScreen.png").convert()
TitleScreen2 = pg.image.load("images\TitleScreen2.png").convert()
background = pg.image.load("images\\background.png").convert_alpha()
startimg = pg.image.load("images\\play.png").convert_alpha()
exitimg = pg.image.load('images\\exit.png').convert_alpha()
easyimg = pg.image.load('images\\easy.png').convert_alpha()
normalimg = pg.image.load('images\\normal.png').convert_alpha()
hardimg = pg.image.load('images\\hard.png').convert_alpha()
#boutons
font = pg.font.Font("I-pixel-u.ttf", 40)

startbtn = Bouton(249, 100, startimg,1.5)
exitbtn = Bouton(250, 500, exitimg, 1.5)
easybtn = Bouton(50, 300, easyimg)
normalbtn = Bouton(300, 300, normalimg)
hardbtn = Bouton(550, 300, hardimg)
def main():
    FPS = 15
    clock = pg.time.Clock()
    snake = Snake()
    pomme = Pomme()
    pomme.pos_random()
    running = True
    ts = True
    while ts:
        screen.blit(TitleScreen, (0,0))
        pg.display.flip()
        time.sleep(0.5)
        screen.blit(TitleScreen2, (0,0))
        pg.display.flip()
        time.sleep(0.5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                ts = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    ts = False
                    ps = True
        clock.tick(10)

    while ps:
        screen.blit(background, (0,0))
        if startbtn.dessin(screen):
            ps = False
        if exitbtn.dessin(screen):
            pg.quit()
            sys.exit()
        if easybtn.dessin(screen):
            snake.change_size(40)
            pomme.change_size(40)
            FPS = 8
        if normalbtn.dessin(screen):
            snake.change_size(40)
            pomme.change_size(40)
            FPS = 13
        if hardbtn.dessin(screen):
            snake.change_size(20)
            pomme.change_size(20)
            FPS = 25

        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ps = False
                sys.exit()
        clock.tick(10)

    while running:
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
        

            
        snake.update()

        if snake.get_tete() == pomme.position:
            snake.taille +=1
            pomme.pos_random()

        screen.blit(background, (0,0))
        text = f'SCORE: {snake.taille-1}'
        text_render = font.render(text, True, (0,0,0))
        text_rect = text_render.get_rect()
        text_rect.center = (682, 25)
        snake.dessin(screen)
        pomme.dessin(screen)
        screen.blit(text_render, text_rect)
        pg.display.update()
        clock.tick(FPS)

    pg.quit()

main()