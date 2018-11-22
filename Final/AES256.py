import base64 
from Crypto.Cipher import AES
from Crypto import Random  
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os 
import time 

class Encryptor: 
	def __init__(self, key):
		self.key = key 


	def blockSize(self, s):
		return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

	def deleteFile(self,file_name): #used after encryption or decryption 
		os.remove(file_name)

	def encrypt(self, message, key):
		try: 
			key_size=32
			message = self.blockSize(message)
			iv = Random.new().read(AES.block_size)
			cipher = AES.new(key, AES.MODE_CBC, iv)
			msg = iv + cipher.encrypt(message)
			msg = base64.b64encode(msg)
			return msg
		except: 
			return 'ERROR_1234'

	def encrypt_text(self,text): # method to cipher text
		try: 
			message = bytes(text,'utf-8')
			encripted = self.encrypt(message,self.key)
			encripted = encripted.decode("utf-8") 
			return encripted
		except: 
			return 'ERROR_1234'


	def encrypt_file(self, file_name,where_to_save):
		try: 
			with open(file_name, 'rb') as fo:
				text = fo.read()
			encripted = self.encrypt(text,self.key)
			new_name = file_name.split(".")
			if len(new_name) > 2:
				temporal = ""
				for x in range (len(new_name)-1):
					temporal = temporal + new_name[x] +"."
				temporal  = temporal[:-1]
				new_name = [temporal,new_name[len(new_name)-1]]

			if where_to_save == '':
				with open(new_name[0] + ".cfr." + new_name[1], 'wb') as fo:
					fo.write(encripted)
				return 'Done'
			else: 
				print("where to save")
				print(where_to_save)
				new = new_name[0].split("/")
				print()
				name = where_to_save + '/'+ new[len(new)-1]
				print("name")
				print(name)
				with open(name + ".cfr." + new_name[1], 'wb') as fo:
					fo.write(encripted)
				return 'Done'
		except: 
			return 'ERROR_1234'
		

	def decrypt(self,cipheredText, key):
		try: 
			cipheredText = base64.b64decode(cipheredText)
			iv = cipheredText[:AES.block_size] # unpad
			cipher = AES.new(key,AES.MODE_CBC,iv)
			text = cipher.decrypt(cipheredText[AES.block_size:])
			res = text.rstrip(b"\0")
			return res 
		except:
			return 'ERROR_1234'

	def decrypt_text(self,enc_text):
		try: 
			decripted = self.decrypt(enc_text,self.key)
			decripted = decripted.decode("utf-8") 
			return(decripted)
		except:
			return 'ERROR_1234'

	def decrypt_file(self,file_name,where_to_save):
		try: 
			with open(file_name,'rb') as fo:
				cipheredText = fo.read()
			decripted = self.decrypt(cipheredText,self.key)
			new_name = file_name.split(".")
			temporal = ""
			for x in range (len(new_name)):
				if x != (len(new_name) - 2):
					temporal = temporal + new_name[x] +"."
			temporal  = temporal[:-1]
			new_name = temporal

			if where_to_save == '':
				with open(new_name, 'wb') as fo:
					fo.write(decripted)
				return 'Done'
			else: 
				new_name = new_name.split("/")
				name = where_to_save + '/'+ new_name[len(new_name)-1]
				with open(name, 'wb') as fo:
					fo.write(decripted)
				return 'Done'

		except:
			return 'ERROR_1234'

	def set_password(self,password): 
		salt = b'salt for encryption'
		kfd = PBKDF2(password,salt,32,1000)
		key = kfd[:16]
		self.key  = key

	def get_password(self):
		return self.key 
		

















