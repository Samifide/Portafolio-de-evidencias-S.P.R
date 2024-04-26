#Practica 3
##semana 9 Programacion basica
##viernes de 6-9 pm
#Samantha Perez rojas
##La fecha y hora máxima de entrega es el 22 de marzo del 2024 a las 11:55 pm.

##Instrucciones generales.
##La pulpería de su comunidad tiene a la venta múltiples productos que son parte de su oferta
##semanal, esta oferta puede ser cambiada ya sea porque se agrega un producto nuevo o porque
##se elimina uno de ellos. En estos productos se encuentran los siguiente grupos:
##● Articulos enlatados.
##● Productos de limpieza.
##● Carnes.
##● Granos. (Arroz, frijoles, entre otros)
##Donde cada grupo indica los nombres de los productos. El administrador debe poder
##seleccionar alguno de los grupos realizar las siguientes acciones:
##- Agregar productos.
##- Eliminar uno de los productos.
##- Actualizar uno de los productos.
##El programa debe ser capaz de mostrar todos los elementos de la lista, de la siguiente manera:
##- Producto 1: <producto>
##- Producto 2: <producto>
##- ...
##- Producto n: <producto>
##Donde n, es el último producto del conjunto.
##Los productos deben mostrarse en las siguientes circunstancias:
##- Antes de eliminar un producto.
##- Después de eliminar un producto.
##- Después de agregar un producto.
##- Después de actualizar un producto.
##Ahora bien, si el producto que se desea agregar, ya existe en el conjunto, entonces no se
##agrega y se muestra un mensaje:
##El producto ya existe.
##Para realizar la eliminación de un producto, investigue cómo se elimina los elementos de las
##listas y de los arreglos en python.

def Mostrar(lista):
    for i in range(len(lista)):
        print("Producto",i+1,"", lista[i])

def eliminar(lista,articulo):
    print(lista)
    articulo.lower()
    for i in lista:
        if articulo==i:
            lista.remove(i)
        else:
            print("realizando busqueda")
    print(lista)
    Mostrar(lista)
    return lista

def Agregar(lista,articulo):
    print(lista)
    articulo.lower()
    if articulo in lista:
        print("este Producto ya existia")
    else:
        lista.append(articulo)
        print("Producto agregado")
    print(lista)
    Mostrar(lista)
    return lista

def Actualizar(lista):
    print(lista)
    e=0
    for i in lista:
        print(e,"-",i)
        e+=1
    print(lista)
    lugar=int(input("Dijite el numero del Producto que desea cambiar"))
    new_elemento=input("Porfavor Dijite el nuevo Producto para reemplazar")
    new_elemento.lower()
    lista[lugar]=new_elemento
    Mostrar(lista)
    return lista



Articulos_enlatados=[]
Productos_limpieza=[]
Carnes=[]
Granos=[]
Productos_ofertasemanal=[]


while True:
    
    print("Este es un menu para agregar, eliminar o modificar ofertas.\n ********Decida el tipo de Producto que desea corregir******** ")

    print("1-Articulos enlatados")
    print("2-Productos de limpieza")
    print("3-Carnes")
    print("4-Granos.(Arroz, frijoles, entre otros)")
    articulo=int(input())
    
    if articulo==1:
        print("\n")
        print("lista: Articulos enlatados \n Defina que accion desea realizar")
        Accion2=int(input("1-Agregar Un Producto \n 2-Eliminar un Producto \n 3-Actualizar Producto \n "))
        if Accion2==1:
            articulo=input("Defina el nombre del articulo que desea agregar: ")
            Agregar(Articulos_enlatados,articulo)
            
        elif Accion2==2:
            articulo=input("Escriba el nombre del Producto que desea eliminar")
            eliminar(Articulos_enlatados,articulo)
        elif Accion2==3:
            Actualizar(Articulos_enlatados)
        else:
            print("Opcion no disponible, disculpas")
              
    elif articulo==2:
        print("\n")
        print("lista: Productos limpieza \n Defina que accion desea realizar")
        Accion2=int(input("1-Agregar Un Producto \n 2-Eliminar un Producto \n 3-Actualizar Producto \n "))
        if Accion2==1:
            articulo=input("Defina el nombre del Producto que desea agregar: ")
            Agregar(Productos_limpieza,articulo)
        elif Accion2==2:
            articulo=input("Escriba el nombre del Producto que desea eliminar")
            eliminar(Productos_limpieza,articulo)
        elif Accion2==3:
            Actualizar(Productos_limpieza)
        else:
            print("Opcion no disponible, disculpas")
              
        
    elif articulo==3:
        print("\n")
        print("lista: Carnes \n Defina que accion desea realizar")
        Accion2=int(input("1-Agregar Un Producto \n 2-Eliminar un Producto \n 3-Actualizar Producto \n "))
        if Accion2==1:
            articulo=input("Defina el nombre del Producto que desea agregar: ")
            Agregar(Carnes,articulo)
        elif Accion2==2:
            articulo=input("Escriba el nombre del Producto que desea eliminar")
            eliminar(Carnes,articulo)
        elif Accion2==3:
            Actualizar(Carnes)
        else:
            print("Opcion no disponible, disculpas")
        
    elif articulo==4:
        print("\n")
        print("lista: Granos.(Arroz, frijoles, entre otros) \n Defina que accion desea realizar")
        Accion2=int(input("1-Agregar Un Producto \n 2-Eliminar un Producto \n 3-Actualizar Producto \n "))
        if Accion2==1:
            articulo=input("Defina el nombre del Producto que desea agregar: ")
            Agregar(Granos,articulo)
        elif Accion2==2:
            articulo=input("Escriba el nombre del producto que desea eliminar")
            eliminar(Granos,articulo)
        elif Accion2==3:
            Actualizar(Granos)
        else:
            print("Opcion no disponible, disculpas")

              
    else:
        print("Opcion no disponible, disculpas")
    Decicion=input("Desea seguir modificando las ofertas? Y(si ) O N(No)")
    Decicion.lower()
    if Decicion=="n":
        break
    
Productos_ofertasemanal+=[Articulos_enlatados,Productos_limpieza,Carnes,Granos]
print("\n")
print("Los productos puestos en oferta son:")
for i in range(len(Productos_ofertasemanal)):
    print (Productos_ofertasemanal[i])
print("\n MUCHAS GRACIAS Y BUEN DIA")
    
