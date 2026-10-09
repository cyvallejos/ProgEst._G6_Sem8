listas = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "hola"]
print(listas)

conjuntos = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "hola"]
print(conjuntos)

tuplas = (1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "hola")
print(tuplas)

diccionarios = {"estudiante": "Juanito", "sexo": "Hombre", "Nota": 85}
print(diccionarios)
diccionarios["Nota"]=80
print(diccionarios)


nuevaLista = []
nuevaLista.append(listas)
nuevaLista.append(conjuntos)
nuevaLista.append(tuplas)
nuevaLista.append(diccionarios)
print(nuevaLista)

for item in nuevaLista:
    print(item)

for item in nuevaLista:
    print(type(nuevaLista))

with open("texto.txt", "+w", encoding="utf-8") as archivo:
    for item in nuevaLista:
        archivo.write(str(item) + "\n")

