##Semana 6 -> Entrega Práctica II
##samantha perez rojas
##clase programacion viernes 6-9 pm 
##Se desea crear un programa que identifique la temperatura promedio de las personas que
##ingresan por día a un establecimiento, como no se sabe la cantidad, cada persona ingresa,
##digita su nombre y también digita su temperatura. Esto se debe realizar para cada día de la
##semana laboral, es decir de lunes a viernes. El programa mostrará:
##● Temperatura promedio de las personas para cada día.
##● La persona con la temperatura más alta y menos alta por cada día con su respectivo
##nombre.
##Para realizar los ingresos, el programa consulta cual día desea ingresar
##Semana 6 -> Entrega Práctica II
##samantha perez rojas
##clase programacion viernes 6-9 pm 
##Se desea crear un programa que identifique la temperatura promedio de las personas que
##ingresan por día a un establecimiento, como no se sabe la cantidad, cada persona ingresa,
##digita su nombre y también digita su temperatura. Esto se debe realizar para cada día de la
##semana laboral, es decir de lunes a viernes. El programa mostrará:
##● Temperatura promedio de las personas para cada día.
##● La persona con la temperatura más alta y menos alta por cada día con su respectivo
##nombre.
##Para realizar los ingresos, el programa consulta cual día desea ingresar
Personas1=[]
Personas2=[]
Personas3=[]
Personas4=[]
Personas5=[]

Todos1=[]
Todos2=[]
Todos3=[]
Todos4=[]
Todos5=[]

while True:
    
    Aceptacion=input("Deseas Ver el menu de opciones o salir, Salir='No', menu='Si'?")

    if Aceptacion=="NO" or Aceptacion=="No" or Aceptacion=="n" or Aceptacion=="N":

        break
    
    else:
        print("[1] Lunes")
        print("[2] Martes")
        print("[3] Miercoles")
        print("[4] Jueves")
        print("[5] Viernes")
        print("[6] Mostrar resultados y salir")
        Dia=int(input("Porfavor ingrese al dia de la semana '1-5' y coloque la informacion \n Si desea salir'6'"))

        if Dia== 1:
            print("Lunes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1=[Nombre,Temperatura]
            Todos1+=[Personas1]
            
        elif Dia== 2:
            print("Martes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas2=[Nombre,Temperatura]
            Todos2.append(Personas2)
            
        elif Dia== 3:
            print("Miercoles")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas3=[Nombre,Temperatura]
            Todos3.append(Personas3)
            
        elif Dia== 4:
            print("Jueves")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas4=[Nombre,Temperatura]
            Todos4.append(Personas4)
        elif Dia== 5:
            print("Viernes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas5=[Nombre,Temperatura]
            Todos5.append(Personas5)
            
        elif Dia== 6:
            print("-LUNES-")
            Personas1Max=()
            Personas1Min=()
            Promedio1=()
            for i in Todos1 :
                if i[1] >= i[1] :
                   Personas1Max =Todos1[i]
                if i[1] < i[1]:
                     Personas1Min =Todos1[i]
                     
                if i[1]>i[1] and  i[1]< i[1]:
                    Promedio1=Todos1[i]
                    
            print("El valor maximo es", Personas1Max)
            print("El valor minimo es", Personas1Min)
            print("El valor Promedio es", Promedio1)
            
                    
                    
                    









            
##            def mostrar_resultados(personas):
##                if personas:
##                    temperaturas = [p[1] for p in personas]
##                    promedio = sum(temperaturas) / len(temperaturas)
##                    max_temperatura = max(personas, key=lambda x: x[1])
##                    min_temperatura = min(personas, key=lambda x: x[1])
##
##                    print(f"  - Temperatura promedio: {round(promedio, 2)}")
##                    print(f"  - Temperatura máxima: {max_temperatura[1]} | {max_temperatura[0]}")
##                    print(f"  - Temperatura mínima: {min_temperatura[1]} | {min_temperatura[0]}")
##                else:
##                    print("  - No hay datos ingresados.")
##
##            print("Lunes:")
##            mostrar_resultados(Todos1)
##            print("Martes:")
##            mostrar_resultados(Todos2)
##            print("Miércoles:")
##            mostrar_resultados(Todos3)
##            print("Jueves:")
##            mostrar_resultados(Todos4)
##            print("Viernes:")
##            mostrar_resultados(Todos5)
        else:
            print("Respuesta incorrecta")

    
print("Muchas gracias, Adios")
