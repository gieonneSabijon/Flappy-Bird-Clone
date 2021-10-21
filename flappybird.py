from os import truncate
import pygame, random
from entities import Player, Pipes

WINDOW = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Flappy Bird")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
points_text = myfont.render('', False, (0, 0, 0))
menu_text = myfont.render('', False, (0, 0, 0))

def main():
    setup()
    run = True  
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update()
        draw()

    pygame.quit()

def setup():
    global points
    global grass_x

    global pipez
    pipez = [Pipes(910,0),Pipes(1210,0),Pipes(1510,0)]

    global birdPlayer
    birdPlayer = Player(5,200)

    grass_x = 0
    points = 0

    for pipe in pipez:
        pipe.set_y(random.randint(50 , 200))

def draw():
    global grass_x
    global menu_text

    grass_image = pygame.image.load('grass.png')
    background_image = pygame.image.load('background.png')
    bot_pipes_image = pygame.image.load('bottompipes.png')
    top_pipes_image = pygame.image.load('toppipes.png')
    flappy_sprite = pygame.image.load('flappybird.png')

    WINDOW.blit(background_image, (0,0))
    WINDOW.blit(grass_image, (grass_x,458))
    WINDOW.blit(flappy_sprite, (50, birdPlayer.get_y()))
    

    for pipe in range(len(pipez)):
        WINDOW.blit(top_pipes_image,(pipez[pipe].get_x(), pipez[pipe].get_y() - 500))
        WINDOW.blit(bot_pipes_image,(pipez[pipe].get_x(), pipez[pipe].get_y() + 150))

    if birdPlayer.get_idle():
        menu_text = myfont.render("Press Space or W to Play", False, (0, 0, 0))
        WINDOW.blit(menu_text,(250,220))
    WINDOW.blit(points_text,(0,0))

    if not birdPlayer.get_alive():
        WINDOW.blit(flappy_sprite, (50, birdPlayer.get_y()))

        menu_text = myfont.render("Game Over", False, (0, 0, 0))
        WINDOW.blit(menu_text,(350,210))
         
        menu_text = myfont.render("Press Enter to Play Again", False, (0, 0, 0))
        WINDOW.blit(menu_text,(250,250))

    else:
        grass_x -= 1
        if grass_x < - 500:
            grass_x = 0 
    
    pygame.display.update()

def update():
    pipes()
    player()
    collision()
    point_counter()

def player():

    birdPlayer.set_rect(pygame.Rect(50, birdPlayer.get_y(), 50, 40))
    key_pressed = pygame.key.get_pressed()
    if birdPlayer.get_alive():
        if not birdPlayer.get_jump():
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_SPACE]:
                birdPlayer.set_vel(-13)
                birdPlayer.set_jump(True)
        if birdPlayer.get_vel() == 0:
            birdPlayer.set_jump(False)

        if birdPlayer.get_y() < 0:
            birdPlayer.set_y(0)

        if birdPlayer.get_y() > 500:
            birdPlayer.set_alive(False)
    else:
        if key_pressed[pygame.K_RETURN]:
            setup()

    if birdPlayer.get_idle():
        birdPlayer.set_x(0)
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_SPACE]:
            birdPlayer.set_idle(False)

    else:
        birdPlayer.set_x(5)
        birdPlayer.set_vel(birdPlayer.get_vel() + 1)
    birdPlayer.set_y(birdPlayer.get_y() + birdPlayer.get_vel()) 
        
def pipes():
    if birdPlayer.get_alive():
        for pipe in range(len(pipez)):
            pipez[pipe].set_x(pipez[pipe].get_x() - birdPlayer.get_x())

            if pipez[pipe].get_x() <= -75:
                pipez[pipe].set_x(900)
                pipez[pipe].set_y(random.randint(50 , 200)) 

            pipez[pipe].set_top_rect(pygame.Rect(pipez[pipe].get_x(), 0, 75, pipez[pipe].get_y()))
            pipez[pipe].set_bot_rect(pygame.Rect(pipez[pipe].get_x(), pipez[pipe].get_y() + 150, 75, 500))

def collision():
    if birdPlayer.get_alive():
        for pipe in range(len(pipez)):
            if birdPlayer.get_rect().colliderect(pipez[pipe].get_top_rect()) or birdPlayer.get_rect().colliderect(pipez[pipe].get_bot_rect()):
                birdPlayer.set_vel(-10)
                birdPlayer.set_alive(False)

def point_counter():
    global points_text
    global points
    points_text = myfont.render(str(points), False, (0, 0, 0))

    for pipe in pipez:
        if pipe.get_x() == 50 and birdPlayer.get_alive():
            points += 1

if __name__ == "__main__":
    main()
