file = "hola.adios.ale.sos"
new_name = file.split(".")
temporal = ""
for x in range (len(new_name)):
	if x != (len(new_name)-2):
		temporal = temporal + new_name[x] +"."
temporal  = temporal[:-1]
new_name = temporal 
#new_name = [temporal,new_name[len(new_name)-1]]

print(new_name)
