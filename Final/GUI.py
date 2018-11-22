import Main 
from Main import Menu as men
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from  tkinter import *

FUENTE = ("Arial",25)

menu = men("Cipher")

def valid_pass(password):
	if len(password) >= 8: 
		return bool(re.match('^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!#$?])', password))
	else:
		return False 

def warning_pass():
	messagebox.showwarning("Contraseña","La contraseña debe tener al menos 8 caracteres, una minúscula, una mayúscula, un número y caracter especial")

def warning_blank():
	messagebox.showwarning("Llenar campos","Es necesario llenar todos los campos")

def mistaken_fields():
	messagebox.showwarning("Campos incorrectos","Alguno de los campos enviados es incorrecto")

def done_cifer(text):
	messagebox.showinfo("Completo",text)

def show_pass(event,label):
	label.configure(show="")

def hide_pass(event,label):
	label.configure(show="*")

def delete_values(entryRes): 
	entryRes.delete(0, 'end')

#Llamado a clase para cifrar texto
def cifrar_texto(event,text, passw,entryRes):
	if text == '' or passw == '': 
		warning_blank() 
	else: 
		if valid_pass(passw):
			res = menu.enc_text(text,passw)
			if res == 'ERROR_1234':
				mistaken_fields()
			else: 
				entryRes.delete(0, 'end')
				entryRes.insert(0,res)
		else:
			warning_pass()

#Llamado a clase para descifrar texto
def des_texto(event,text, password, entryRes):
	if text == '' or password == '': 
		warning_blank() 
	else: 
		res = menu.dec_text(text,password)
		if res == 'ERROR_1234':
			mistaken_fields()
		else: 
			entryRes.delete(0, 'end')
			entryRes.insert(0, res)

#llamado a clase para cifrar archivo 
def cifrar_archivo(event,file_root,password, del_original):
	if file_root == '' or password == '': 
		warning_blank() 
	else:
		if valid_pass(password):
			where_to_save = ''
			if del_original == 0:
				where_to_save = s_file()
			res = menu.enc_file(file_root, password,del_original,where_to_save)
			if res == 'ERROR_1234':
				mistaken_fields()
			else: 
				done_cifer("Se ha cifrado el archivo")
		else:
			warning_pass()

#Llamada descifrar archivo
def des_archivo(event,filename,password,where_to_save): 
	if filename == '' or password == '': 
		warning_blank() 
	else:  
		res= menu.dec_file(filename,password,where_to_save)
		if res == 'ERROR_1234':
			mistaken_fields()
		else: 
			done_cifer("Se ha descifrado el archivo")

#Buscador de archivos	
def search_file(event,entry):
	try: 
		root = Tk()
		root.withdraw()
		root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =[("all files","*.*"),("jpeg files","*.jpg")])
		entry.delete(0, 'end')
		entry.insert(0,root.filename)
	except: 
		mistaken_fields()

#Guardar archivos
def save_file(event,entry): 
	try: 
		root = Tk()
		root.withdraw()
		root.directory = filedialog.askdirectory()
		entry.delete(0, 'end')
		entry.insert(0,root.directory)
	except: 
		mistaken_fields()

def s_file(): 
	try: 
		root = Tk()
		root.withdraw()
		root.directory = filedialog.askdirectory()
		return root.directory
	except: 
		mistaken_fields()

class General(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		container = tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.frames = {}
		for x in (Principal,CifText,CifFile,DecText,DecFile):
			frame = x(container,self)
			self.frames[x] = frame 
			frame.grid(row = 0, column = 0, sticky="nsew")
		self.show_frame(Principal)

	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

class Principal(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Titulo 
		label = tk.Label(self,text = "Cifrado seguridad", font=FUENTE)
		label.pack()

		#Botón cifrar texto
		bCifText = tk.Button(self,text="Cifrar texto",command= lambda:controller.show_frame(CifText))
		bCifText.pack()

		#Botón cifrar archivo 
		bCifFile = tk.Button(self,text="Cifrar archivo",command= lambda:controller.show_frame(CifFile))
		bCifFile.pack()

		#Botón descifrar texto 
		bDecText = tk.Button(self,text="Descifrar texto",command= lambda:controller.show_frame(DecText))
		bDecText.pack()

		#Botón descifrar archivo 
		bDecFile = tk.Button(self,text="Descifrar archivo",command= lambda:controller.show_frame(DecFile))
		bDecFile.pack()

class CifText(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		#Titulo 
		label = tk.Label(self,text = "Cifrar Texto", font=FUENTE)
		label.pack()

		#Texto a cifrar 
		LT = tk.Label(self,text="Texto a cifrar")
		textEnt = tk.Entry(self)
		delete_values(textEnt)
		LT.pack()
		textEnt.pack()


		#Contraseña
		LP = tk.Label(self,text="Contraseña")
		passEnt = tk.Entry(self, show="*")
		LP.pack()
		passEnt.pack()

		#password functions 
		BV = tk.Button(self,text="VER")
		BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
		BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
		BV.pack()

		#Cifrar
		BCifrar = tk.Button(self,text="Cifrar")
		BCifrar.bind('<Button-1>',lambda a:cifrar_texto(a,textEnt.get(),passEnt.get(),textEnt))
		BCifrar.pack()

		#Menu principal 
		bHome = tk.Button(self,text="Menú Principal",command= lambda:controller.show_frame(Principal))
		bHome.pack()

		
		#Notas
		pLabel = tk.Label(self,text="La contraseña debe ser de una longitud mínima de 8 caracteres\n debe incluir una letra minúscula, una mayúscula, un digito y un caracter especial(! # $ ?)")
		pLabel.pack()

class CifFile(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		#titulo 
		label = tk.Label(self,text = "Cifrar archivo", font=FUENTE)
		label.pack()

		#ruta 
		LT = tk.Label(self,text="Ruta del archivo a cifrar")
		textEnt = tk.Entry(self)
		LT.pack()
		textEnt.pack()

		#explorar 
		BExplorar = tk.Button(self,text="Explorar archivos")
		BExplorar.bind('<Button-1>',lambda a:search_file(a,textEnt))
		BExplorar.pack()

		#Contraseña
		LP = tk.Label(self,text="Contraseña")
		passEnt = tk.Entry(self, show="*")
		LP.pack()
		passEnt.pack()

		#Propiedades contraseña
		BV = tk.Button(self,text="VER")
		BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
		BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
		BV.pack()

		#Check delete 
		checkVar = IntVar()
		Bcheck = tk.Checkbutton(self,text="Borrar original" ,variable=checkVar)
		Bcheck.pack()

		#Cifrar button 
		BCifrar = tk.Button(self,text="Cifrar")
		BCifrar.bind('<Button-1>',lambda w:cifrar_archivo(w,textEnt.get(),passEnt.get(),checkVar.get()))
		BCifrar.pack()
		Bcheck.pack()

		#Menu principal 
		bHome = tk.Button(self,text="Menú Principal",command= lambda:controller.show_frame(Principal))
		bHome.pack()

class DecText(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		#Titulo 
		label = tk.Label(self,text = "Descifrar texto", font=FUENTE)
		label.pack()

		#Texto a descifrar 
		LT = tk.Label(self,text="Texto a descifrar")
		textEnt = tk.Entry(self)
		LT.pack()
		textEnt.pack()

		#Contraseña
		LP = tk.Label(self,text="Contraseña")
		passEnt = tk.Entry(self, show= "*")
		LP.pack()
		passEnt.pack()

		#Metodos de contraseña
		BV = tk.Button(self,text="VER")
		BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
		BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
		BV.pack()

		#Descifrar botón 
		BDCifrar = tk.Button(self,text="Descifrar")
		BDCifrar.bind('<Button-1>',lambda a:des_texto(a,textEnt.get(),passEnt.get(),textEnt))
		BDCifrar.pack()

		#Menu principal 
		bHome = tk.Button(self,text="Menú Principal",command= lambda:controller.show_frame(Principal))
		bHome.pack()

class DecFile(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		#Titulo 
		label = tk.Label(self,text = "Cifrado seguridad", font=FUENTE)
		label.pack()

		#Ruta archivo a descifrar 
		LT = tk.Label(self,text="Ruta del archivo a descifrar")
		textEnt = tk.Entry(self)
		LT.pack()
		textEnt.pack()

		#Archivo a descifrar gui 
		BArchivoFile = tk.Button(self,text="Archivo a descifrar")
		BArchivoFile.bind('<Button-1>',lambda x:search_file(x,textEnt))
		saveEnt = tk.Entry(self)
		BArchivoFile.pack()
		saveEnt.pack()

		#Carpeta a guardar 
		BExplorar = tk.Button(self,text="Carpeta donde se guardará el archivo")
		BExplorar.bind('<Button-1>',lambda a:save_file(a,saveEnt))
		BExplorar.pack()
		
		#Contraseña
		LP = tk.Label(self,text="Contraseña")
		passEnt = tk.Entry(self, show="*")
		LP.pack()
		passEnt.pack()

		#Metodos contraseña
		BV = tk.Button(self,text="VER")
		BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
		BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
		BV.pack()

		#Boton cifrar 
		BCifrar = tk.Button(self,text="Descifrar")
		BCifrar.bind('<Button-1>',lambda a:des_archivo(a,textEnt.get(),passEnt.get(),saveEnt.get()))
		BCifrar.pack()

		#Menu principal 
		bHome = tk.Button(self,text="Menú Principal",command= lambda:controller.show_frame(Principal))
		bHome.pack()

app = General()
app.title('Seguridad Informática')
app.mainloop()