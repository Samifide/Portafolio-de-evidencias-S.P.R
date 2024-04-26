#clase4. semana4
#condicionales
#samantha perez rojas

##Ejercicio 3
#Desarrolle un programa que le indique si su año de nacimiento es en año bisiesto.
#Nota Considere que un año bisiesto es aquel que es divisible entre 4 pero 
#que no es divisible entre 100, excepto el que es divisible entre 400
# > <

año=int(input("Porfavor dijite su año de nacimiento"))

if año%4==0 and año%100!=0 or año%400==0:
    print("Su año de nacimiento es Bisiesto: ",año)
else:
    print("su año de nacimiento no es Bisiesto: ",año)
