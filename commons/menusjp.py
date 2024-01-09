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
    print("2. Prueba inicial")
    print("3. Trainers")
    print("4. Aulas")
    print("5. Rutas")
    print("6. Horarios")
    print("7. Matriculas")
    print("8. Filtros")
    print("9. Reportes")
    print("10. Salir")       
    op=validar_opcion("Opcion: ",1,10)
    return op
#op=1
def menu_campers():
    limpiar_pantalla()
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Modificar campers")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
#op=2
def menu_registro_prueba_inicial():
    limpiar_pantalla()
    print("------Registro preuba inicial--------")
    print("1.Ingresar registro")
    print("2.Salir")
    op=validar_opcion("Opcion:",1,2)
    return op
#op=3

def menu_trainers():
    limpiar_pantalla()
    print("----------- Menú Trainers-----------")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
#op=4
def menu_aulas():
    limpiar_pantalla()
    print("----------- Menú Aulas-----------")
    print("1. Crear Aulas")
    print("2. Buscar Aulas")
    print("3. Modificar Aulas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
#op=5
def menu_rutas():
    limpiar_pantalla()
    print("---------Menú Rutas------------")
    print("1.Crear Ruta")
    print("2.Ver rutas disponibles")
    print("3.Modificar rutas")
    print("4.Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
#op=6
def menu_horario():
    limpiar_pantalla()
    print("--------Menú Horarios--------")
    print("1.Crear horario")
    print("2.Mostrar Horarios disponibles")
    print("3.Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

#op=7
def menu_matriculas():
    limpiar_pantalla()
    print("----------- Menú Matriculas-----------")
    print("1. Crear Matriculas")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriuclas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
#op=8
def mennun_filtros():
    limpiar_pantalla()
    print("---------Menú Filtros----------")
    print("1.Crear filtro")
    print("2.Registrar filtro")
    print("3.Salir.")
#op=9
def menu_reportes():
    limpiar_pantalla()
    print("----------- Menú Reportes-----------")
    print("1. Listar campers estado inscripto")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op