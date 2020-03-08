import pygame
pygame.init()


speed = [4, 3]
size = width, height = 400,400
clock = pygame.time.Clock()
fps = 60
logo = pygame.image.load("logo-red.png")
rect = logo.get_rect()

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if rect.left < 0 :
        speed[0] = -speed[0]
        logo = pygame.image.load("logo-red.png")
    
    if rect.right > width:
        speed[0] = -speed[0]
        logo = pygame.image.load("logo-pink.png")
    
    if rect.top < 0 :
        speed[1] = -speed[1]
        logo = pygame.image.load("logo-green.png")
    
    if rect.bottom > height:
        speed[1] = -speed[1]
        logo = pygame.image.load("logo-blue.png")
        
    rect.left+= speed[0]       
    rect.top += speed[1]    
    screen.fill((0,0,0))
    screen.blit(logo, rect)
    pygame.display.update()
    clock.tick(fps)
    