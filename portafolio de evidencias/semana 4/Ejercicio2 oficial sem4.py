#clase4. semana4
#condicionales
#samantha perez rojas

##Ejercicio 2
#Desarrolle un programa que ordene de forma descendente 3 números.
#Nota suponga que los números son diferentes entre sí.
# > <
NumA=int(input("Porfavor ingrese el Primer dijito"))
NumB=int(input("Porfavor ingrese el Segundo dijito"))
NumC=int(input("Porfavor ingrese el Tercer dijito"))

if NumA>NumB and NumA>NumC:
    if NumB>NumC:
        print("De Mayor a menor")
        print("",NumA,",",NumB,",",NumC)
    else:
        print("De Mayor a menor")
        print("",NumA,",",NumC,",",NumB)
else:
    if NumB>NumA and NumB>NumC:
        if NumA>NumC:
            print("De Mayor a menor")
            print("",NumB,",",NumA,",",NumC)
        else:
            print("De Mayor a menor")
            print("",NumB,",",NumC,",",NumA)
    else:
        if NumC>NumA and NumC>NumB:
            if NumA>NumB:
                print("De Mayor a menor")
                print("",NumC,",",NumA,",",NumB)
            else:
                print("De Mayor a menor")
                print("",NumC,",",NumB,",",NumA)
print("Muchas Gracias")
