Num_Vehiculo = []
opc = 0
while opc !=1:
    print()
    print("-----Menu-----")
    print("[1] Gestion inventario Vehiculos")
    print("[2] Gestion de clientes")
    print("[3] visualizar vehiculos ")
    opc = input("Seleccione una opcion: ")
    if opc == "1":
        print("----Gestion inventario vehiculos---")
        print("[1] Agregar vehiculos")
        print("[2] inhabilitar vehiculos")
    opc = input("Seleccione una opcion: ")
    if opc == "1":
        print()
        print("Agrega el vehiculo que deseas")
        Marca = input("Ingrese la marca del vehiculo: ")
        Año = input("Ingrese el año del vehiculo:")
        Modelo = input("Ingrese el modelo del vehiculo:")
        cilindraje = input("Ingrese el cilindraje del modelo: ")
        Precio_alquiler =float(input("Ingrese el precio de al alquiler: "))
        Precio_auto = float(input("Ingrese el precio del auto: "))
        placa = input("Ingrese el numero de placa")


        Num_Vehiculo = [Marca,Año,Modelo,cilindraje,Precio_alquiler,Precio_auto]
        
        print(Num_Vehiculo)
        print("Vehiculo agregado con exito ")
    if opc == "2":
        print("Inhabilitar vehiculos")
        print("----Menu-----")
        print("[1] Vehiculo dañado ")
        print("[2]Vehiculo reservado")