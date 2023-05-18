from Options import *
import numpy as np


# Create the game board
def C_board():
	board = np.zeros((row_co,column_co))
	return board

def draw_board(board):
	for c in range(column_co):
		for r in range(row_co):
			pygame.draw.rect(screen, blue, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, gray, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(column_co):
		for r in range(row_co):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, gold, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, red, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()
    