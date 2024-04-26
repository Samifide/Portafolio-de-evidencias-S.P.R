#Practica 1
##semana 4 Programacion basica
##fecha limite 17-2-2023
#Samantha Perez rojas

##Un usuario desea crear una calculadora de formas, en esta se puede calcular el área y el
##perímetro de la figura deseada, la calculadora puede gestionar, triángulos y cuadrados.
##Al iniciar, el programa solicita al usuario el tipo de figura que desea calcular, si el usuario digita
##C entonces la calculadora sabe que va a calcular un cuadrado, si digita T entonces será un
##triángulo. Ahora bien, dependiendo de la figura seleccionada, el programa debe solicitar las
##medidas de los lados y en el caso del tríangulo, la base y la altura. Considere que únicamente
##se calcularán para triángulos equilateros. Una vez indicada esta información, el programa
##realizará los cálculos respectivos y mostrará la información de area y perímetro.
##Algoritmo
##A) Analisis del problema: Calcular figuras pidiendo datos.
##    Analisar datos que se van a utilizar.
##B) Crear Pasos:
##    1-pedir informacion importante
##    2-analisar el tipo de respuesta 't' o 'c'
##    3- realizar operacion definida para esa opcion
##    4- dar resultados de las operaciones
##c)Realizar codigo

print("Saludos")
print("Dijite 'C' para calcular un cuadrado")
print("Dijite 'T' para calcular un Triangulo")
Figura=input("Porfavor escriba el tipo de figura que desea calcular: ")

if Figura=="C" or Figura=="c":
    Lado=int(input("Porfavor dijite el lado del Cuadrado: "))
    Area=Lado**2
    Perimetro=Lado*4
    print("Muchas gracias")
    print("El Area del Cuadrado es: ",Area)
    print("Y el Perimetro del Cuadrado es: ",Perimetro)
elif Figura=="T" or Figura=="t":
    Base=int(input("Porfavor dijite la Base del Triangulo: "))
    Altura=int(input("Porfavor dijite la Altura del Triangulo: "))
    Area=(Base*Altura)/2
    Perimetro=Base*3
    print("Muchas gracias")
    print("El Area del Triangulo es: ",Area)
    print("Y el Perimetro del Triangulo es: ",Perimetro)
    
else:
    print("Eso no esta entre las opciones")
    
