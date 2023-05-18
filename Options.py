import pygame

pygame.init()
brown = (100,40,0)
rust = (210,150,75)
green = (0,255,0)
red = (255,0,0)
black= (0, 0, 0, 255)
blue= (0, 0, 255, 255)
cyan= (0, 255, 255, 255)
gold= (255, 215, 0, 255)
gray= (190, 190, 190, 255)
orange= (255, 165, 0, 255)
purple= (160, 32, 240, 255)
violet= (238, 130, 238, 255)
yellow= (255, 255, 0, 255)
white= (255, 255, 255, 255)



row_co = 6
column_co = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 10)

#Fonts
myfont = pygame.font.SysFont("monospace", 50)

# Create the Pygame screen
width = column_co * SQUARESIZE
height = (row_co+1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)