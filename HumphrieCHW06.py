#! /bin/python3
#name:		HumphriesCHW06
#programmer:	Cullen Humphries
#date:		monday, june 22, 2016
#abstract	This program will play rock, paper, scissors
#===========================================================================================#

import time
import random


def main():
	name = input('Please Enter your name:   ')
	win, loss, tie = game_loop(name)
	print('Okay,',name.'you Won',won,'matches. You Lost',loss,'matches. And you Tied',tie,'matches\n')
	exit()
#========================================#

def game_loop(name):
	test1 = 0
	
	print('Hello,',name,'your choices are:')
	print('''
1) Rock
2) paper
3) Scissors
4) exit
''')
	while test1 == 0:
		choice = input('Please make a choice:   ')
		if choice == 1 or choice == 2 or choice == 3 or choice == 4
			test = 1
		else
			print('error: Please choice a number from the menu:')
			print('''
1) Rock
2) paper
3) Scissors
4) exit
''')





































#def select_choice():
#    ...
#    return (i, card)

#my_i, my_card = select_choice()
