# Add spaceship image and move with arrow keys

import pygame 
import random 
import sys 

## funciton declaration part 
def paintEntity(entity, x, y) :
       monitor.blit(entity, (int(x), int(y)))
       
def playGame():
    global monitor 
    
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    
    # Declare a variable to store the amount of movement when the initial position of the ship is pressed on the keyboard.
    shipX = swidth / 2  # spaceship location 
    shipY = sheight * 0.8
    dx, dy = 0, 0       # The amount of movement of the spaceship when the keyboard is pressed
    
    # infinite loop
    while True:
        (pygame.time.Clock().tick(50))  # slow down the game(1 to 100 is appropriate)
        monitor.fill((r, g, b))  # paint the background
        
        # Check if an event is coming from the keyboard or mouse
        for e in pygame.event.get():
            if e.type in[pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
            # Press the arrow key to move the spaceship (keep it pressed to move).
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT : dx = +5
                elif e.key == pygame.K_UP : dy = -5
                elif e.key == pygame.K_DOWN : dy = +5
        
        # When you release the arrow keys, the spaceship stops.
            if e.type in [pygame.KEYUP] :
                 if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx, dy = 0, 0

        # Make the spaceship move only within the screen.
        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
            and (sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]) :  # only to the center of the screen
            shipX += dx
            shipY += dy
        paintEntity(ship, shipX, shipY)   # display the spaceship on the screen

        
        # Update the screen.
        pygame.display.update()
        
## global var declaration part
r, g, b = [0]*3     # game background color
swidth, sheight = 500, 700      # background size
monitor = None  # game display 
ship, shipSize = None, 0     # Spaceship object and size variables

# main code part
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('Defeat the space monster')

# Prepare the spaceship image and find its size.
ship = pygame.image.load('ship02.png')
shipSize = ship.get_rect().size

playGame()