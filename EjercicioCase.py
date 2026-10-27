producto = ""
existencias = 0
verduras = 100
carnes = 90
frutas = 80
lacteos = 0
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