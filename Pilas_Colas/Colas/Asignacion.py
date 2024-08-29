import sys
from Pilas_Colas.Estructuras_Datos import Cola
import threading
import time
from Vista import *

# lo primero a hacer es pedir las tareas
# Tendremos dos colas
colaTareas = Cola()
colaAuxiliar = Cola()  # Va a ser de tipo Cola()
tareasCompletadas = Cola()


def iniciarPrograma():
    while True:
        electionMenu = menu()  # ponemos el menu
        if electionMenu == 1:
            agregarTarea(colaTareas, colaAuxiliar)
        elif electionMenu == 2:
            darDeAltaTarea(tareasCompletadas)
        elif electionMenu == 3:
            eliminar()
        elif electionMenu == 4:
            mostrar(colaTareas, colaAuxiliar)
        elif electionMenu == 5:
            sys.exit()


def seguimientoTareas():
    while True:
        if colaTareas.esta_vacia():
            continue
        if colaTareas.top().duracion == 0 :
            tareasCompletadas.queue(colaTareas.dequeue())  # Metemos la primera
            if colaAuxiliar.esta_vacia():
                continue
            tAux = colaAuxiliar.dequeue()  # Igualamos al que quitamos
            colaTareas.queue(tAux)  # y lo ponemos aqui una vez que haya terminado
            tAux.iniciar_contador()
        else:
            time.sleep(colaTareas.top().duracion)  # Leemos la duracion y esperamos, y una vez esperado lo eliminamos:



hilo1 = threading.Thread(target=iniciarPrograma)
hilo2 = threading.Thread(target=seguimientoTareas)

hilo1.start()
hilo2.start()
