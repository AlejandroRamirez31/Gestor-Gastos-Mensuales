print("---Menu De Control De Gastos--")
print("---1.Registrar gasto--")
print("---2.Mostar gastos registrados--")
print("---3.Calcular total de gastos--")
print("---4.Salir--")
opcion = input("Elige una opción 1-4.c ")

if opcion == "1":
    print("Resgistrando archivo...")
    descripcion = input("Describe en una palabra el gasto: ")
    monto = input("Agrega el monto: ")
    with open("Gasto_1.txt", "a", encoding="utf-8") as archivo:
        archivo.write(descripcion + "," + monto + "\n")
    print("Gasto registrado correctamente.")

elif opcion == "2":
    print("Gastos mensuales: ")
    with open("Gasto_1.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())

elif opcion == "3":
    print("Calculando gastos mensuales...")
    with open("Gasto_1.txt", "r", encoding="utf-8") as archivo:
        total = 0
        for linea in archivo:
            datos = linea.split(",")
            monto = float(datos[1])
            total += monto
    print("Este es el total de gastos: ", total)

