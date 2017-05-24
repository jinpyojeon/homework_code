#!/usr/bin/python
import numpy as np

# Problem 11.2

# Refer to: http://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/

def isSafe(board, row, col):
    for i in range(len(board[row])):
        if board[row][i]:
            return False

    for i in range(len(board)):
        if board[i][i]:
            return False

        if board[i][len(board)-1-i]:
            return False

    return True

def solveNQueen(board, col):
    if col >= len(board):
        return True 
    
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQueen(board, col+1):
                return True

            board[i][col] = 0
    
    return False

def printBoard(board):
    for row in board:
        for col in row:
            print col,
        print 

def main():
    board = [[0, 0, 0, 0], 
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    
    if (solveNQueen(board, 0)):
        print "There is solution"
        printBoard(board)
    else:
        print "There is no solution"
        printBoard(board)



# Problem 11.3

class Polynomial:
    
    # Absolute simplest implementation I can think of 
    def __init__(self, coefficients):
        self.coefficients = coefficients

# Assuming length of m = 2n-1 polynomial with same length
#def Karatsubas(poly1, poly2):
#    n = (len(np.roots(poly1)) + 1)/2  # (m+1)/2
#    a = 
    
main()
