import Main 
from Main import Menu as men
import tkinter
from tkinter import filedialog
from tkinter import *

menu = men("hola")
gui = tkinter.Tk()
gui.title('Cifrado Seguridad Informatica')
gui.geometry('400x450')
gui.configure(background='thistle')

def show_pass(event,label):
	label.configure(show="")

def hide_pass(event,label):
	label.configure(show="*")

def cifrar_texto_view():
	gui.withdraw()
	ct = tkinter.Toplevel()
	LT = tkinter.Label(ct,text="Texto a cifrar")
	textEnt = tkinter.Entry(ct)
	LP = tkinter.Label(ct,text="Contraseña")
	passEnt = tkinter.Entry(ct, show="*")
	BV = tkinter.Button(ct,text="VER")
	BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
	BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
	Lress= tkinter.Label(ct)
	Lres = tkinter.Label(ct)
	BCifrar = tkinter.Button(ct,text="Cifrar")
	BCifrar.bind('<Button-1>',lambda a:cifrar_texto(a,textEnt.get(),passEnt.get(),Lress,Lres))

	pLabel = tkinter.Label(ct,text="La contraseña debe ser de una longitud mínima de 8 caracteres, y debe incluir una letra minúscula, una mayúscula, un digito y un carácter especial")
	BHome = tkinter.Button(ct, text="Menú principal")
	LT.pack()
	textEnt.pack()
	LP.pack()
	passEnt.pack()
	BV.pack()
	BCifrar.pack()
	pLabel.pack()

	Lress.pack()
	BHome.pack()
	Lres.pack()


def cifrar_texto(event,text, passw,labelTitle,labelRes):
	res = menu.enc_text(text,passw)
	labelTitle.config(text="TEXTO ENCRIPTADO")
	labelRes.config(text=res)
	print(res)


def des_texto_view():
	gui.withdraw()
	ct = tkinter.Toplevel()
	LT = tkinter.Label(ct,text="Texto a descifrar")
	textEnt = tkinter.Entry(ct)
	LP = tkinter.Label(ct,text="Contraseña")
	passEnt = tkinter.Entry(ct, show= "*")
	BV = tkinter.Button(ct,text="VER")
	BDCifrar = tkinter.Button(ct,text="Descifrar")
	Lress= tkinter.Label(ct)
	Lres = tkinter.Label(ct)

	BDCifrar.bind('<Button-1>',lambda a:des_texto(a,textEnt.get(),passEnt.get(),Lress,Lres))
	BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
	BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
	BHome = tkinter.Button(ct, text="Menú principal")
	LT.pack()
	textEnt.pack()
	LP.pack()
	passEnt.pack()
	BV.pack()
	BDCifrar.pack()
	BHome.pack()
	Lress.pack()
	Lres.pack()

def des_texto(event,text, password, labelTitle, labelRes):
	res = menu.dec_text(text,password)
	labelTitle.config(text="TEXTO PLANO")
	labelRes.config(text=res)
	print(res)



def cifrar_archivo_view():
	gui.withdraw()
	ct = tkinter.Toplevel()
	LT = tkinter.Label(ct,text="Ruta del archivo a cifrar")
	textEnt = tkinter.Entry(ct)
	BExplorar = tkinter.Button(ct,text="Explorar")
	BExplorar.bind('<Button-1>',lambda a:search_file(a,textEnt))
	LP = tkinter.Label(ct,text="Contraseña")
	passEnt = tkinter.Entry(ct, show="*")
	BV = tkinter.Button(ct,text="VER")
	BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
	BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
	checkVar = IntVar()
	Bcheck = tkinter.Checkbutton(ct,text="Borrar original" ,variable=checkVar)
	BCifrar = tkinter.Button(ct,text="Cifrar")
	BCifrar.bind('<Button-1>',lambda w:cifrar_archivo(w,textEnt.get(),passEnt.get(),checkVar.get()))
	BHome = tkinter.Button(ct, text="Menú principal")
	pLabel = tkinter.Label(ct,text="La contraseña debe ser de una longitud mínima de 8 caracteres, y debe incluir una letra minúscula, una mayúscula, un digito y un carácter especial")
	LT.pack()
	textEnt.pack()
	BExplorar.pack() 
	LP.pack()
	passEnt.pack()
	BV.pack()
	BCifrar.pack()
	Bcheck.pack()
	pLabel.pack()
	BHome.pack()

def cifrar_archivo(event,file_root,password, del_original):
	print("state")
	print(del_original)
	menu.enc_file(file_root, password,del_original)
	print("Done cifer")


def search_file(event,entry):
	root = Tk()
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =[("all files","*.*"),("jpeg files","*.jpg")])
	entry.delete(0, 'end')
	entry.insert(0,root.filename)
	print (root.filename)

def save_file(event,entry): 
	root = Tk()
	root.directory = filedialog.askdirectory()
	entry.delete(0, 'end')
	entry.insert(0,root.directory)
	print (root.directory)

def des_archivo_view(): 
	gui.withdraw()
	ct = tkinter.Toplevel()
	LT = tkinter.Label(ct,text="Ruta del archivo a descifrar")
	textEnt = tkinter.Entry(ct)
	BArchivoFile = tkinter.Button(ct,text="Archivo a descifrar")
	BArchivoFile.bind('<Button-1>',lambda x:search_file(x,textEnt))
	saveEnt = tkinter.Entry(ct)
	BExplorar = tkinter.Button(ct,text="Carpeta donde se guardará el archivo")
	BExplorar.bind('<Button-1>',lambda a:save_file(a,saveEnt))
	LP = tkinter.Label(ct,text="Contraseña")
	passEnt = tkinter.Entry(ct, show="*")
	BV = tkinter.Button(ct,text="VER")
	BCifrar = tkinter.Button(ct,text="Descifrar")
	BCifrar.bind('<Button-1>',lambda a:des_archivo(a,textEnt.get(),passEnt.get()))
	BV.bind('<Button-1>',lambda y:show_pass(y,passEnt))
	BV.bind('<ButtonRelease-1>',lambda x:hide_pass(x,passEnt))
	BHome = tkinter.Button(ct, text="Menú principal")
	LT.pack()
	BArchivoFile.pack()
	BExplorar.pack()
	textEnt.pack()
	saveEnt.pack()
	LP.pack()
	passEnt.pack()
	BV.pack()
	BCifrar.pack()
	BHome.pack()


def des_archivo(event,filename,password): 
	menu.dec_file(filename,password)

def cerrar(): 
	gui.destroy()


# principal 
Titulo = tkinter.Label(gui,text="SCSeguridad")
Titulo.pack()


BCifTexto = tkinter.Button(gui, text ="Cifrar Texto",command=cifrar_texto_view) #command=cifrar_texto_view)
BCifArchivo = tkinter.Button(gui, text ="Cifrar Archivo",command=cifrar_archivo_view)
BDesTexto = tkinter.Button(gui, text ="Descifrar Texto",command=des_texto_view)
BDesArchivo = tkinter.Button(gui, text ="Descifrar Archivo",command=des_archivo_view)
BCifTexto.pack()
BCifArchivo.pack()
BDesTexto.pack()
BDesArchivo.pack()

BExit = tkinter.Button(gui, text ="Cerrar",command=cerrar)
BExit.pack()


gui.mainloop()

