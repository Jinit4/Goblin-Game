import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption ("First Game")
       

#Setting the width and the height of the character
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True #With this loop we will display the window that we have created above.
while run:
    pygame.time.delay(100) #This is in MilliSeconds. Just provide some delay it will be 0.1 Second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y+= vel
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width, height))
    pygame.display.update()

pygame.quit()