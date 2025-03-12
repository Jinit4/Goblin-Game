import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption ("Goblin Game")
screen_width = 500
       
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

class player (object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))

def redraw_game_window():
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()

man = player (300, 410, 64, 64)
run = True #With this loop we will display the window that we have created above.
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel: 
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right=False
        man.walkCount = 0

    if not (man.is_jump):
        if keys [pygame.K_SPACE]:
            man.is_jump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2)*0.5* neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10 
    redraw_game_window()
pygame.quit()