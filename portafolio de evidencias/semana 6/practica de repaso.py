##Actividades semana 6
##clase de progrmacion
##23-2-2024

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

TiempoxVue=0
TiempoxPits=0
TiempoxVuenew=0
TiempoxPitsnew=0

for i in range(10):
    TiempoxVue=float(input("porfavor escriba cuanto tiempo se tardo en esta vuelta:"))
    TiempoxPits=float(input("porfavor escriba cuanto tiempo se tarda en pits"))
    TiempoxVuenew+=TiempoxVue
    TiempoxPitsnew+=TiempoxPits
    
TiempoTotal=(TiempoxPitsnew/TiempoxVuenew)*100

promedioTiempoxVue=TiempoxVuenew/10
promedioTiempoxPits=TiempoxPitsnew/10
print("el tiempo promedio por vuelta es de: ",promedioTiempoxVue,"%")
print("el tiempo promedio en los PITS es de: ",promedioTiempoxPits,"%")
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


CantidadNiños=int(input("Porfavor escriba la cantidad de niños que desea realizar la informacion: "))
Rango=range(CantidadNiños)
AlturaProm=0
menosCien=0
entreCienY120=0
entre121y130=0
entre131y140=0
mas140=0
for i in Rango:
    altura= int(input("porfavor escriva la estatura del niño"))
    if altura < 100:
        
        menosCien+=1
        
    elif altura => 100 and =< 120:
        
        entreCienY120+=1
        
    elif altura => 121 and =< 130:
        
        entre121y130+=1
        
    elif altura => 131 and =< 140:
        entre131y140+=1
        
    elif altura > 140 :
        mas140+=1
    else:
        print("opcion no valida")
        
    AlturaProm+=altura

Divicion=AlturaProm/CantidadNiños

print("La altura promedio es de:",Divicion," de todos los niños")

print("Ejercicio 3")
##3. Desarrollar un programa que le solicite al usuario un valor y muestre los primeros 
##10 números divisibles entre este valor. 
Num=int(input("Porfavor digite un numero: "))

for i in 10:
    if Num% i==0:
        print(i,"es divisible entre ",Num)

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
