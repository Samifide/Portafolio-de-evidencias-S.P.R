##samantha perez rojas
##semana10
##clase programacion basica
##viernes 6-9

##ejercicio 2
##Un profesor necesita un programa que calcule la nota final de 
##sus estudiantes. Tiene 25 estudiantes que realizan 4 actividades 
##evaluativas (para efectos de esta clase, se reducirá a 5 
##estudiantes).
##Utilice una matriz para almacenar las calificaciones donde 
##cada fila representará un estudiante y las columnas 
##almacenarán la información de las actividades evaluativas.


lista_estudiantes=[]

def calificar_notas(lista):
    for i in range (len(lista)):
        print (lista[i])
        columna=lista[i]
        for e in range(len(columna)):
            print("informacion del estudiante",i+1,columna[e])


i=0
while i<=4:
    i+=1
    print("Estudiante",i)
    estudiante=[]
    for e in range(0,4):
        print("Digite su calificacion de la actividad",e+1)
        calificacion=int(input(":"))
        estudiante+=[calificacion]
    lista_estudiantes+=[estudiante]
    print("\n")

    

print(lista_estudiantes)

calificar_notas(lista_estudiantes)
