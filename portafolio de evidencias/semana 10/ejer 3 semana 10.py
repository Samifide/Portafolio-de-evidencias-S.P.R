##samantha perez rojas
##semana10
##clase programacion basica
##viernes 6-9

##ejercicio 3
##Desarrolle un programa para reservar espacios en una microbús que da
##servicio en 4 horarios. Se le pide que inicialmente almacene un valor 0 en
##los 20 espacios disponibles, luego le solicite al usuario la posición que
##desea reservar, remplazando el valor de 0 por un 1 (que representa
##vendido).
##¿Qué otro valor se podría utilizar?
##Nota: Recuerde que el índice de las filas y columnas empieza en cero pero para el usuario la
##fila empieza en 1.

bus_Matris=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
print(len(bus_Matris))
while True:
    horario=int(input(" Porfavor elija el horario de bus que desea \n Horario 1 \n Horario 2 \n Horario 3 \n Horario 4 \n:"))
    horario=horario-1
    espacio=int(input("cual espacio le gustaria del 1 al 20?"))
    espacio=espacio-1
    print("!!!VENDIDO!!!")
    bus_Matris[horario][espacio]="¡1!"
    seguir=int(input("Desea seguir reservando espacio? 1=SI|0=NO"))
    if seguir==0:
        break
    

for i in range(len(bus_Matris)):
    print(bus_Matris[i],end="\n")
