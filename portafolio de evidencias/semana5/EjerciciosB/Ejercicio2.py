##16-2-2024
##Ejemplo-EJERCICIO 2
##SEMANA 5

##Desarrolle un programa que permita determinar la nota mayor, la nota menor,
##la cantidad de aprobados y la cantidad de reprobados de un grupo de alumnos.
##Muestre los resultados obtenidos.
##Notas: No se conoce la cantidad de alumnos.
##La nota de aprobación es 70.

Aprovados=0
Reprovados=0

Introducir=input("¿Desea introducir estudiantes?")
while Introducir=="Si" or Introducir=="SI" or Introducir=="si":
    Nota=int(input("Porfavor escriba la nota del estudiante"))
    if Nota>=70:
        Aprovados+=1
    else:
        Reprovados+=1
    Introducir=input("¿Desea introducir estudiantes?")
print("!MUCHAS GRACIAS¡")
print("La cantidad de reprovados es",Reprovados)
print("La cantidad de Aprovados es",Aprovados)
