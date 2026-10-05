#Crea un programa que permita guardar n cantidad de notas en un archivo, leer las notas, calcular el promedio, la nota más alta y la nota más baja.

while True:
    try:
        cantidad = int(input("¿Cuántas notas deseas guardar? "))
        if cantidad > 0:
            break
        print("Debes ingresar una cantidad mayor que cero.")
    except ValueError:
        print("Error ingresa un número entero.")

with open("notas.txt", "a+", encoding="utf-8") as archivo:
    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingresa la nota {i + 1}: "))
                break
            except ValueError:
                print("Error ingresa una nota con valor numérico.")
        archivo.write(f"{nota}\n")

print("Registro guardado.")

with open("notas.txt", "r", encoding="utf-8") as archivo:
    notas = [float(linea.strip()) for linea in archivo]

promedio = sum(notas) / len(notas)
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")