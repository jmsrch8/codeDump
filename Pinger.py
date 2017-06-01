#! /bin/python3
#Name pinger App
#Maker Cullen Humphries
#date: wednesday, may 31, 2017
#Abstract: ping a list of hostnames or ip addresses.
################################################################

import subprocess

def main():
	with open('in.txt', 'r') as _file:
		rec = 0
		while rec != '':
			rec = _file.readline()
			rec = rec.rstrip('\n')
			state = Reach.checkAlive(rec)
			Write.fileOut(state)
		_file.close()
		print('\a', end='')
		input('\nPress \'ENTER\' to Exit')





class Reach:
        def checkAlive(host):
                state = "No"
                if (host != "NO"):
                        p = subprocess.call('ping ' + host)
                        if ( p == 0):
                                state = "Yes"
                
                return state

class Write:

	def fileOut(state):
		with open('pinger_out.txt', 'a') as _file:
			      _file.write(state + '\n')
			      _file.close()
			      print(".", end='')

main()
