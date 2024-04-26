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

Personas1=[]
Personas2=[]
Personas3=[]
Personas4=[]
Personas5=[]
TemperaturasJuntas1=0
TemperaturasJuntas2=0
TemperaturasJuntas3=0
TemperaturasJuntas4=0
TemperaturasJuntas5=0
while True:
    
    Aceptacion=input("Deseas Ver el menu de opciones o salir, Salir='No', menu='Si'?")

    if Aceptacion.lower()=="no" or Aceptacion.lower()=="n":

        break
    
    else:
        print("[1] Lunes")
        print("[2] Martes")
        print("[3] Miercoles")
        print("[4] Jueves")
        print("[5] Viernes")
        print("[6] Mostrar resultados y salir")
        Dia=int(input("Porfavor ingrese al dia de la semana '1-5' \n y coloque la informacion \n Si desea salir'6'"))

        if Dia== 1:
            print("Lunes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1+=[(Temperatura,Nombre)]
            TemperaturasJuntas1+=Temperatura
            
        elif Dia== 2:
            print("Martes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas2+=[(Temperatura,Nombre)]
            TemperaturasJuntas2+=Temperatura

            
        elif Dia== 3:
            print("Miercoles")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas3+=[(Temperatura,Nombre)]
            TemperaturasJuntas3=+Temperatura
            
        elif Dia== 4:
            print("Jueves")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas4+=[(Temperatura,Nombre)]
            TemperaturasJuntas4=+Temperatura
            
        elif Dia== 5:
            print("Viernes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas5+=[(Temperatura,Nombre)]
            TemperaturasJuntas5=+Temperatura
        elif Dia== 6:
            print("\n")
            print("Lunes:")
            if Personas1:
                
                Minimo1=min (Personas1)
                Maximo1=max (Personas1)
                
                Promedio1=TemperaturasJuntas1/  len (Personas1)
                
                print("Temperatura Promedio es:",Promedio1 )
                print("Temperatura máxima:",Maximo1[1],"|", Maximo1[0] )
                print("Temperatura Minima:",Minimo1[1],"|", Minimo1[0] )
            else:
                print ("no se encuentra nada en este dia")
        

            print("\n")
            print("Martes:")
            if Personas2:
            
                Minimo2=min (Personas2)
                Maximo2=max (Personas2)
                
                Promedio2=TemperaturasJuntas2/  len (Personas2)
                
                print("Temperatura Promedio es:",Promedio2 )
                print("Temperatura máxima:",Maximo2[1],"|", Maximo2[0] )
                print("Temperatura Minima:",Minimo2[1],"|", Minimo2[0] )
            else:
                print ("no se encuentra nada en este dia")  

            print("\n")
            print("Miércoles:")
            if Personas3:
                
                Minimo3=min (Personas3)
                Maximo3=max (Personas3)
                
                Promedio3=TemperaturasJuntas3/  len (Personas3)
                
                print("Temperatura Promedio es:",Promedio3 )
                print("Temperatura máxima:",Maximo3[1],"|", Maximo3[0] )
                print("Temperatura Minima:",Minimo3[1],"|", Minimo3[0] )
            else:
                print ("no se encuentra nada en este dia")
                
            print("\n")
            print("Jueves:")
            if Personas4:
     
                Minimo4=min (Personas4)
                Maximo4=max (Personas4)
                
                Promedio4=TemperaturasJuntas4/  len (Personas4)
                
                print("Temperatura Promedio es:",Promedio4 )
                print("Temperatura máxima:",Maximo4[1],"|", Maximo4[0] )
                print("Temperatura Minima:",Minimo4[1],"|", Minimo4[0] )
            else:
                print ("no se encuentra nada en este dia")                            

            print("\n")
            print("Viernes:")
            if Personas4:            
                Minimo5=min (Personas5)
                Maximo5=max (Personas5)
                
                Promedio5=TemperaturasJuntas5/  len (Personas5)
                
                print("Temperatura Promedio es:",Promedio5 )
                print("Temperatura máxima:",Maximo5[1],"|", Maximo5[0] )
                print("Temperatura Minima:",Minimo5[1],"|", Minimo5[0] )
            else:
                print ("no se encuentra nada en este dia")                            
                
            
        else:
            print("Respuesta incorrecta")


print("Hasta luego")
print("Muchas gracias")

