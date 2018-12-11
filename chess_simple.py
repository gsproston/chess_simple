import pygame, sys, time
from pygame.locals import *

import window
import board as b

# global constants
FPS = 30

# global variables
shutdown = False
    
def listenOnEvents():
  global shutdown, paused
  for event in pygame.event.get(): #runs when an event occurs
    if event.type == QUIT: #quit called
      shutdown = True #end loop
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