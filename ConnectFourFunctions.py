from ConnectFourGUI import *


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

def Board_Full(board):
    cnt = 0
    for i in range(column_co):
        if board[5][i] != 0:
            cnt = cnt + 1
    if cnt == 7:
        return True
    else:
        return False
