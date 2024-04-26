#samantha perez rojas
##15-03-2024
##semana 9
##ejercicio 2
##En una sala de teatro se requiere almacenar los nombres de las personas 
##que ocuparán las butacas de una fila, cada fila tiene 10 butacas. Cree 
##un programa que almacena los nombres en las posiciones que le van 
##indicando, por ejemplo: Ana Jiménez, 4 (el cuatro indica el número de 
##butaca).
fila=[]
butaca=[]
campo=0
for i in range(10):
    nombre=input("porfavor dijite su nombre: ")
    campo=campo+1
    butaca+=[nombre,campo]
    fila.append(butaca)
    butaca=[]


for e in range(len(fila)):
    print(fila[e])
