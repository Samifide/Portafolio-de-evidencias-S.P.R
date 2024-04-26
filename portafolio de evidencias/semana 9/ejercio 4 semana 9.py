#samantha perez rojas
##15-03-2024
##semana 9
##ejercicio 4
##Jimena es una joven que trabaja para pagarse sus estudios. Se ha 
##inscrito en una de las plataformas de entrega de comida y otros. 
##Haga un programa que le permita a Jimena registrar el monto ganado 
##en cada día, al finalizar la semana le mostrará el total y le indicará el día 
##que ganó menos dinero

i=0
monto_total=0
monto=0
montos=[]
dias=[]
completo=[]

while i!=7:
    i+=1
    print("monto ganado dia",i)
    monto=int(input("",))
    montos.append(monto)
    dias.append(i)
    completo+=[montos,dias]
    monto_total=monto_total+monto
    dia=i
    
menor=montos[0]
for numero in montos:
    if numero < menor:
        menor = numero


print("el monto total es: ",monto_total)
print(montos)
print("la menor cantidad de dinero fue de:",menor)
