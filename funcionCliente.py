# Bryan Angulo
# Menu del cleinte

def menuCliente():
    seleccion = []
    while True:
        print(f"\n----------------- Menu Cliente -----------------\n")
        print("1. Ver mapa de lugares turísticos conectados")
        print("2. Consultar la ruta óptima entre dos ciudades")
        print("3. Explorar lugares")
        print("4. Seleccionar ciudades a visitar")
        print("5. Listar la o las  ciudades seleccionadas")
        print("6. Actualizar la o las ciudades  seleccionadas")
        print("7. Eliminar la o las ciudades seleccionadas")
        print("8. Guardar selección de ciudades")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            verMapa()
        elif opcion == "2":
            consultarRutaOptima()
        elif opcion == "3":
            explorarLugares()
        elif opcion == "4":
            seleccionarCiudades(seleccion)
        elif opcion == "5":
            listarSeleccion(seleccion)
        elif opcion == "6":
            actualizarCiudadSeleccion(seleccion)
        elif opcion == "7":
            eliminarCiudadSeleccion(seleccion)
        elif opcion == "8":
            guardarSeleccion(seleccion)
        elif opcion == "0":
            print("\nSaliendo del menu cliente....")
            break
        else:
            print("\nOpción no válida")

def verMapa():
    # Ver mapa de lugares turísticos conectados.
    #Cargar desde archivo "rutas.txt".
    print("\nMapa de lugares turísticos conectados")

def consultarRutaOptima():
    #Consultar la ruta óptima entre dos ciudades/puntos turísticos y el costo. 
    # Busque mediante un algoritmo de búsqueda (Lineal, Binaria, Interpolación etc.).
    #Pedir lugar de origen y lugar de destino.
    print("\nRuta óptima entre dos ciudades")

def explorarLugares():
    #Explorar lugares: organizados jerárquicamente por zonas. (árbol).
    print("\nExplorar lugares")

def seleccionarCiudades(seleccion):
    #Seleccionar ciudades/puntos turísticos a visitar. 
    #Pedir lugar de origen y lugar de destino.
    #(mínimo dos)
    print("\nSeleccionar ciudades a visitar")

def listarSeleccion(seleccion): 
    # Listar la o las ciudades y el costo total(seleccionadas?). 
    # (Ordenar las ciudades /puntos turísticos en base a un algoritmo de ordenamiento 
    # (Burbuja, Inserción, Selección, MergeSort, QuickSort, etc.). 
    print("\nLista de ciudades seleccionadas")  

def actualizarCiudadSeleccion(seleccion):
    # Actualizar la o las ciudades /puntos turísticos (seleccionadas?). 
    print("\nActualizar ciudades seleccionadas ")        

def eliminarCiudadSeleccion(seleccion):
    # Eliminar la o las ciudades /puntos turísticos (seleccionadas?). 
    print("\nEliminar ciudades seleccionadas")   

def guardarSeleccion( seleccion):
    #-	Guadar la selección de ciudades/puntos turísticos 
    # en un archivo “rutas-nombre-del-cliente.txt”
    print("\nGuardar seleccion en archivo")   


menuCliente()