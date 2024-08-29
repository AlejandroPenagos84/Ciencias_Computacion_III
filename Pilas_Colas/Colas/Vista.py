from Tarea import Tarea

def menu():
    print("Que funcion desea realizar: "
          "\n[1] Agregar Tarea"
          "\n[2] Dar de alta Tareas"
          "\n[3] Eliminar"
          "\n[4] Mostrar"
          "\n[5] Salir")
    eleccion = int(input())

    return eleccion


def agregarTarea(colaTareas,colasAuxiliares):
    tareaAux = Tarea(input("Nombre de Tarea: "), int(input("Digite la duracion en segundos: ")))
    if not tareaAux:
        return
    # Como hay tarea entonces evaluaremos
    if colaTareas.esta_vacia():
        colaTareas.queue(tareaAux)
        tareaAux.iniciar_contador()  # Iniciamos el contador hasta que termine la tarea
    else:
        colasAuxiliares.queue(tareaAux)
        colasAuxiliares.sort(
            lambda t: t.duracion)  # organiza por duracion, y cuando se muestren las tareas, se mostrara cola auxiliares

def darDeAltaTarea(tareasCompletadas):
    #primero mostrara las tareas completadas:
    if tareasCompletadas.esta_vacia():
        print("No hay tareas Completadas")
        return
    darAlta = -1

    while darAlta !=1 :
        for t in tareasCompletadas.items:
            print("|____________________________________________________|")
            print(f"* Tarea: {t.nombre} \n* TR: {t.duracion}") #Hace referencia al tiempo restante y verifica si esta en 0, si no, hubo error
            print("|____________________________________________________|")

        darAlta = int(input("[0] Dar de Alta \n [1] Salir"))

        if darAlta == 0:
            tareasCompletadas.dequeue()

def eliminar():
    return

def mostrar(colaTareas,colasAuxiliares):

    if not colaTareas.esta_vacia():
        ct = colaTareas.top()
    if not colasAuxiliares.esta_vacia():
        print("|____________________________________________________|")
        print(f"* Tarea: {ct.nombre} \n* Duracion Actual: {ct.duracion}")
        print("|____________________________________________________|")
        for t in colasAuxiliares.items:
            print(f"* Tarea: {t.nombre} \n* Duracion Actual: {t.duracion}")
            print("|____________________________________________________|")