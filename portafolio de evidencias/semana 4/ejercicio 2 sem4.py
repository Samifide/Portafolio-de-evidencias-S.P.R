#clase4. semana4
#condicionales
#samantha perez rojas

##Ejercicio 2 aparte MODIFICADO
##Desarrolle un programa que muestre el mayor de dos números. 
##Tiempo aproximado 15 minutos
##Modifique el programa para que funcione 
##para 4 números.
NumA=int(input("Porfavor ingrese el primer numero"))
NumB=int(input("Porfavor ingrese el segundo numero"))
NumC=int(input("Porfavor ingrese el tercer numero"))
NumD=int(input("Porfavor ingrese el cuarto numero"))
if NumA >NumB and NumA >NumC and NumA >NumD:
    #Salida para A
    print("el numero ",NumA ," es mayor")
else:
    if NumB >NumA and NumB >NumC and NumB >NumD:
        #Salida para B
        print("el numero ",NumB, " es mayor")
    else:
        #Salida para c
        if NumC >NumA and NumC >NumB and NumC >NumD:
            print("el numero ",NumC, " es mayor")
        else:
            #Salida para D
            print("el numero ",NumD, " es mayor")
print ("Buen dia")
