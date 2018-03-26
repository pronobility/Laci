# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:08:21 2018

@author: user357
"""

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 415]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
background_image = pygame.image.load("kep.png").convert()

player_image = pygame.image.load("player.png").convert()

click_sound = pygame.mixer.Sound("laser5.ogg")

# Hide the mouse cursor

pygame.mouse.set_visible(0)
player_image.set_colorkey(BLACK)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
 
    # --- Game Logic
    
    # Move the object according to the speed vector.
    # Fogjuk a jelenlegi egér pozíciót. Ez két számnak a listáját adja vissza.
 
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Képet a képernyőre másol
    screen.blit(background_image, [0, 0])
    screen.blit(player_image, [x, y])
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    
    
    
    
 
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()