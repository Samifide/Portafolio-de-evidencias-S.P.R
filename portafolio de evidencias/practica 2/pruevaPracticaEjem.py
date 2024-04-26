Personas1=[]
Personas2=[]
Personas3=[]
Personas4=[]
Personas5=[]

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
        Dia=int(input("Porfavor ingrese al dia de la semana '1-5' y coloque la informacion \n Si desea salir'6'"))
        Personas1+=[(99, "th"), (68, "uj"), (64, "sk"),(23,"AA")]
        Personas2+=[(34, "th"), (54, "lo"), (90, "lo")]

        if Dia== 1:
            print("Lunes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1+=[(Temperatura,Nombre)]
            
        elif Dia== 2:
            print("Martes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1+=([Temperatura,Nombre])

            
        elif Dia== 3:
            print("Miercoles")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1+=([Temperatura,Nombre])
            
        elif Dia== 4:
            print("Jueves")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1+=([Temperatura,Nombre])

        if Dia== 5:
            print("Viernes")
            Nombre=input("Por favor escriba su nombre Completo")
            Temperatura=int(input("Por favor escriba su temperatura en grados"))
            Personas1+=([Temperatura,Nombre])
            
        if Dia== 6:
            
            print("Lunes:")
            print("Temperatura mínima:", min(Personas1))
            print("Temperatura máxima:", max(Personas1))

            print("Martes:")
            
            print("Martes:")

            
            print("Miércoles:")

            
            print("Jueves:")

            
            print("Viernes:")

            
        else:
            print("Respuesta incorrecta")

    
print("Muchas gracias, Adios")
