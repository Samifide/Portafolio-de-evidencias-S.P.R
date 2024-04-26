#Practica de repaso 1
#introduccion

##1. Un corredor de Fórmula 1 requiere de un programa que le capture los tiempos 
##realizados en cada vuelta y los tiempos utilizados en PITS, de manera que este al final le 
##indique lo siguiente: 
##• Cuál es el tiempo promedio por vuelta. 
##• Cuál es el tiempo promedio por PITS. 
##• Qué porcentaje del tiempo PITS corresponde al tiempo de recorrido de una 
##vuelta. 
##• Considere que son 10 vueltas y 10 entradas a PITS.
print("Ejercicio 1")
TiempoxVue=input("porfavor escriba cuanto tiempo se tarda por vuelta")
TiempoxVue=int(TiempoxVue)
TiempoxPits=input("porfavor escriba cuanto tiempo se tarda en pits")
TiempoxPits=int(TiempoxPits)
TiempoxVue*=10
TiempoxPits*=10
TiempoTotal=((TiempoxPits/TiempoxVue)/10)*1000
print("el tiempo total en porcentaje es de: ",TiempoTotal,"%")

print("Ejercicio 2")
##2. Se requiere analizar las estaturas de los N niños de una escuela y extraer la siguiente 
##estadística:
##• Cantidad de niños que miden menos de 100 cm.
##• Cantidad de niños que miden entre 100 y 120 cm.
##• Cantidad de niños que miden entre 121 y 130 cm.
##• Cantidad de niños que miden entre 131 y 140 cm.
##• Cantidad de niños que miden más de 140 cm.
##• Promedio de estaturas.
##• Muestre los resultados obtenidos.

CantidadA=input("Porfavor escriba la Cantidad de niños que miden menos de 100 cm: ")
CantidadA=int(CantidadA)
TotalA=CantidadA*0.99
Cantidadb=input("Porfavor escriba la Cantidad de niños que miden entre 100 y 120 cm: ")
Cantidadb=int(Cantidadb)
Totalb=Cantidadb*1.19
Cantidadc=input("Porfavor escriba la Cantidad de niños que miden entre 121 y 130 cm: ")
Cantidadc=int(Cantidadc)
Totalc=Cantidadc*1.29
Cantidadd=input("Porfavor escriba la Cantidad de niños que miden entre 131 y 140 cm: ")
Cantidadd=int(Cantidadd)
Totald=Cantidadd*1.39
Cantidade=input("Porfavor escriba la Cantidad de niños que miden más de 140 cm: ")
Cantidade=int(Cantidade)
Totale=Cantidade*1.41

Promedio= (TotalA+Totalb+Totalc+Totald+Totale)/(CantidadA+Cantidadb+Cantidadc+Cantidadd+Cantidade)

print("El promedio total de estaturas es de: ",Promedio)
print("Ejercicio 3")
##3. Desarrollar un programa que le solicite al usuario un valor y muestre los primeros 
##10 números divisibles entre este valor. 
Num=input("Porfavor digite un numero: ")
Num=int(Num)
TotalA=(Num*1)
Totalb=(Num*2) 
Totalc=(Num*3) 
Totald=(Num*4)
Totale=(Num*5) 
Totalf=(Num*6) 
Totalg=(Num*7) 
Totalh=(Num*8) 
Totali=(Num*9) 
Totalj=(Num*10)
print(TotalA,", ",Totalb,", ",Totalc,", ",Totald,", ",Totale,", ",Totalf,", ",Totalg,", ",Totalh,", ",Totali,", ",Totalj)
print("Ejercicio 4")
##4. Desarrolle un programa que le solicita al usuario 15 salarios y que le indique cuánto 
##dinero se necesita para que a menos todos ganen $500.

Salario1 = int(input("Ingrese un valor del salario 1: "))
Salario2 = int(input("Ingrese un valor del salario 2: "))
Salario3 = int(input("Ingrese un valor del salario 3: "))
Salario4 = int(input("Ingrese un valor del salario 4: "))
Salario5 = int(input("Ingrese un valor del salario 5: "))
Salario6 = int(input("Ingrese un valor del salario 6: "))
Salario7 = int(input("Ingrese un valor del salario 7: "))
Salario8 = int(input("Ingrese un valor del salario 8: "))
Salario9 = int(input("Ingrese un valor del salario 9: "))
Salario10 = int(input("Ingrese un valor del salario 10: "))
Salario11 = int(input("Ingrese un valor del salario 11: "))
Salario12 = int(input("Ingrese un valor del salario 12: "))
Salario13 = int(input("Ingrese un valor del salario 13: "))
Salario14 = int(input("Ingrese un valor del salario 14: "))
Salario15 = int(input("Ingrese un valor del salario 15: "))

promedioSalarios=(Salario1+Salario2+Salario3+Salario4+Salario5+Salario6+Salario7+Salario8+Salario9+Salario10+Salario11+Salario12+Salario13+Salario14+Salario15)/15
Faltante=500-promedioSalarios
print("se nesesitan: ",Faltante , " para que todos alcancen 500")
