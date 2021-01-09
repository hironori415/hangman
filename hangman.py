# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:02:32 2021

@author: hiroh
"""
import random

def hangman(word):
    wrong=0
    stages=["",
            "_____    ",
            "|        ",
            "|    |   ",
            "|    o   ",
            "|   /|\  ",
            "|   / \  ",
            ]
    already=[]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to Hangman!")

    while wrong<len(stages)-1:
        print("\n")
        msg="Guess a character:"
        char=input(msg)
        def step():
            already.append(char)
            print("\n You have said ")
            print(already) 
            
        def check():
            if char in already:
                print("\n You already said the character!")
            else:
                step()
                print(" ".join(board))
                e=wrong+1
                print("\n".join(stages[0:e]))
            
        if char in rletters:
            print("\n HIT! ")
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
            check()
        
        else:
            print("\n FALSE! ")
            wrong+=1
            check()
        
        if "_" not in board:
            print("You win!!")
            print(" ".join(board))
            win=True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The right word is {}.".format(word))
        
ans=["certain","landmark","particular","medcine"]

hangman(random.choice(ans))