#semana 2 26-1-2023 intro progra
###ejercicio 1
##print("ejercicio 1") 
##A= input("ingrese el valor a ")
##B=input("ingrese el valor b ")
##C=input("ingrese el valor c ")
##D=input("ingrese el valor d ")
##
##print(D,C,B,A)
##
###ejercicio 2
##print("ejercicio 2")
##Edad= input("ingrese su edad actual ")
###este codigo "a=int(a)" permite convertir texto a numero
##Edad =int(Edad)
##Edad+=5
##
##print("la edad dentro de 5 años sera: ", Edad)

#ejercicio 3
##print("ejercicio 3")
##a=input("Escriba un dato A: ")
##a=int(a)
##b=input("Escriba un dato b: ")
##b=int(b)
##print (((a+b)*2)/3)

#ejercicio 4
##print("ejercicio 4")
##a=input("Escriba un dato A: ")
##a=int(a)
##AlCubo= a**3
##AlCuadrado= a**2
##print ("Resultado al cubo: ",AlCubo)
##print ("Resultado al cuadrado: ",AlCuadrado)
##
#ejercicio 5
##print("ejercicio 5")
##a=input("Escriba la base de un rectangulo: ")
##a=int(a)
##b=input("Escriba la altura de un rectangulo: ")
##b=int(b)
##area= a*b
##altura=(a*2)+(b*2)
##print("El area es",area )
##print("El perimetro es",altura )

#ejercicio 6
print("ejercicio 6")
##Desarrolle un programa que solicite la distancia de su casa a la
##Universidad, el costo por kilómetro, la cantidad de días a la semana que 
##viaja a la Universidad y que calcule el costo total de trasladarse por 
##cuatrimestre. Asuma que cada visite implica ida y vuelta y que el 
##cuatrimestre tiene 15 semanas.

##
##Distancia=input("Escriba cual es la distancia en kilometros de su casa a la universidad: ")
##Distancia=float(Distancia)
##kilometroPrecio=input("Escriba el precio en colones por kilometros que tiene que pagar: ")
##kilometroPrecio=int(kilometroPrecio)
##Dias=input("Ahora porfavor digite la cantidad de dias que se tiene que presentar al colegio: ")
##Dias=int(Dias)
##
##total=(((Distancia*kilometroPrecio)*2)*Dias)*15
##print("Muchas gracias")
##print("Este es el total de gastos por cuatrimestre: ",total)
##

#ejercicio 7
##print("ejercicio 7")
##Desarrolle un programa que solicite al usuario la 
##edad de 5 personas y le muestre cuál es la edad promedio
##Persona1=input("Porfavor dijite la edad de la primera persona: ")
##Persona1=int(Persona1)
##Persona2=input("Porfavor dijite la edad de la segunda persona: ")
##Persona2=int(Persona2)
##Persona3=input("Porfavor dijite la edad de la tercera persona: ")
##Persona3=int(Persona3)
##Persona4=input("Porfavor dijite la edad de la cuarta persona: ")
##Persona4=int(Persona4)
##Persona5=input("Porfavor dijite la edad de la quinta persona: ")
##Persona5=int(Persona5)
##print("muchas gracias")
##edad=(Persona1+Persona2+Persona3+Persona4+Persona5)/5
##print("la edad promedio es: ", edad)

#ejercicio 8
print("ejercicio 8")
##8. Desarrolle un programa que solicite al usuario la cantidad de horas 
##semanales trabajadas, el precio que se le paga por hora y que calcule el 
##salario mensual. Considere que se debe aplicar una deducción del 10.5% 
##por cargas sociales y 5% por asociación solidarista. Asuma que cada mes 
##cuenta con 4.2 semanas.


##horasSemanales=input("Profavor dijite la cantidad de horas semanales trabjadas: ")
##horasSemanales=int(horasSemanales)
##PagoxHora=input("porfavor dijite el pago por hora: ")
##PagoxHora=int(PagoxHora)
##Mes=4.2
##SalarioCompleto=(horasSemanales*PagoxHora)*Mes
##SalrioFinal=SalarioCompleto*(0.105+0.05)
##print("Su salario mensual final aplicando descuentos es de: ",SalrioFinal)

#ejercicio 9
print("ejercicio 9")
##Desarrolle un programa que le solicite al usuario sus ingresos y sus gastos 
##mensuales por alimentación. Con esta información el programa debe 
##mostrar el porcentaje que gasto que corresponde al rubro de alimentación 
##y el porcentaje que queda disponible para otros rubros.
Ingresos=input("Digite porfavor sus ingresos mensuales:")
Ingresos=int(Ingresos)
Gastos=input("Porfavor dijite cuantos son sus gatos en comida: ")
Gastos=int(Gastos)
GatosP=(Gastos/Ingresos)*100
IngresosP=100-GatosP
print("Su porcentaje de Gastos es de: ",GatosP,"%")
print("Su porcentaje de Dinero restante es de: ",IngresosP,"%")
