import threading
import time

class Tarea:
    def __init__(self, nombre, duracion):
        self.thread = None
        self.nombre = nombre
        self.duracion = duracion
        self._running = True

    def __contador__(self):
        while self.duracion > 0 and self._running:
            time.sleep(1)
            self.duracion-=1

        if self.duracion == 0:
            self._running = False


    def iniciar_contador(self):
        self.thread = threading.Thread(target=self.__contador__)
        self.thread.start()