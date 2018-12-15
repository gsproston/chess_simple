import pygame, sys, time
from pygame.locals import *

import window
import board as b

# global constants
FPS = 30

# global variables
shutdown = False

def processClick():
  x = pygame.mouse.get_pos()[0]
  y = pygame.mouse.get_pos()[1]
  # get the offsets
  screen = pygame.display.get_surface() 
  # get the offsets
  offsetw = (screen.get_width() - b.SQUARE_SIZE*8) / 2
  offseth = (screen.get_height() - b.SQUARE_SIZE*8) / 2
  # see if the click is within the board
  if (x > offsetw and x < screen.get_width() - offsetw and
    y > offseth and y < screen.get_height() - offseth):
    # convert to board co-ordinates
    x -= offsetw
    y -= offseth
    x /= b.SQUARE_SIZE
    y /= b.SQUARE_SIZE
    b.squareClicked(int(x), int(y))
    
def listenOnEvents():
  global shutdown, paused
  for event in pygame.event.get(): #runs when an event occurs
    if event.type == QUIT: #quit called
      shutdown = True #end loop
    elif event.type == MOUSEBUTTONDOWN: #mouse clicked
      processClick()
    elif event.type == KEYDOWN: #key has been pressed
      if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        shutdown = True #end loop  
    
if __name__ == "__main__":
  pygame.init()
  window.init()
  clock = pygame.time.Clock()
  
  b.initBoard()

  #main game loop
  while (not shutdown):
    listenOnEvents()
    clock.tick(FPS) #update x times a second, determines FPS

  #main loop ends, exit
  pygame.quit()