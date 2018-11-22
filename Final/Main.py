import AES256 
from AES256 import Encryptor
import os 
import os.path
from os import listdir
from os.path import isfile, join 
import time 

class Menu:

	def __init__(self,name):
		self.name = name

	def enc_file(self,file_name, password, del_original,where_to_save):
		encriptor = Encryptor('temp')
		key = encriptor.set_password(password)
		var = encriptor.encrypt_file(str(file_name),str(where_to_save))
		if del_original == 1: 
			encriptor.deleteFile(file_name)
		else:
			print("else")
			#indicar donde guardar el archivo 
		return var

	def enc_text(self,text,password):
		encriptor = Encryptor('temp')
		encriptor.set_password(password)
		enc_Text = encriptor.encrypt_text(text)
		return enc_Text

	def dec_file(self,file_name,password,where_to_save):
		encriptor = Encryptor('temp')
		encriptor.set_password(password)
		var = encriptor.decrypt_file(str(file_name),str(where_to_save))
		return var

	def dec_text(self,enc_text,password):
		encriptor = Encryptor('temp')
		encriptor.set_password(password)
		text = encriptor.decrypt_text(str(enc_text))
		return text
