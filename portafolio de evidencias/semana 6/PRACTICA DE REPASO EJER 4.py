##Actividades semana 6
##clase de progrmacion
##23-2-2024

#Practica de repaso 1

print("Ejercicio 4")
##4. Desarrolle un programa que le solicita al usuario 15 salarios y que le indique cuánto 
##dinero se necesita para que a menos todos ganen $500.

completo=0
for i in range(15):
    Salario = int(input("Ingrese un valor del salario : "))
    if Salario  < 500:
        print("se nesesita",500-Salario,"Para que gane 500")
        
    completo+=Salario
Promedio=completo/15
print("Se nesesita ",Promedio," en promedio para que todos los empleados ganene 500")
