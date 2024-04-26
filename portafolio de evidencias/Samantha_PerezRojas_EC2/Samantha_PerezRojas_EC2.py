##prueva caso 2
##12-4-2024
##samantha perez rojas
##clase programacion basica
##Health Center
##El centro hospitalario de la ciudad tiene un problema con los sistemas de información, y necesitan
##desplegar la información de las citas para cada día. Esto es un problema que puede suceder en
##cualquier momento, por lo que tienen que crear una solución alterna que les permita suplir las
##necesidades referentes a la citas medicas y la información de los pacientes. Las funcionalidades
##principales son:
##● Activación de la jornada de citas: Requiere verificación local de la información, unicamente
##de los médicos jefes.
##○ Juan Romero, cedula 109858663
##○ Sofia Tames, cedula 30652745
##● Mostrar la información de las citas:
##○ Se debe leer la información de las citas referentes al día, esta información incluye:
##■ Fecha general.
##■ Hora de la cita.
##■ Nombre del paciente.
##■ Indicación de activado.
##○ El sistema debe ser capaz de agregar una cita con la información detallada
##anteriormente y además, se debe poder mostrar.


##○ Juan Romero, cedula 109858663
##○ Sofia Tames, cedula 30652745


registros_medicos=[]
Paciente=[]

def Registrar_paciente(completo,registros_medicos,fechas):
    print("Registro pacientes")
    dia=input("porfavor escriba el numero del dia en el que se va a dar la sita")
    mes=input("Porfavor Seleccione el mes en el que se va adar la cita \n 1-Enero \n 2-Febrebro \n 3-Marzo \n 4-Abril \n 5-Mayo \n 6-Junio \n 7-Julio \n 8-Agosto \n 9-Septiembre \n 10-Octubre \n 11-Noviembre \n 12-Diciembre" )
    Year=input("Porfavor escriba el año de la sita")
    fecha_completa=dia+"/"+mes+"/"+Year
    hora=input("Porfavor escriba las horas en las que se aplicara la sita")
    Nombre=input("Porfavor escriba el nombre del paciente")
    Apellido1=input("Porfavor escriba el Primer Apellido del paciente")
    Apellido2=input("Porfavor escriba el Segundo Apellido del paciente")
    nombre_completo=Nombre+" "+Apellido1+" "+Apellido2
    cita=True
    print("Su sita esta activada \n Informacion Correspondiente de la cita")
    print(nombre_completo," Tendra una cita medica el dia ",fecha_completa," a la hora ",hora," Con doctor ",completo)

    
    registros_medicos.append([fecha_completa,hora,Nombre,Apellido1,Apellido2,nombre_completo])

    Paciente=hora,nombre_completo
    for dia in range(len(fechas)):
        if fecha_completa==fechas[dia][0]:
            fechas[dia].append((Paciente,"Doctor:",completo,cita))
        else:
            fechas.append([fecha_completa,(Paciente,"Doctor:",completo,cita)])
    print(fechas)
    print(registros_medicos)


def Visualizar_Pacientes(fechas):
    print("Citas Por fecha")
    for i in range(len(fechas)):
        fechaRevicion=fechas[i]
        print("Fecha",fechaRevicion[0])
        for j in fechaRevicion:
            print(j)

doctores=[["Juan Romero",  109858663],["Sofia Tames", 30652745]]
print(doctores)

fechas=[["fechas","CITAS"]]
print(fechas)

while True:
    Abierto=True
    print("Saludos , este es el hospital Health Center \n")
    print("Porfavor ingrese su nombre para iniciar secion")
    nombre=input("Porfavor escriba su nombre Doctor o Doctora: ")
    apellido=input("Porfavor escriba su Apellido Doctor o Doctora: ")
    Cedula=int(input("Porfavor escriba su Cedula Doctor o Doctora: "))
    completo=(nombre+" "+apellido)
    print(completo)

    if (completo==doctores[0][0] and Cedula==doctores[0][1]) or (completo==doctores[1][0] and Cedula==doctores[1][1]):
        print("Bienvenido Doctor ", completo)
        while Abierto==True:
            decicion=input("Que accion desea realizar doctor? \n A-Registrar a un Paciente \n B-Ver los registros \n D-Salir del sistema temporalmente")
            decicion=decicion.upper()
            if decicion=="A":
                Registrar_paciente(completo,registros_medicos,fechas)
            elif decicion=="B":
                Visualizar_Pacientes(fechas)
            elif decicion=="C":
                print("Usted esta saliendo del sistema Doctor")
                Abierto=False
            else:
                print("Lolamaneto desicion no disponible")
            
    else:
        print("Lolamento Usted no es jefe medico")
        


    
