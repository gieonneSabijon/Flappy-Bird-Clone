import pygame, random

WINDOW = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Flappy Bird")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
points_text = myfont.render('', False, (0, 0, 0))
menu_text = myfont.render('', False, (0, 0, 0))
points = 0
bird_x = 5
bird_y = 0

pipe_x = [300, 600, 900]
pipe_y = [100, 200, 300]

vel = 5
jump = False

alive = True

bird = pygame.Rect(0, 0, 0, 0)
top_pipes = []
bot_pipes = []

for i in range(4):
    top_pipes.append(pygame.Rect(0,0,0,0))
    bot_pipes.append(pygame.Rect(0,0,0,0))

def main():
    clock = pygame.time.Clock()
    run = True  

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update()
        draw()

    pygame.quit()

def draw():
    global menu_text
    if alive:
        WINDOW.fill((99, 153, 214))
        pygame.draw.rect(WINDOW, (240, 234, 58), bird)
        for pipe in range(len(pipe_x)):
            pygame.draw.rect(WINDOW, (9, 145, 34), top_pipes[pipe])
            pygame.draw.rect(WINDOW, (9, 145, 34), bot_pipes[pipe])
        WINDOW.blit(points_text,(0,0))
    else:
        menu_text = myfont.render("Game Over", False, (0, 0, 0))
        WINDOW.fill((214, 21, 11))
        WINDOW.blit(menu_text,(350,225))
        WINDOW.blit(points_text,(0,0))

    pygame.display.update()

def update():

    pipes()
    keyboard_Input()
    collision()
    point_counter()

def keyboard_Input():
    global bird_y
    global bird_x
    global jump
    global vel
    global alive
    global bird

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_SPACE]:
        vel = -8
        jump = True
    else:
        jump = False

    vel += 1
    bird_y += vel
    

    if bird_y < 0:
        bird_y = 0

    if bird_y > 500:
        alive = False

    bird = pygame.Rect(50, bird_y, 50, 50)
        
def pipes():
    global pipe_y
    global pipe_x
    global bird_x
    global top_pipes

    for pipe in range(len(pipe_x)):
        pipe_x[pipe] -= bird_x

        if pipe_x[pipe] <= -75:
            pipe_x[pipe] = 900
            pipe_y[pipe] = random.randint(50 , 400)

        top_pipes[pipe] = pygame.Rect(pipe_x[pipe], 0, 75, pipe_y[pipe])
        bot_pipes[pipe] = pygame.Rect(pipe_x[pipe], pipe_y[pipe] + 150, 75, 500)

def collision():


    global top_pipes
    global bot_pipes
    global bird
    global alive

    for pipe in range(len(pipe_x)):
        if bird.colliderect(top_pipes[pipe]) or bird.colliderect(bot_pipes[pipe]):
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
            print(points)


if __name__ == "__main__":
    main()
