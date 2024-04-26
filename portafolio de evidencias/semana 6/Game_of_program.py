
cumple_enero = int(0)
cumple_febrero = int(0)
cumple_marzo = int(0)
cumple_abril= int(0)
cumple_mayo= int(0)
cumple_junio = int(0)
cumple_julio = int(0)
cumple_agosto = int(0)
cumple_septiembre = int(0)
cumple_octubre = int(0)
cumple_noviembre = int(0)
cumple_diciembre = int(0)
age_kid_total = int(0)


cantidad = input("Ingresa la cantidad de estudiantes para comparar los meses de cumple:")
cantidad = int(cantidad)

for x in range (cantidad):
    birthday_kid = input("Cual es el mes que cumple el estudiante:")
    age_kid = int(input("Cual es la edad del estudiante"))
    if birthday_kid.lower()=="enero":
        cumple_enero+=1
    elif birthday_kid.lower()=="febrero":
        cumple_febrero+=1
    elif birthday_kid.lower()=="marzo":
        cumple_marzo+=1
    elif birthday_kid.lower()=="abril":
        cumple_abril+=1
    elif birthday_kid.lower()=="mayo":
        cumple_mayo+=1
    elif birthday_kid.lower()=="junio":
        cumple_junio+=1
    elif birthday_kid.lower()=="julio":
        cumple_julio+=1
    elif birthday_kid.lower()=="agosto":
        cumple_agosto+=1
    elif birthday_kid.lower()=="septiembre":
        cumple_septiembre+=1
    elif birthday_kid.lower()=="octubre":
        cumple_octubre+=1
    elif birthday_kid.lower()=="noviembre":
        cumple_noviembre+=1
    elif birthday_kid.lower()=="diciembre":
        cumple_diciembre+=1
    age_kid_total=age_kid_total+age_kid

prom_edades = age_kid_total//cantidad
print("Hay un promedio de ",prom_edades)
print("Hay",cumple_enero, " que cumplen en enero")
print("Hay",cumple_febrero, " que cumplen en febrero")
print("Hay",cumple_marzo, " que cumplen en marzo")
print("Hay",cumple_abril, " que cumplen en abril")
print("Hay",cumple_mayo, " que cumplen en mayo")
print("Hay",cumple_junio, " que cumplen en junio")
print("Hay",cumple_julio, " que cumplen en julio")
print("Hay",cumple_agosto, " que cumplen en agosto")
print("Hay",cumple_septiembre, " que cumplen en septiembre")
print("Hay",cumple_octubre, " que cumplen en octubre")
print("Hay",cumple_noviembre, " que cumplen en noviembre")
print("Hay",cumple_diciembre, " que cumplen en diciembre")
