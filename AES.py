'''
	Elizabeth Rodríguez Fallas 
 	Referencia: the-javapocalypse/Python-File-Encryptor. (2018). GitHub. Retrieved 20 November 2018, from https://github.com/the-javapocalypse/Python-File-Encryptor/blob/master/script.py
'''
from Crypto.Cipher import AES
from Crypto import Random  
from Crypto.Random import get_random_bytes
import os 
import os.path
from os import listdir
from os.path import isfile, join 
import time 

class Encryptor: 
	def __init__(self, key):
		self.key = key 

	def base64(self, s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def deleteFile(self,file_name): #used after encryption or decryption 
		os.remove(file_name)

	def encrypt_text(self, message, key):
		key_size=256
		message = self.base64(message)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		msg = iv + cipher.encrypt(message)
		return msg

	def encrypt_file(self, file_name):
		with open(file_name, 'rb') as fo:
			text = fo.read()
		encripted = self.encrypt_text(text,self.key)
		new_name = file_name.split(".")
		if len(new_name) > 2:
			temporal = ""
			for x in range (len(new_name)-1):
				temporal = temporal + new_name[x] +"."
			temporal  = temporal[:-1]
			new_name = [temporal,new_name[len(new_name)-1]]


		with open(new_name[0] + ".cfr." + new_name[1], 'wb') as fo:
			fo.write(encripted)
		

	def decrypt_text(self,cipheredText, key):
		iv = cipheredText[:AES.block_size]
		cipher = AES.new(key,AES.MODE_CBC,iv)
		text = cipher.decrypt(cipheredText[AES.block_size:])
		res = text.rstrip(b"\0")
		return res 

	def decrypt_file(self,file_name):
		with open(file_name,'rb') as fo:
			cipheredText = fo.read()
		decripted = self.decrypt_text(cipheredText,self.key)
		new_name = file_name.split(".")
		temporal = ""
		for x in range (len(new_name)):
			if x != (len(new_name) - 2):
				temporal = temporal + new_name[x] +"."
		temporal  = temporal[:-1]
		new_name = temporal

		with open(new_name, 'wb') as fo:
			fo.write(decripted)
		
print('bytes')
print(get_random_bytes(32))
key = b"qBr\x94S\xd3\xa2'\x8c\xf2n\xdcN!?\xada\xd0h`\x9c\x89\r\xf6\x06\x15j[\x1d\x9d\xb4\xbf" #get_random_bytes(32) #size for AES 256 
encriptor = Encryptor(key)
clear = lambda: os.system('cls')


while True:
	clear()
	choice = int(input("1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to exit.\n"))
	clear()
	if choice == 1:
		encriptor.encrypt_file(str(input("Enter name of file to encrypt: ")))
	elif choice == 2:    
		encriptor.decrypt_file(str(input("Enter name of file to decrypt: ")))
	elif choice == 3:    
		exit()
	else:    
		print("Please select a valid option!")
        










