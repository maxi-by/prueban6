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
pacientes = {
    'V001': ['Firulais', 'perro', 'labrador', 5, 'macho', 'Juan Perez'],
    'V002': ['Michi', 'gato', 'persa', 2, 'hembra', 'Ana Lopez'],
    'V003': ['Rocky', 'perro', 'bulldog', 8, 'macho', 'Carlos Ruiz'],
}
expediente = {
    'V001': [25000, 2],
    'V002': [15000, 1],
    'V003': [30000, 5],
}
def total_consultas(especie, pacientes, expediente):
    total = 0
    for clave in pacientes:
        if pacientes[clave][1].lower() == especie.lower():
            total += expediente[clave][1]
    print(f"El total de consultas realizadas es: {total}")
def busqueda_costo(c_min, c_max, pacientes, expediente):
    resultados = []
    for clave in expediente:
        costo = expediente[clave][0]
        consultas = expediente[clave][1]
        if (costo >= c_min and costo <= c_max and consultas > 0):
            producto = pacientes[clave][0] + "--" + clave
            resultados.append(producto)
    if len(resultados) == 0:
        print("No hay pacientes en ese rango de costos.")
    else:
        print("-- Pacientes encontrados --")
        resultados.sort()
        for producto in resultados:
            print(f"- {producto}")
