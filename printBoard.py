#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:31:59 2019

@author: cadecorontzos
"""
def tictactoe():
    moves=[1,2,3,4,5,6,7,8,9]
    board=emptyBoard()
    drawBoard(board)
    while not isFull(board):
        move=int(input("Player X, please select a square: "))
        while not isLegal(moves,move): #A legal move must be made to continue.
            print("You can't go there. Choose a legal space.")
            print("Legal spaces are numbered from 1 to 9, left to right, and must be empty")
            move=int(input("Player X, please select a square: "))
        moves.remove(move)
        play(board,"X",move)
        drawBoard(board)
        if didWin(board,"X"):
            print("X wins!!")
            break
        move=int(input("Player O, please select a square: "))
        while not isLegal(moves,move):
            print("You can't go there, choose an empty, legal space please you idiot.")
            move=int(input("Player O, please select a square: "))
        moves.remove(move)
        play(board,"O",move)
        drawBoard(board)
        if didWin(board,"O"):
            print("O wins!!")
            break
    if not didWin(board,"O") and not didWin(board,"X"):#if it is a cat's game
        print("Cat's Game!")

#returns if the move the player gave is legal.
def isLegal(moves,move):
    return move in moves

#prints the given board array
def drawBoard(board):
    
    for r in range(2):
        
        print("|".join(board[r]))
        print("-+-+-")
    print("|".join(board[2]))

#changes the board based on the given move, assumes move is legal
def play(board, move, position):
    place=position-1
    if board[place//3][place%3]==" ":
        board[place//3][place%3]=move

#returns if the given player won. Checks rows, colomns, and diagonals.
def didWin(board,player):
    for r in range(2):
        if board[r][0]==player and (board[r][0]==board[r][1] and board[r][1]==board[r][2]):
            return True
        if board[0][r]==player and (board[0][r]==board[1][r] and board[1][r]==board[2][r]):
            return True
    if(board[0][0]==player and (board[0][0]==board[1][1] and board[1][1]==board[2][2])):
        return True
    if(board[0][2]==player and (board[0][2]==board[1][1] and board[1][1]==board[2][0])):
        return True
    return False

#returns if the board is full. A catgame is called if isFull returns true and neither player has won
def isFull(board):
    for r in range(2):
        for c in range(2):
            if board[r][c]!="X" or board[r][c]!="O":
                return False
    return True
            
#returns the empty board array.   
def emptyBoard():
   return [[" "," "," "],[" "," "," "],[" "," "," "]]

if __name__ == "__main__":
    tictactoe()
        
        
