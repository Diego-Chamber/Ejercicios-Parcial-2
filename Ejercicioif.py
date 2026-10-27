nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese tu nombre: ")
edad = int(input("Ingrese tu edad: "))
nacionalidad = input("Ingrese tu nacionalidad: ")

if edad >= 18:# el if va seguido de la condicion y dos puntos
    print("Eres mayor de edad")
else:# else va seguido de dos puntos para decir que se have si no se cumpla la condicion de if
    print("No eres mayor de edad")

if nacionalidad == "N":
    print("Eres de nacionalidad mexicana")
else:
    print("No eres de nacionalidad mexicana")