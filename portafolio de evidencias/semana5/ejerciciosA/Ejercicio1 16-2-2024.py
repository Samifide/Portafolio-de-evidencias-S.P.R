##Ejercicios 16-2-2024
##calse 5
##Programacion Basica

##ejercicio 1
##• Una fábrica de galletas nos ha solicitado que desarrollemos un programa que 
##calcule la suma total de los salarios de sus 10 colaboradores.
##Tome en cuenta que en cada salario se deberá deducir el 9% de cargas sociales.
##Al final muestre el total pagado por la empresa por concepto de salarios.
##
range(11)

#nota:se tiene que iniciar afuera para poder usarlas adentro y guardar informacion
sumaSalario=0
SalarioConPorcentaje=0
for i in range(1,11):
    print(i)
    Salario=int(input("Porfavor escriba el salario del empleador:"))
    SalarioConPorcentaje=Salario*0.9
    sumaSalario+=Salario
print("Los salarios sumados da un total de: ",sumaSalario)
print("Aplicado el porcentaje es",SalarioConPorcentaje)
print("Muchas gracias")
#nota:
