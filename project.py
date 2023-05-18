import numpy as np
import random
import pygame
import sys


pygame.init()
brown = (100,40,0)
white = (210,150,75)
green = (0,255,0)
red = (255,0,0)

row_co = 6
column_co = 7
SQUARESIZE = 50
RADIUS = int(SQUARESIZE/2 - 10)

#Fonts
myfont = pygame.font.SysFont("monospace", 20)

# Create the Pygame screen
width = column_co * SQUARESIZE
height = (row_co+1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)

#Difficulity level
Dp1 = int(input("Enter player 1 Difficulity: "))
Dp2 = int(input("Enter player 2 Difficulity: "))



# Create the game board
def C_board():
	board = np.zeros((row_co,column_co))
	return board

# Functions
def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[row_co-1][col] == 0

def get_next_open_row(board, col):
	for r in range(row_co):
		if board[r][col] == 0:
			return r

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(column_co-3):
		for r in range(row_co):
			if (board[r][c] == piece and
			board[r][c+1] == piece and 
			board[r][c+2] == piece and 
			board[r][c+3] == piece):
				return True

	# Check vertical locations for win
	for c in range(column_co):
		for r in range(row_co-3):
			if (board[r][c] == piece and 
			    board[r+1][c] == piece and 
			    board[r+2][c] == piece and 
			    board[r+3][c] == piece):
				return True

	# Check positively sloped diaganols
	for c in range(column_co-3):
		for r in range(row_co-3):
			if( board[r][c] == piece and 
			    board[r+1][c+1] == piece and
			    board[r+2][c+2] == piece and
			    board[r+3][c+3] == piece):
				return True

	# Check negatively sloped diaganols
	for c in range(column_co-3):
		for r in range(3, row_co):
			if (board[r][c] == piece and 
			    board[r-1][c+1] == piece and
			    board[r-2][c+2] == piece and
			    board[r-3][c+3] == piece):
				return True

def draw_board(board):
	for c in range(column_co):
		for r in range(row_co):
			pygame.draw.rect(screen, brown, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, white, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(column_co):
		for r in range(row_co):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, green, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, red, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

def evaluate_window(window, piece):
    score = 0
    opp_piece = 1 if piece == 2 else 2
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4
    return score

def score_position(board, piece):
    score = 0
    # Score center column
    center_array = [int(i) for i in list(board[:, column_co//2])]
    center_count = center_array.count(piece)
    score += center_count * 3
    # Score horizontal
    for r in range(row_co):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(column_co-3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)
    # Score vertical
    for c in range(column_co):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(row_co-3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)
    # Score positive diagonal
    for r in range(row_co-3):
        for c in range(column_co-3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)
    # Score negative diagonal
    for r in range(row_co-3):
        for c in range(column_co-3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)
    return score

def get_valid_locations(board):
	valid_locations = []
	for col in range(column_co):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

def is_terminal_node(board):
    return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_locations(board)) == 0

def minmax(board, depth, alpha, beta, maximizing_player):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):
                return (None, 100000000000000)
            elif winning_move(board, 1):
                return (None, -100000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, 2))
    if maximizing_player:
        value = float('-inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, 2)
            new_score = minmax(temp_board, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else: # Minimizing player
        value = float('inf')
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, 1)
            new_score = minmax(temp_board, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def Board_Full():
    cnt = 0
    for i in range(column_co):
        if board[5][i] != 0:
            cnt = cnt + 1
    if cnt == 7:
        return True
    else:
        return False


board = C_board()
game_over = False
turn = 0

draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        pygame.draw.rect(screen, white, (0, 0, width, SQUARESIZE))
        pygame.display.update()

        
        #Insert AI LOGIC here
        pygame.time.wait(1000)
        
        if turn == 0:
            col, _ = minmax(board, Dp1, float('-inf'), float('inf'), True)
        else:
            col, _ = minmax(board, Dp2, float('-inf'), float('inf'), False)


        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn + 1)



            if winning_move(board, turn + 1):
                if turn == 0:
                    label = myfont.render("Player 1 wins!", 1, green)
                else:
                    label = myfont.render("Player 2 wins!", 1, red)
                screen.blit(label, (40, 10))
                game_over = True
            if Board_Full():
                label = myfont.render("Draw", 1, white)
                game_over = True
            

            turn += 1
            turn %= 2

            draw_board(board)

            if game_over:
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()