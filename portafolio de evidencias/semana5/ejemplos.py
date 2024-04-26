##clase 5
##ejemplos
##Ciclos REPETITIVOS
##FOR . while etc
##EJEMPLO1
rango= range(20)

print (rango)
#repite la cantidad que se pide
for i in range(20):
    print("el elemento es:",i)

print("\n")
print("\n")
print("\n")
print("\n")
##EJEMPLO2
## linea 14 :conjunto: mete en una variable cantidas de numeros o palabras
##listaA=[1,2,3,4,5,6,7,8]
listaB=["AAAAAAAAAAA","BBBBBB"]
##el for repite para cada elementos que definimos
for ELEMENTO in listaB:
                ##mostrar datos metidos en lista A/Lista B              
    print("el elemento es:",ELEMENTO)
print("\n")
print("\n")
print("\n")
print("\n")
##EJEMPLO3

##EL FOR REPITE LA CANTIDAD QUE LE DECIMOS
for b in range(5,20,2):
##       range (empezar, terminar, frecuencia)
    print("el elemento es:",b)
print("\n")
print("\n")
print("\n")
print("\n")
##EJEMPLO4
##EL FOR REPITE LA CANTIDAD QUE LE DECIMOS de donde a donde
for v in range(5,20):
##       range (empezar, terminar)
    print("el elemento es:",v)
print("\n")
print("\n")
print("\n")
print("\n")
##EJEMPLO5
##REPETIR DATOS DEFINIDOS CON CONDICION
for C in range(1,20):
##       range (empezar, terminar)
    if (C%2==0):
        print("el elemento es:C",C)
    
print("\n")
print("\n")
print("\n")
print("\n")

##------------------------------------------WHILE
#EJEMPLO 6 WHILE
Valor=20
while Valor>0:
    print("multiplicando",Valor,"par 2:",Valor*2)
    Valor=Valor-1
print("salir del while")
##
print("\n")
print("\n")
print("\n")
print("\n")
#EJEMPLO 7 WHILE
ValorB=20
while ValorB>0 and ValorB-1>2:
    print("multiplicando",ValorB,"par 2:",ValorB*2)
    ValorB=ValorB-1
print("salir del while")
print("\n")
print("\n")
print("\n")
print("\n")
##
#EJEMPLO 8 WHILE
Entrada=input("Ingrese entrada para el while")
while Entrada=="a":
    print("emtro en el siclo")
    Entrada=input("quiere salir")
print("acaba de salir")

#EJEMPLO 8 WHILE
Entrada=input("Ingrese entrada para el while")
while Entrada!="a":
    print("emtro en el siclo")
    Entrada=input("quiere salir")
print("acaba de salir")
##
