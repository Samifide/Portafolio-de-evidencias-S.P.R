##Ejercicios 16-2-2024
##calse 5
##Programacion Basica

##ejercicio 3
##• Desarrolle un programa que convierta a binario un número ingresado por el usuario.
##Mejore el ejercicio mostrándolo en octal y hexadecimal.
Numero=int(input("Porfavor ingrese un numero"))
binario = format(int(Numero), '08b')
print("este es el numero en binario",binario)

Octal = oct(Numero)
print("este es el numero en octal",Octal)

hexadecimal = hex(Numero)
print("este es el numero en hexadecimal",hexadecimal)

