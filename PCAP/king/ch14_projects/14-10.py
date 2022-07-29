# configure basic display 

import pygame 
import random 
import sys 

## funciton declaration part 
def playGame():
    global monitor 
    
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    
    # infinite loop
    while True:
        (pygame.time.Clock().tick(50))  # slow down the game(1 to 100 is appropriate)
        monitor.fill((r, g, b))  # paint the background
        
        # Check if an event is coming from the keyboard or mouse
        for e in pygame.event.get():
            if e.type in[pygame.QUIT]:
                pygame.quit()
                sys.exit()
            
        
        # update display 
        pygame.display.update()
        print('~', end = '')
        
## global var declaration part
r, g, b = [0]*3     # game background color
swidth, sheight = 500, 700      # background size
monitor = None  # game display 

# main code part
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('Defeat the space monster')


playGame()