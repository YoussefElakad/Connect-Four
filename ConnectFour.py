from ConnectFourAILogic import *
from ConnectFourGUI import*
import sys


board = C_board()
game_over = False
turn = 0


#Difficulity()
Dp1 = int(input("enter player 1 Difficulity: "))
Dp2 = int(input ("enter player 2 Difficulity: "))


draw_board(board)
pygame.display.update()


# Main Game LOOP
while not game_over:
    for event in pygame.event.get():
        pygame.draw.rect(screen, gray, (0, 0, width, SQUARESIZE))
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
                    label = myfont.render("Player 1 wins!", 1, gold)
                else:
                    label = myfont.render("Player 2 wins!", 1, red)
                screen.blit(label, (40, 10))
                game_over = True
            if Board_Full(board):
                label = myfont.render("Draw", 1, white)
                game_over = True
            

            turn += 1
            turn %= 2

            draw_board(board)

            if game_over:
                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()