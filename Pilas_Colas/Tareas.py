from Estructuras_Datos import Cola

class Tareas:
    def __init__(self, nombre,beneficio,plazo):
        self.nombreTarea = nombre
        self.plazo = plazo
        self.beneficio =beneficio

    def getBeneficio(self):
        return self.beneficio
    def getNombreTarea(self):
        return self.nombreTarea
    def getPlazo(self):
        return self.plazo
    def toString(self):
        return "["+self.nombreTarea+" , "+str(self.plazo)+" , "+str(self.beneficio)+"]"




def tareasPrediseñadas():
    tarea1 = Tareas("tarea1",10,3)
    tarea2 = Tareas("tarea2",15,4)
    tarea3 = Tareas("tarea3",20,1)
    tarea4 = Tareas("tarea4",5,1)
    tarea5 = Tareas("tarea5",1,2)
    return [tarea1,tarea2,tarea3,tarea4,tarea5]