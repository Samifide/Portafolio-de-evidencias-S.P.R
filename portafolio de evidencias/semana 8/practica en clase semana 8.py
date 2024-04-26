#semana 8
#programacion basica
##pruebas
##samantha perez rojas
##clase viernes de 6-9pm

##Desarrolle un programa que convierta un número a su respectivo valor en base binaria,
##octal y hexadecimal.
##Cada una de las conversiones debe ser un proceso independiente.
##El proceso binario debe mostrar el resultado, los otros dos procesos deben retornar el
##resultado para ser mostrado desde el proceso inicial.
##Adicionalmente, programe un proceso que reciba dos parámetros (el valor y la base) y
##que muestre el número correspondiente

def binario(numero):
    numeronew=bin(numero)
    print( numeronew)


def octa(numero):
    listaocta=["0","1","2","3","4","5","6","7"]
    octal=""
    while numero>0:
        resto= numero%8
        octal=listaocta[resto] + octal
        numero=numero//8
    return octal


def hexa(numero):
    listahexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    hexadecimal=""
    while numero>0:
        resto= numero%16
        hexadecimal=listahexa[resto] + hexadecimal
        numero=numero//16
    return hexadecimal


numero=int(input("porfavor escriba un numero"))
binario(numero)
print("porfavor escriba un numero \n sera convertido a \n binario \n octal \n hexadecimal")
print("\n")
print("este es el codigo binario")
binario(numero)
print("\n este es el codigo octal")
print(octa(numero))
print("\n este es el codigo hexadecimal")
print(hexa(numero))
print("\n")
print("este nuevo codigo sera para mostrar el numero en formato \n binario \n octal \n hexadecimal \n dependiendo de la base que elija para convertir")
print("\n")
print("\n")
numero=int(input("porfavor escriba el  numero que va convertir"))
print("\n")
base=int(input("\n binario (2) \n octal (8) \n hexadecimal (16) \n porfavor escriba en numero la base a la que desea escribir: "))
if base==2:
    print(binario(numero))
elif base==8:
    print(octa(numero))
elif base==16:
    hexa(binario(numero))
else:
    print("escribio una opcion incorrecta")
