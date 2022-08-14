import sys
import pygame
import numpy as np

from constants import *


pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill( BG_COLOR )


class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squares # [SQUARES]
        self.marked_sqrs = 0

    def final_state(self):
        '''
        @return 0 if there is no win yet
        @return 1 if player 1 wins
        @return 2 if player 2 wins
        '''

        # Vertical Wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        # Horizontal Wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][0] == self.squares[row][0] != 0:
                return self.squares[row][0]

        # Desc Description
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                return self.squares[1][1]

        # Asc Description
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                return self.squares[1][1]
        
        return 0



    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_square(self, row, col):
        return self.squares[row][col] == 0

    def det_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqrs(row, col):
                    empty_sqrs.append(row, col)

        return empty_sqrs

    def is_full(self):
        return self.marked_sqrs == 9

    def is_empty(self):
        return self.marked_sqrs == 0

class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1 # 1-crosses and 2-circles
        self.show_lines()

    def show_lines(self):
        #Vertical 
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQSIZE, 0), (WIDTH-SQSIZE, HEIGHT), LINE_WIDTH)

        #Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT-SQSIZE), (WIDTH, HEIGHT-SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            # Draw Cross
            # Desc Line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            # Desc Line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

        elif self.player == 2:
            # Draw Circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

def main():

    # object
    game = Game()
    board = game.board


    # MainLoop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_square(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
                    
                
        pygame.display.update() 
main()