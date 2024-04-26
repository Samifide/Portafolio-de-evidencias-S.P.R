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
