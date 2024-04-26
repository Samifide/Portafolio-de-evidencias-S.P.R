##samantha perez rojas
##semana10
##clase programacion basica
##viernes 6-9

##ejercicio 1
##Comparta con su profesor, algunos casos en los que se considera que es 
##necesario utilizar un arreglo de dos dimensiones para almacenar los 
##datos.
##De los casos mencionados anteriormente, desarrolle un ejercicio 
##relacionado, su profesor podrá orientarlo al respecto.

####crear una pequeña base de datos que recorra la matriz y agrege usarios(nombre y cedula)

lista_usuarios=[]
usuario=[]

def recorrer_lista_usuarios(lista):
    for i in range (len(lista)):
        print (lista[i])
        columna=lista[i]
        for e in range(len(columna)):
            print("informacion de usuario",i,columna[e])




while True:
    nombre=input("Digite el nombre del usuario")
    cedula=int(input("dijite el numero de cedula"))
    usuario=[nombre,cedula]
    lista_usuarios+=[usuario]
    SN=input("Desea salir dejar de introducir usuarios?1=si|0=no")
    if SN=="1":
        break
    

print(lista_usuarios)

recorrer_lista_usuarios(lista_usuarios)



