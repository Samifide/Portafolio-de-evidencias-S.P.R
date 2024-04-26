#samantha perez rojas
##15-03-2024
##semana 9
##ejercicio 3

##Se requiere un programa que imprima una palabra al revés, debe 
##funcionar para cualquier palabra, por lo cual debe utilizar instrucciones 
##de lectura. En la solución utilice ciclos
i=-1
palabra=input("escriba una palabra porfavor:")
print("la alreves palabra es: ")
for e in range(len(palabra)):
    print(palabra[i:i-1:i])
    i=i-1
    
