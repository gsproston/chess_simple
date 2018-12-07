import pygame, sys, time
from pygame.locals import *

import window

# global constants
FPS = 30
SQUARE_SIZE = 60

# global variables
Board = [[]]
shutdown = False

# draws the entire board
def drawBoard(): 
  screen = pygame.display.get_surface()    
  screen.fill((255,255,255))
  pygame.display.flip()
    
def listenOnEvents():
  global shutdown, paused
  for event in pygame.event.get(): #runs when an event occurs
    if event.type == QUIT: #quit called
      shutdown = True #end loop
    elif event.type == KEYDOWN: #key has been pressed
      if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        shutdown = True
    
if __name__ == "__main__":
  pygame.init()
  window.init()    
  clock = pygame.time.Clock()

  #main game loop
  while (not shutdown):    
    # init the board
    Board = [[None for x in range(8)] for y in range(8)]
		# draw the board for the first time
    drawBoard()
        
    # only keep drawing the board if the state changes
    while (not shutdown): 
      listenOnEvents()
      clock.tick(FPS) #update x times a second, determines FPS

  #main loop ends, exit
  pygame.quit()