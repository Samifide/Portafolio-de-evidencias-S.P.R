##Ejercicios 16-2-2024
##calse 5
##Programacion Basica

##ejercicio 2
##Desarrolle un programa que calcule y muestre la suma de
##los números pares 
##contenidos en 10 valores enteros ingresados por el usuario

NumerosPares=0
range(11)
for i in range(1,10):
    print(i)
    Num=int(input("Porfavor dijite un numero"))
    if Num%2==0:
        NumerosPares+=Num
print("la cantidad completa de numeros pares es: ",NumerosPares)
