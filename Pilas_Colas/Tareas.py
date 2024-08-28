class Tareas:
    def __init__(self, nombre, plazo, duracion):
        self.nombreTarea = nombre
        self.plazo = plazo
        self.beneficio =duracion

    def getDuracion(self):
        return self.duracion
    def getNombreTarea(self):
        return self.nombreTarea
    def getPlazo(self):
        return self.plazo
