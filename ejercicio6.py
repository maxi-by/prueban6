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
    if edad > 0:
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
def main():
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
    while True:
        mostrar_menu()
        opc = leer_opcion()
        match opc:
            case 1:
                especie = input("Ingrese el nombre de la especie: ")
                total_consultas(especie, pacientes, expediente)
            case 2:
                try:
                    c_min = int(input("Ingrese el costo minimo: "))
                    c_max = int(input("Ingrese el costo maximo: "))
                    busqueda_costo(c_min, c_max, pacientes, expediente)
                except ValueError:
                    print("Debe ingresar valores enteros")
            case 3:
                while True:
                    codigo = input("Ingrese el codigo de la mascota: ")
                    try:
                        costo = int(input("Ingrese el nuevo costo: "))
                        if actualizar_costo(codigo, costo, expediente):
                            print("Costo actualizado")
                        else:
                            print("El código no existe")
                    except ValueError:
                        print("Error: Debe ingresar un numero entero")
                    continuar = input("¿Desea actualizar otro costo (s/n)?: ")
                    if continuar != "s":
                        break
            case 4:
                codigo = input("Ingrese el codigo de la mascota: ")
                if not validar_codigo(codigo) or buscar_codigo(codigo, expediente):
                    print("Error: Debe ingresar el codigo de la mascota o este mismo ya existe")
                    continue
                nombre = input("Ingrese el nombre de la mascota: ")
                if not validar_nombre(nombre):
                    print("Error: Debe ingrasar el nombre de la mascota")
                    continue
                especie = input("Ingrese la especie de la mascota: ")
                if not validar_especie(especie):
                    print("Error: Debe ingresar la especie de la mascota")
                    continue
                raza = input("Ingresa la raza de la mascota: ")
                if not validar_raza(raza):
                    print("Error: debe ingresar la raza de la mascota")
                    continue
                try:
                    edad = int(input("Ingrese la edad de la mascota: "))
                    if not validar_edad(edad):
                        print("Error: Debe ingresar la edad de la mascota")
                        continue
                except ValueError:
                    print("Error: la edad debe ser un numero entero")
                    continue
                sexo = input("Ingrese el sexo de la mascota: ")
                if not validar_sexo(sexo):
                    print("Error: Debe ingresar si su mascota es macho o hembra ")
                    continue
                nombre_dueño = input("Ingrese el nombre del dueño: ")
                if not validar_nombre_dueño(nombre_dueño):
                    print("Error: Debe ingresar el nombre del dueño")
                    continue
                try:
                    costo = int(input("Ingrese el costo de antencion: "))
                    consultas = int(input("Ingrese numero de consultas: "))
                    if not validar_costo(costo):
                        print("Error: Debe ingresar un costo mayor a 0")
                        continue
                    if not validar_consultas(consultas):
                        print("Error: Debe ingresar un numero mayor o igual 0")
                        continue
                    agregar_paciente(codigo, nombre, especie, raza, edad, sexo, nombre_dueño, costo, consultas, expediente, pacientes)
                    print("Mascota registrada")
                except ValueError:
                    print("Error: El costo debe ser mayor a 0 y la consulta debe ser mayor o igual a 0")
            case 5:
                codigo = input("Ingrese el codigo de la mascota: ")
                if eliminar_paciente(codigo, expediente, pacientes):
                    print("Registro eliminado")
                else:
                    print("El código no existe")
            case 6:
                print("Programa finalizado.")
                break
main()
