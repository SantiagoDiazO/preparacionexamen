opcion = 100
empanadas = []

print("***EMPANADAS EL MACHETICO***")
print("1: Registrar empanada")
print("2: Mostrar empanada")
print("3: Buscar empanada")
print("4: Editar empanada")
print("2: Eliminar empanada")
print("0: Salir")

while opcion != 0:
    opcion = int(input("Ingrese la opcion deseada: "))
    if opcion == 1:
        #Agregando una empanada al arreglo de empanadas
        empanada = {}
        empanada["id"] = int(input("Digita el codigo de la empanada: "))
        empanada["nombre"] = input("Digita el nombre de la empanada: ")
        empanada["precio"] = float(input("Digite el precio de la empanada: "))
        empanada["fechaFabricacion"] = input("Digite la fecha de fabricacion: ")
        empanada["popularidad"] = int(input("Digite la popularidad de la empanada: "))
        empanadas.append(empanada)
    elif opcion == 2:
        print(empanadas)
    elif opcion == 3:
        empanadaABuscar = int(input("Digite el codigo de la empanada a buscar: "))
        for empanadaSeleccionada in empanadas:
            if empanadaSeleccionada["id"] == empanadaABuscar:
                print(empanada)
            else:
                print("No se encontro la empanada")
    elif opcion == 4:
        empanadaABuscar = int(input("Digite el codigo de la empanada a buscar: "))
        for empanadaSeleccionada in empanadas:
            if empanadaSeleccionada["id"] == empanadaABuscar:
                empanadaSeleccionada["precio"] = float(input("Digite el nuevo precio: "))
            else:
                print("No se encontro la empanada")
    elif opcion == 5:
        empanadaABuscar = int(input("Digite el codigo de la empanada a buscar: "))
        for empanadaSeleccionada in empanadas:
            if empanadaSeleccionada["id"] == empanadaABuscar:
                pass
            else:
                print("No se encontro la empanada")
    elif opcion == 0:
        print("Gracias")
    else:
        print("***Digita una opcion valida***")