##Actividades semana 6
##clase de progrmacion
##23-2-2024

#Practica de repaso 1

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
        
    elif altura >= 100 and altura <= 120:
        
        entreCienY120+=1
        
    elif altura>=121 and altura<= 130:
        
        entre121y130+=1
        
    elif altura>=131 and altura<= 140:
        entre131y140+=1
        
    elif altura > 140 :
        mas140+=1
    else:
        print("opcion no valida")
        
    AlturaProm+=altura

Divicion=AlturaProm/CantidadNiños

print("La altura promedio es de:",Divicion," de todos los niños")

