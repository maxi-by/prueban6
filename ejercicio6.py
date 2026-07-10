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
def buscar_codigo(codigo, expediente):
    for clave in expediente:
        if clave.upper() == codigo.upper():
            return True
    return False
def actualizar_costo(codigo, nuevo_costo, expediente):
    codigo = codigo.upper()
    if buscar_codigo(codigo, expediente):
        expediente[codigo][0] = nuevo_costo
        return True
    return False
def validar_codigo(codigo):
    if codigo.strip() != "":
        return True
    else:
        return False
def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False
def validar_especie(especie):
    if especie.strip() != "":
        return True
    else:
        return False
def validar_raza(raza):
    if raza.strip() != "":
        return True
    else:
        return False
def validar_edad(edad):
    if edad.strip() != "":
        return True
    else:
        return False
def validar_sexo(sexo):
    if sexo == "macho" or sexo == "hembra":
        return True
    else:
        return False
def validar_nombre_dueño(nombre_dueño):
    if nombre_dueño.strip() != "":
        return True
    else:
        return False
def validar_costo(costo):
    if costo > 0:
        return True
    else:
        return False
def validar_consultas(consultas):
    if consultas >= 0:
        return True
    else:
        return False
def agregar_paciente(codigo, nombre, especie, raza, edad, sexo, nombre_dueño, costo, consultas, expediente, pacientes):
    if buscar_codigo(codigo, expediente):
        return False
    else:
        pacientes[codigo.upper()] = [nombre, especie, raza, edad, sexo, nombre_dueño]
        expediente[codigo.upper()] = [costo, consultas]
        return True
def eliminar_paciente(codigo, expediente, pacientes):
    if buscar_codigo(codigo, expediente):
        pacientes.pop(codigo)
        expediente.pop(codigo)
        return True
    return False
