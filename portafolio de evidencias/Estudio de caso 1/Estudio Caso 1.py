##Samantha Perez Rojas
##clase programacion 1-3-2024
##viernes 6-9 pm
##primer caso de estudio

NumerosGanadores=[7,89,92,23]

semanas=0

personas=0

Perticipante=[]

numIngreso=0

Ganador=[]

DineroAcumulado=0

while semanas < 4:
    while personas  < 100:
        Nombre=input("Porfavor escriba su nombre completo: ")
        Cedula=int(input("Porfavor escriba su numero de cedula: "))
        print("selccione un monto: ")
        print("500")
        print("1000")
        print("2000")
        print("5000")
        Monto=int(input("porfavor escriba el monto que desea aportar: "))
        print("\n")
        numIngreso=numIngreso+1
        DineroAcumulado=DineroAcumulado+Monto
        Perticipante=[Nombre,Cedula,Monto,numIngreso]
        if Nombre and Cedula and Monto:
            numIngreso=numIngreso+1
            DineroAcumulado=DineroAcumulado+Monto
            Perticipante=[Nombre,Cedula,Monto,numIngreso]
            personas+=1
            for i in NumerosGanadores:
                if  numIngreso == i:
                      Ganador=Perticipante
        else:
            print("No ingreso datos correctamente")
        



    print("Eres el ganador")
    if Ganador[2] == 500:
        print(Ganador+ "Eres el ganador, \n Ganaste una hamburguesa con papas y Gaseosa.")
        
    elif Ganador[2] == 1000 :
        print(Ganador+ "Eres el ganador, \n Ganaste Cupon cena para 2 personas.")
        
    elif Ganador[2] == 2000 :
        print(Ganador+ "Eres el ganador, \n Un día en el parque de diversiones con transporte y comida pago para 3 personas")
        
    elif Ganador[2] == 5000:
        print(Ganador+ "Eres el ganador, \n Fin de semana todo incluido en hotel paradisiaco para 2 personas")
        
    print("La cantidad de dinero recaudada es de ",DineroAcumulado)
    semanas+=1
    
print("Ya se llego al final de las rifas")
                  
