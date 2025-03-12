import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption ("Goblin Game")
screen_width = 500
       
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#Setting the width and the height of the character
x = 50
y = 400
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()

is_jump = False
jump_count = 10

left = False
right = False
walkCount = 0

def redraw_game_window():
    global walkCount

    win.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()

run = True #With this loop we will display the window that we have created above.
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 -vel - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right=False
        walkCount = 0

    if not (is_jump):
        if keys [pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2)*0.5* neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10 
    redraw_game_window()
pygame.quit()