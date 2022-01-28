import pygame

pygame.init()

DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]
display = pygame.display.set_mode(DISPLAY_SIZE)

black = [0, 0, 0]

running = True

while running:
    display.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the user clicks on the "x" to close the window
            running = False
    
    pygame.display.update() # update graphics on screen
pygame.quit()
quit()
