def crear_campers():
    #lista de inscritos
    campers =[] 
    #lista de campers aprobados
    camper_aprobados=[]
    print("Inscripcion de campers ")

    while True:
        # [1,2,3]
        # {1,2,3,2} = {1,2,3} conjunto - set([1,2,3])
        # {"nombre":"Carlos","edad":30} diccionario
        #creacion de nuevo usuario.
        id = input("Ingrese identificacion: ")
        apellido=input("Ingese los 2  apellidos: ")
        nombre=input("Ingrese todos los nombres: ")
        direccion=input("Ingrese direccion: ")
        acudiente=input("Ingrese el nombre completo del acudiente: ")
        celular=input("Ingrese el numero de celular: ")
        telefono=input("Ingrese numero de telefono: ")
        estado="inscrito"
        # id:input
        # nombre:input
        # direccion:input
        # acudiente:input
        # telefono:input
        # estado:input
        diccionaario = {
            "Identificacion" : id,
            "Apellido": apellido,
            "Nombre" : nombre,
            "Direccion" : direccion,
            "Acudiente" : acudiente,
            "Telefono" : telefono,
            "Celular" : celular,
            "Estado": estado
            }
        campers.append(diccionaario)
        print("Ingresar informacion de otro inscrito.")
        ingreso=-1
        ingreso = int(input("Si desea agregar otro camper escriba 1, si no, escriba 0: "))
        if ingreso==0:
            break
    return campers