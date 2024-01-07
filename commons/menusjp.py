import os
def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')    


def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")


def menu_principal():
    limpiar_pantalla()
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Reportes")
    print("6. Salir")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_campers():
    limpiar_pantalla()
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Modificar campers")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    
def menu_trainers():
    limpiar_pantalla()
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas():
    limpiar_pantalla()
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriuclas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_aulas():
    limpiar_pantalla()
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Buscar Aulas")
    print("3. Modificar Aulas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_reportes():
    limpiar_pantalla()
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscripto")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op