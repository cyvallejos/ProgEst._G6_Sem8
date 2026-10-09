def main():
    estudiantes = []

    while True:
        try:
            cantidad = int(input("Cuantos estudiantes desea ingresar? "))
            if cantidad > 0:
                break
            print("Ingrese una cantidad mayor que cero.")
        except ValueError:
            print("Ingrese un numero entero valido.")

    for numero in range(cantidad):
        print(f"\nEstudiante {numero + 1}:")
        nombres = input("Nombres: ").strip()
        apellidos = input("Apellidos: ").strip()

        while True:
            try:
                nota = float(input("Nota: ").replace(",", "."))
                break
            except ValueError:
                print("Ingrese una nota numerica valida.")

        estudiante = {
            "nombres": nombres,
            "apellidos": apellidos,
            "nota": nota,
        }
        estudiantes.append(estudiante)

    suma_notas = 0
    estudiante_mayor = estudiantes[0]
    estudiante_menor = estudiantes[0]

    for estudiante in estudiantes:
        suma_notas += estudiante["nota"]
        if estudiante["nota"] > estudiante_mayor["nota"]:
            estudiante_mayor = estudiante
        if estudiante["nota"] < estudiante_menor["nota"]:
            estudiante_menor = estudiante

    promedio = suma_notas / len(estudiantes)

    estudiantes_pendientes = estudiantes.copy()
    mejores_estudiantes = []
    cantidad_mejores = len(estudiantes_pendientes)
    if cantidad_mejores > 3:
        cantidad_mejores = 3

    for _ in range(cantidad_mejores):
        indice_mayor = 0
        for indice in range(1, len(estudiantes_pendientes)):
            if (
                estudiantes_pendientes[indice]["nota"]
                > estudiantes_pendientes[indice_mayor]["nota"]
            ):
                indice_mayor = indice
        mejores_estudiantes.append(estudiantes_pendientes.pop(indice_mayor))

    print(f"\nPromedio de notas: {promedio:.2f}")
    print(
        f"Nota mas alta: {estudiante_mayor['nota']:.2f} - "
        f"{estudiante_mayor['nombres']} {estudiante_mayor['apellidos']}"
    )
    print(
        f"Nota mas baja: {estudiante_menor['nota']:.2f} - "
        f"{estudiante_menor['nombres']} {estudiante_menor['apellidos']}"
    )

    print("\nLos 3 estudiantes con mayor nota:")
    for posicion, estudiante in enumerate(mejores_estudiantes, start=1):
        print(
            f"{posicion}. {estudiante['nombres']} {estudiante['apellidos']}: "
            f"{estudiante['nota']:.2f}"
        )

if __name__ == "__main__":
    main()