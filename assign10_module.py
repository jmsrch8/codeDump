#! /bin/python3
#name:		class assign10
#programmer:	Cullen Humphries
#date:		firday, august 5, 2016
#abstract	addrec adds records to file and disrec displays records in groups of 10
#=====================================================================#

#defining the add record function
def addrec():
	flag = 1
	while flag == 1:
		_file = open('records.list', 'a')
		in_file = input('add to file:	')
		_file.write(in_file + '\n')
		_file.close()
		try:		
			choice = input('would you like to keep adding records?(y or n):		')
		except:
			print('error')
			raise SystemExit
		if choice.lower == 'y' or choice.lower() == 'yes':
			print()
		elif choice.lower() == 'n' or choice.lower() == 'no':
			print('\nexiting...\n')
			flag = 2
		else:
			print('please enter y(yes) or n(no)\n')




#defining the display records function
def disrec():
	_file = open('records.list', 'r')
	rec = _file.readline()
	rec = rec.rstrip('\n')
	while rec != '':		
		flag2 = 10
		while flag2 != 0:
			print(rec)
			rec = _file.readline()
			rec = rec.rstrip('\n')
			flag2 -= 1
		if rec != '':
			input('\npress \'ENTER\' to see the next 10...	\n\n')
		else:
			print('\n')
	_file.close()	

		
			















