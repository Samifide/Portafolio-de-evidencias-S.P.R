#samantha perez rojas
##15-03-2024
##semana 9
##ejercicio 1
##Eduardo es un joven ciclista, cada semana debe reportar a su 
##entrenador la cantidad de kilómetros recorridos en sus prácticas. Haga 
##un programa que le permita almacenar para cada día los kilómetros 
##recorridos y luego al final de la semana muestre por cada día, junto con 
##el total de la semana. Para la solución, utilice arreglos y ciclos.
i=0
dia=[]
canti_KM=0
while i!=7:
    i+=1
    print("Dia: ", i)
    Kilometros_recorridos=int(input("dijite la cantida de kilometros que recorrio este dia"))
    canti_KM=canti_KM+Kilometros_recorridos
    dia.append(Kilometros_recorridos)

print("La cantidad completa de kilometros es: ",canti_KM)

e=0
for i in dia:
    e+=1
    print("la cantidad de kilometros en el dia",e,"son")
    print (i)
    
