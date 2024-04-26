##Camila Argeñal Coronado
##Eduardo miranda mora
##Jordan Ivan Soto Morales
##Josias Aguilar Arroyo
##Samantha Perez Rojas
##clase d eprgrmacion viernes 6-9
##semana 12
##5-4-2024
##fecha limite 7/4/2024

def crearArchivo():
    file = open("ventas.txt", "w")
    print("El archivo está listo")
    file.close()

def agregar():
    with open("ventas.txt", "a") as file:
        for _ in range(3):
            nombre_vendedor = input("Ingrese el nombre del vendedor: ")
            monto_venta = input("Ingrese el monto de la venta en dólares: ")
            file.write(f"{nombre_vendedor},{monto_venta}\n")
    print("Los datos de las ventas han sido agregados correctamente al archivo.")

def mostrar():  
    file = open("ventas.txt", "r")
    mensaje = file.read()
    print(mensaje)
    file.close()

def menu_acciones():
    print("\nMenú:")
    print("1. Agregar")
    print("2. Mostrar")


    
    
while True:
    menu_acciones()
    opc = input("Seleccione una opción: ")

    if opc == "1":
        agregar()
    elif opc == "2":
        mostrar()
