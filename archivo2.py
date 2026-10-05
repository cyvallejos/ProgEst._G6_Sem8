#Leer un archivo "misdatos.txt" usando with
with open("misdatos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    
print(contenido)