producto = ""
existencias = ""
verduras = ""
carnes = ""
frutas = ""
lacteos = ""
opcion = 0

print("Bienvenido al inventario de productos")
print("----------MENU DE OPCIONES----------")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Modificar existencias")
print("4. Mostrar inventario")
print("5. Salir")
opcion = int(input("Ingrese la opcion que desea realizar: "))
match opcion:
    case 1:
        producto = input("Ingrese el nombre del producto: ")
        existencias = int(input("Ingrese la cantidad de existencias: "))
        print("Producto agregado con exito")
    case 2:
        producto = input("Ingrese el nombre del producto a eliminar: ")
        print("Producto eliminado con exito")
    case 3:
        producto = input("Ingrese el nombre del producto a modificar: ")
        existencias = int(input("Ingrese la nueva cantidad de existencias: "))
        print("Existencias modificadas con exito")
    case 4:
        print("Inventario de productos:")
        print(f"Verduras: {verduras}")
        print(f"Carnes: {carnes}")
        print(f"Frutas: {frutas}")
        print(f"Lacteos: {lacteos}")
    case 5:
        print("Gracias por usar el inventario de productos")   
    case _:
        print("opcion no valida, por favor ingrese una opcion del 1 al 5")