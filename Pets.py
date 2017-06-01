#! /bin/python3
#name:		class pets
#programmer:	Cullen Humphries
#date:		monday, july 25, 2016
#abstract	This petdata class stores data about pets
#===========================================================================================#



class PetData:


	def __init__ (self, pet_name, pet_type, pet_age):
		self.__pet_name = pet_name
		self.__pet_type = pet_type
		self.__pet_age = pet_age

	def set_pet_name(self, pet_name):
		self.__pet_name = pet_name

	def set_pet_type(self, pet_type):
		self.__pet_type = pet_type

	def set_pet_age(self, pet_age):
		self.__pet_age = pet_age

	def get_pet_name(self):
		return self.__pet_name

	def get_pet_type(self):
		return self.__pet_type

	def get_pet_age(self):
		return self.__pet_age

