#clase4. semana4
#9-2-2024
#condicionales
#samantha perez rojas
#------------------------------------------------------------------------------

#condicional if
#> <
#ejemplo 1
##a = 5
## 
##if (not a >= 100): # a >= 100 -> F | not F -> V
##    print("Hola")
##print("Fuera")

#ejercicio 
##Salario=float(input("Porfavor dijite su salario: "))
##if Salario < 1000:
##    Salario*=1.15
##print ("Su salario es: ",Salario)
#------------------------------------------------------------------------------
#if-else
##a=100
##if a <=100:
##    print("hola")
##else:
##    print ("Adios")
##print ("Fuera")

#ejercicio
##Salario=float(input("Porfavor dijite su salario: "))
##if Salario > 1000:
##    print("a su salario se le acaba de aplicar un 15%")
##    Salario*=1.15
##else:
##    print("a su salario se le acaba de aplicar un 20%")
##    Salario*=1.20
##print (Salario)
##
###------------------------------------------------------------------------------
##
###condicional if ANIDADO
###ejemplo
##nota= int(input("Ingrese su nota porfavor: "))
##if nota>=70:
##    #salida 1
##    print("Aprobado")
##else:
##    if nota >= 60:
##        #salida 2
##        print("Aplazado")
##    else:
##        #salida 3        
##        print("Reprobado!")
##print("Nos vemos.....!")


#------------------------------------------------------------------------------
#Practica Ejercicio 1
#Práctica Estructura de decisión if ANIDADO
#Desarrolle un programa que calcule el salario de un colaborador, según 
#su categoría se le aplica el aumento correspondiente.
##Salario= int(input("Ingrese su Salario porfavor : "))
##Categoria= int(input("Ingrese su Categoria tambien porfavor: "))
##if Categoria==1:
##    #salida 1
##    Salario*=1.0
##else:
##    if Categoria==2:
##        #salida 2
##        Salario*=1.2
##    else:       
##        if Categoria==3:
##            #salida 3 
##            Salario*=1.5
##        else:
##            #salida 4        
##            Salario*=2.0
##print("su nuevo salario es",Salario )

#uso del "elif" #
#Practica Ejercicio 1
##Desarrolle un programa que muestre si un estudiante aprobó o no un curso.
##Si la nota es mayor o igual 70, muestre un mensaje de “Aprobado” en caso
##contrario muestre un mensaje “Reprobado”.


##Nota=int(input("Porfavor ingrese su nota: "))
##
##if Nota >=90:
##    print ("Usted aprobo con ",Nota)
##elif Nota>=70 :
##    print("Aprovado")
##elif Nota>=60 :
##    print("Aplazado")
##else:
##    print("Reprobado")
##print("Muchas gracias")

#-----------------------------------------------------------------------------
##Ejercicio 1 aparte
##Desarrolle un programa que muestre el mayor de dos números. 

##NumA=int(input("Porfavor ingrese el primer numero"))
##NumB=int(input("Porfavor ingrese el segundo numero"))
##if NumA >NumB:
##    print("el numero ",NumA " es mayor")
##else:
##    if NumB >NumA:
##        print("el numero ",NumB " es mayor")
##    else:
##        print("Ambos numeros son iguales")
##print ("Buen dia")

#-----------------------------------------------------------------------------
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
