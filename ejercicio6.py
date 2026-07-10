def mostrar_menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Consultas totales por especie
2. Búsqueda de pacientes por rango de costo
3. Actualizar costo de atención
4. Registrar nueva mascota
5. Eliminar registro de mascota
6. Salir
====================================""")
def leer_opcion():
    while True:
        try:
            opc = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: La opcion debe ser un numero entero")
        else:
            if opc >= 1 and opc <= 6:
                return opc
            else:
                print("Error: La opcion ingresada debe estar entre 1-6")
