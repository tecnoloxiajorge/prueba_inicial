# datos personales
# -*- coding: utf-8 -*-
datos=[]

# nombre
nombre=raw_input("Introduce tu nombre: ")
while nombre.isalpha()==False:
	print("Nombre incorrecto!")
	nombre=raw_input("Introduce tu nombre: ")
datos.insert(0,nombre)

# telefono
telefono=raw_input("Introduce número de teléfono: ")
while telefono.isdigit()==False or len(telefono)!=9:
	print("Número incorrecto")
	telefono=raw_input("Introduce número de teléfono(9 digitos): ")
datos.insert(1,telefono)

# contraseña
confirmapass=" "
contrasena=1
while contrasena!=confirmapass:
	contrasena=raw_input("Indica tu contraseña: ")
	while contrasena.isalnum()==False or len(contrasena)<8:
		print("Contraseña incorrecta")
		contrasena=raw_input("Introduce una contraseña (al menos 8 caracteres y letras y números): ")
	confirmapass=raw_input("Confirma la contraseña: ")
datos.insert(2,contrasena)

# correo electronico
arroba=False
punto=False
while arroba==False or punto==False:
	arroba=False
	punto=False
	correo=raw_input("Introduce el correo electrónico: ")
	for var in correo:
		if var=="@":
			arroba=True
		if var==".":
			punto=True
	if arroba==False or punto==False:
		print("Correo incorrecto")

datos.insert(3,correo)


print(datos)



 


