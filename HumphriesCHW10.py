#! /bin/python3
#name:		HumphriesCHW10
#programmer:	Cullen Humphries
#date:		friday, august 5, 2016
#abstract	This program will add records to a file and display records using a module
#===========================================================#
import time
from assign10_module import *

# define main
def main():
#print menu
	print('''
	MENU
1. Add records to file
2. Display Records in file
3. search records in file
4. change records in file
5. remove recods in file
0. quit''')

#reading user choice
	flag = 1
	while flag == 1:
		try:
			choice = input('\nEnter number of menu choice:	')
		except:
			print('error')
			exit()
		if choice == '0':
			exit()
		elif choice == '1':
			addrec()
			exit()
		elif choice == '2':
			print('displaying the first 10 entrys in the file:')
			disrec()
			exit()
		elif choice == '3':
			input('searching for record...	...press enter to continue...')
			flag = 2
		elif choice == '4':
			input('changing record...	...press enter to continue...')
			flag = 2
		elif choice == '5':
			input('removing record...	...press enter to continue...')
			flag = 2
		else:
			print('\nplease choose 1, 2, 3, 4, 5, or 0')
	exit()


#creating simple exit function
def exit():
	input('\nPress \'ENTER\' to exit... ')
	raise SystemExit





main()

