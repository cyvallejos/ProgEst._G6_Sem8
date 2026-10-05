##Leer un archivo llamado datos.txt
archivo = open("datos.txt", "r", encoding="utf-8")
print(archivo.read())
archivo.close()