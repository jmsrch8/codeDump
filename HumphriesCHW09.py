#! /bin/python3
#name:		HumphriesCHW09
#programmer:	Cullen Humphries
#date:		monday, july 2, 2016
#abstract	This program will play rock, paper, scissors
#===========================================================================================#

import Pets

def main():

	pets = make_list()
	print('\nHere are the pets:\n')
	display_list(pets)


def make_list():
	pet_list = []
	print('\nPlease enter the data for the \'3\' pets:	')
	flag = 1
	for count in range(1,4):
		print('\nPet: ', flag)
		flag += 1
		pet_name = input('Enter the pet\'s name:   ')
		pet_type = input('Enter the pet\'s type:   ')
		pet_age = input('Enter the pet\'s age:    ')

		pet = Pets.PetData(pet_name, pet_type, pet_age)
		pet_list.append(pet)
	return pet_list

def display_list(pets_list):
	flag = 1
	for pet in pets_list:
		print('For pet',flag)
		print('The pet\'s Name is:  ',pet.get_pet_name())
		print('The pet\'s Type is:  ',pet.get_pet_type())
		print('The pet\'s age is:   ',pet.get_pet_age())
		print('\n')
		flag += 1
	
main()
input('Press \'ENTER\' to exit')
