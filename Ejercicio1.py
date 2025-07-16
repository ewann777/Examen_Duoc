productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
             }

stock ={      '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }

def mostrarstockmarca():
    print("--------------------------------")
    print("--- BUSCANDO STOCK POR MARCA ---")
    print("--------------------------------")
    buscar = input("Ingresa marca a consultar: ")
    for producto, caracteristica1 in productos.items():
        if buscar == caracteristica1[0]:
            for modelo, caracteristica2 in stock.items():
                if producto in modelo:
                    print("--------------------------------")
                    print(f"El stock es: ", caracteristica2[1])
                    print("--------------------------------")

def mostrarporprecio():
    while True:
        try:
            minimo = int(input("Ingresa el precio mínimo: "))
            maximo = int(input("Ingresa el precio máximo: "))
            if maximo < minimo:
                print("El precio mínimo debe ser menor al máximo ")
            else:
                break
        except:
            print("Ingresa solo números ") 
    s = []

    for modelo, caracteristicas in stock.items():
        if caracteristicas[0] >= minimo and caracteristicas[0] <= maximo:
            for modelo2, caracteristicas in productos.items():
                if modelo == modelo2:
                    print(f"{caracteristicas[0]} - {modelo}")
def salir():
    print("Programa finalizado")

def listadodeproductos():
    print("----- Listado De Notebooks Ordenados --------")
    for producto, caracteristicas in productos.items():
        print(f"{caracteristicas[0]} -  {caracteristicas[5]} - {caracteristicas[4]} - {caracteristicas[2]} ")
    print("--------------------------------------------------")

def menu():
    while True:
        print("-*** MENÚ PRINCIPAL ***-")
        print("--- 1.- Stock Marca ---")
        print("--- 2.- Búsqueda Por Precio ---")
        print("--- 3.- Listado De Productos ---")
        print("--- 4.- Salir ---")
        print("Cambio de menú")
        try:
            opc = input("Ingrese una opción (1 a 4): ")
            break
        except:
            print("Ingresa una opción del 1 al 4")
    if opc == "1":
        mostrarstockmarca()
    elif opc == "2":
        mostrarporprecio()
    elif opc == "3":
        listadodeproductos()
    elif opc == "4":
        salir()
        print("Programa finalizado")
        exit()
    else:
        print("Debe seleccionar una opción válida!!")
menu()