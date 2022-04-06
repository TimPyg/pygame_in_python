import pygame 
pygame.init()
sc = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drow")

keep_going = True
RED = (255,0,0)
radius_red = 15
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            print(spot)
            pygame.draw.circle(sc,RED,spot,radius_red)
    pygame.display.update()
pygame.quit()


# 245 - SmileExplosion.py  __init__
#          SmilePop.py 
