#Leer los nombres, apellidos, edad y carrera de un estudiante
#guardo en un archivo llamado estudiante.txt
nombre = input("Dime tus nombres: ")
apellidos = input("Dime tus apellidos: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu carrera: ")

datos = f"Nombre: {nombre.title()}\nApellidos: {apellidos.title()}\nEdad: {edad}\nCarrera: {carrera.title()}"

with open("estudiante.txt", "a+", encoding="utf-8") as archivo:
    archivo.write(datos)
    
print("Archivo creado satisfactoriamente.")