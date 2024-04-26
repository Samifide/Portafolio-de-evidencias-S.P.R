#clase 3
##2-2-2024
##clase de progrmacion :ejemplos y ejercicios.

#ejercicio 1
Nombre=input("Porfavor escriba su nombre: ")
ApellidoA=input("Dajiste su Primer apellido: ")
ApellidoB=input("Dajiste su Segundo apellido: ")
print("Bienvenido estimado(a)",Nombre,"",ApellidoA,"",ApellidoB)
##
##ejercicio 2
##
##Vamos a crear una especie de calculadora simple! 
####El programa calculará el de la suma, la resta, la multiplicación y la 
####división de dos números y mostrará los resultados obtenidos.
print("si un numero es cero '0' probablemnte de error")
NumA=input("Porfavor dijiste el Primer dijiste a calcular: ")
Numb=input("Porfavor dijiste el Segundo dijiste a calcular: ")
NumA=int(NumA)
Numb=int(Numb)
suma=NumA+Numb
Resta=NumA-Numb
Div=NumA/Numb
Multi=NumA*Numb
print("los resultados son...")
print("Multiplicacion")
print(NumA,"x",Numb,"=",Multi)
print("Divicion")
print(NumA,"/",Numb,"=",Div)
print("Suma")
print(NumA,"+",Numb,"=",suma)
print("Resta")
print(NumA,"-",Numb,"=",Resta)

#ejercicio 3
#Elabore un programa que calcule y muestre el área y el perímetro de un 
##cuadrado.

Lado=input("Profavor dijiste el largo del lado: ")
Lado=int(Lado)
Perimetro=Lado+Lado+Lado+Lado
Area=Lado*Lado
print("el Perimetro es en total:",Perimetro)
print("el Area es en total:",Area)

#ejercicio 4
##Desarrolle un programa intercambie el valor de las edades de Luis y 
##Pedro y muestre las edades luego de realizado el intercambio.

Luis=input("Luis porfavor dijite su edad: ")
Pedro=input("Pedro porfavor dijite su edad: ")
Extra=Luis
Luis=Pedro
Pedro=Extra
##
print("La edad de Luis es",Luis)
print("La edad de pedro es",Pedro)


#ejrcicio 5·
#Desarrolle un programa que eleve un número a una potencia.
Exponente=input("escriba el numero que sera exponente: ")
Exponente=int(Exponente)
NumeroBase=input("Escriba el numero que sera la base: ")
NumeroBase=int(NumeroBase)
Resul=NumeroBase**Exponente
print("",Exponente)
print(NumeroBase)
print("El resultado es ", Resul)





