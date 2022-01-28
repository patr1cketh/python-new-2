import pygame

pygame.init()

display = pygame.display.set_mode([800, 600])

black = [0, 0, 0]
clock = pygame.time.Clock()

running = True

while running:
    display.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the user clicks on the "x" to close the window
            running = False
    
    pygame.display.update() # update graphics on screen
    clock.tick(45)
pygame.quit()
quit()
