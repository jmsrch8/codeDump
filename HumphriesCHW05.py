#!/bin/python3
#name:		HumphriesCHW05
#programmer:	Cullen Humphries
#date:		monday, june 20, 2016
#abstract	This program will do calculations on a varing number of student test scores
#===========================================================================================#



import time





#===========================================================================================================#

#Define main()
def main():
#declare function variables
	student_count = 0
	should_cont = 'y'
	val = 1
	val2 = 0
#create while loop
	while val == 1:
		name = input('Please enter the student\'s name:  ')
		score_count = int(input('Please enter the number of scores:   '))
#error check
		while val2 == 0:
			val2 = valinput3(score_count)
			if val2 == 0:
				score_count = int(input('Please enter a number greater than 0:   '))
		loop(score_count, name)
		student_count += 1
		should_cont = input('Would you like to continue? (y or n):   ')
#error check
		val = valinput2(should_cont)
		
		
	print('You have Calculated the scores for',student_count,'student(s)\n')
	exit()

#==========================================================================================================#

#define loop()

def loop(scct, name):
#ddeclare function variables
	score = 1
	val = 1
	totscore = 0
	loopcount = scct
	avscore = 0
	highscore = 0
	lowscore = 100
#basic while loop 
	while scct > int('0'):
			score = float(input('please enter a score:   '))
			val = valinput1(score)
			if val == 0:
				while val == 0:
					print('Please enter a score between 0 and 30.')
					score = float(input('please enter a correct score:   '))
#error check
					val = valinput1(score)
					
#define total High and low scores			
			totscore += score
			if score > highscore:
				highscore = score
			if score < lowscore:
				lowscore = score
#count sentinal down
			scct -= 1



	avscore = totscore / loopcount
#call display
	display1(totscore, loopcount, avscore, highscore, lowscore, name)

#=========================================================================================================#


#define first error check
def valinput1(inpt):
	if inpt >= 0 and inpt <= 30:
		return 1
	else:
		return 0
	
#=========================================================================================================#
#define second error check
def valinput2(should_cont):
	val = 2
	while val == 2:
		if should_cont == 'y' or should_cont == 'Y' or should_cont == 'yes' or should_cont == 'Yes':
			ret = 1
			val = 1
		elif should_cont == 'n' or should_cont == 'N' or should_cont == 'no' or should_cont == 'No':
			ret = 0
			val = 1
		else:
			print('error!')
			should_cont = input('please enter y or n:   ')
			val = 2
	if ret == 1:
		return 1
	elif ret == 0:
		return 0
	
#=========================================================================================================#

#define third error check
def valinput3(scnt):
	if scnt	> 0:
		return 1
	else:
		return 0

		

#=========================================================================================================#

#define display
def display1(tsc, lct, asc, hsc, lsc, name):
	print('Of',lct,'Scores,',name,'has a Total of:', tsc)
	print('The Average Score is:',format(asc, '.2f'))
	print('The High Score is:',hsc,'\nThe Low Score is:',lsc )


#============================================================================================================#

#define exit
def exit():
	input('Press \'ENTER\' to Exit.....')

#=============================================================================================================#

#call main()
main()


#end








