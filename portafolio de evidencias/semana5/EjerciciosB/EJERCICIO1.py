##16-2-2024
##Ejemplo-EJERCICIO 1
##SEMANA 5
##Desarrolle un programa que muestre los números pares del 20 al 40 y a la 
##par de cada número muestre su cuadrado


Cuadrado=0
range(41)
for i in range(20,41):
    print(i)
    if i%2==0:
        Cuadrado=i**2
        print("El numero par es es:",i,". El numero al cuadrado es:",Cuadrado)
