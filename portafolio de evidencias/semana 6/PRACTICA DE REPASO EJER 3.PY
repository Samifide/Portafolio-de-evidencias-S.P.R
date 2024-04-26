##Actividades semana 6
##clase de progrmacion
##23-2-2024

#Practica de repaso 1
print("Ejercicio 3")

##3. Desarrollar un programa que le solicite al usuario un valor y muestre los primeros 
##10 números divisibles entre este valor. 
Num=int(input("Porfavor digite un numero: "))
A=0
i=0
while A < 10:
    i+=1
    if Num % i==0 :
        print(i,"es divisible entre ",Num)
        A+=1
