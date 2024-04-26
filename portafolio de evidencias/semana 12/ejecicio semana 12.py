##ejercicio semana 12

##Desarrolle un programa que controla las notas obtenidas por los estudiantes 
##del curso de Programación Básica.
##En un archivo debe registrar la siguiente información: nombre, número de 
##grupo y calificación.
##Cree las funciones para agregar y mostrar información.
##Es conveniente que el acceso a las funciones se realice a través de un menú.
lista_estudiantes=[]
import os 


def agregar():
    estudiante=[]
    nombre=input("defina el nombre del estudiante: ")
    grupo=input("Porfavor escriba el numero de su grupo: ")
    calificacion=int(input("Porfavor escriba la calificacion obtenida en prueba \n __"))
    estudiante.append(["\n",["nombre",nombre],["grupo",grupo],["calificacion",calificacion]])
    return estudiante

def agregaAtexto(lista_estudiantes):
    lista_estudiantes=str(lista_estudiantes)
    archivo_nuevo=open("text.txt", "w")
    archivo_nuevo.write(lista_estudiantes)
    archivo_nuevo.close()
    
        
def mostrar(lista_estudiantes):
    print (lista_estudiantes)

while True:
    print("1- ingresar calificaciones")
    print("2- mostrar claificaciones")
    Desicion =int(input("Cual accion desea realizar"))
    if Desicion==1:
        lista_estudiantes+=agregar()
        print(lista_estudiantes)
        agregaAtexto(lista_estudiantes)
        
    elif Desicion==2:
        mostrar(lista_estudiantes)
    else:
        print("informacion ingresada incorrecta")
        
