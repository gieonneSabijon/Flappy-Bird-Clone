from os import truncate
import pygame, random

WINDOW = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Flappy Bird")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
points_text = myfont.render('', False, (0, 0, 0))
menu_text = myfont.render('', False, (0, 0, 0))
clock = pygame.time.Clock()

def main():
    setup()
    run = True  

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update()
        draw()

    pygame.quit()

def setup():
    global bird_y
    global pipe_x
    global pipe_y
    global alive
    global points
    global bird_x
    global jump
    global vel
    global bird 
    global top_pipes
    global bot_pipes
    global idle
    global grass_x

    idle = True
    grass_x = 0
    points = 0
    bird_x = 5
    bird_y = 200

    pipe_x = [910, 1210, 1510]
    pipe_y = [0, 0, 0]

    for pipe in range(len(pipe_y)):
        pipe_y[pipe] = random.randint(50 , 200)
    vel = 0
    jump = False

    alive = True

    bird = pygame.Rect(0, 0, 0, 0)
    top_pipes = []
    bot_pipes = []
    for i in range(len(pipe_x)):
        top_pipes.append(pygame.Rect(0,0,0,0))
        bot_pipes.append(pygame.Rect(0,0,0,0))

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
    WINDOW.blit(flappy_sprite, (50, bird_y))
    for pipe in range(len(pipe_x)):
        WINDOW.blit(top_pipes_image,(pipe_x[pipe], pipe_y[pipe] - 500))
        WINDOW.blit(bot_pipes_image,(pipe_x[pipe], pipe_y[pipe] + 150))
    WINDOW.blit(points_text,(0,0))
    if idle:
        menu_text = myfont.render("Press Space or W to Play", False, (0, 0, 0))
        WINDOW.blit(menu_text,(250,220))
    if not alive:
        WINDOW.blit(flappy_sprite, (50, bird_y))
        menu_text = myfont.render("Game Over", False, (0, 0, 0))
        WINDOW.blit(menu_text,(350,225))
        WINDOW.blit(points_text,(0,0))
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
    global bird_y
    global bird_x
    global jump
    global vel
    global alive
    global bird
    global idle
    bird = pygame.Rect(50, bird_y, 50, 40)

    key_pressed = pygame.key.get_pressed()
    if alive:
        if not jump:
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_SPACE]:
                vel = -13
                jump = True
        if vel == 0:
            jump = False
        

        if bird_y < 0:
            bird_y = 0

        if bird_y > 500:
            alive = False



    else:
        if key_pressed[pygame.K_RETURN]:
            setup()

    if idle:
        bird_x = 0
        if key_pressed[pygame.K_w] or key_pressed[pygame.K_SPACE]:
             idle = False

    else:
        bird_x = 5
        vel += 1
    bird_y += vel
        
def pipes():
    global pipe_y
    global pipe_x
    global bird_x
    global top_pipes

    if alive:
        for pipe in range(len(pipe_x)):
            pipe_x[pipe] -= bird_x

            if pipe_x[pipe] <= -75:
                pipe_x[pipe] = 900
                pipe_y[pipe] = random.randint(50 , 200)

            top_pipes[pipe] = pygame.Rect(pipe_x[pipe], 0, 75, pipe_y[pipe])
            bot_pipes[pipe] = pygame.Rect(pipe_x[pipe], pipe_y[pipe] + 150, 75, 500)

def collision():


    global top_pipes
    global bot_pipes
    global bird
    global alive
    global vel

    if alive:
        for pipe in range(len(pipe_x)):
            if bird.colliderect(top_pipes[pipe]) or bird.colliderect(bot_pipes[pipe]):
                vel = -10
                alive = False

def point_counter():
    global points_text
    global points
    global bird_x
    global pipe_x
    global alive
    points_text = myfont.render(str(points), False, (0, 0, 0))

    for pipe in pipe_x:
        if pipe == 50 and alive:
            points += 1


if __name__ == "__main__":
    main()