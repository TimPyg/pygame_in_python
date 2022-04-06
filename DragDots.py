import pygame 
pygame.init()
sc = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and Drag to Draw")

keep_going = True
YELLOW= (255,255,0)
radius_red = 15
mousedown = False
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
   #     spot = event.pos
        print(spot)
        pygame.draw.circle(sc,YELLOW,spot,radius_red)
    pygame.display.update()
pygame.quit()

