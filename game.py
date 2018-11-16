# 1 include pygame
import pygame

# 2 Init pygame
# In order to use pygame we have to run the init method
pygame.init()

# 3 create a screen with a size
# the screen size must be a tuple
screen_size = (512,480)
# Actually tell pygame to set the screen up and store it
# so pygame can use it
pygame_screen = pygame.display.set_mode(screen_size)

# set the title of the window
pygame.display.set_caption('Goblin Runner')

# VARIABLES FOR OUR GAME
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')


# 4 create the game loop (while 1)
# create a boolean for weather the game should run or not
game_on = True
while game_on:

    # we are inside the main game loop
    # it will keep running as long as our bool is true
   
   # 5 add a quit event (requires sys)
   # pygame comes with an event loop (like js)
    

    for event in pygame.event.get():
       # print event
        if(event.type == pygame.QUIT):
            game_on = False   
    #    we need to give pygame a way out
    #    if we dont... python is going to freak out
    #    because its inside of an infinite loop
    #  
    # 6 screen.fill (pass bg_color)
    # we want to draw on the screen
    # we are going to use blit (block image transfer)
    # blit is a function and takes 2 arguments:
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(hero_image, [256,17])
    pygame_screen.blit(monster_image, [125,40])
    # 7 Flip the screen and start over
    pygame.display.flip()
    
    # Controls
    
    