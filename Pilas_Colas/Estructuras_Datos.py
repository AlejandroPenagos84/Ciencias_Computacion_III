'''
Esta es la forma normalita de hacerlo
class Pila():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.items.pop()

    def top(self):
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.items[-1]

    def esta_vacia(self):
        return self.items == []

class Cola():
    def __init__(self):
        self.items = []

    def queue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")
        return self.items.pop(0)

    def top(self):
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")
        return self.items[0]

    def esta_vacia(self):
        return self.items == []

    def tam(self):
        return len(self.items)
'''
from ast import Index

'''
En este enfoque la cola hereda de pila los elementos que son exactamente iguales como agregar, esta vacio,
el constructor, etc. Los que cambian se sobrescriben

class Pila():
    def __init__(self):
        self.items = []

    def agregar(self,item):
        self.items.append(item)

    def remover(self):
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.items.pop()

    def top(self):
        if self.esta_vacia():
            raise IndexError("La pila esta vacia")
        return self.items[-1]

    def esta_vacia(self):
        return self.items == []

class Cola(Pila):
    def remover(self):
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")
        return self.items.pop(0)

    def top(self):
        if self.esta_vacia():
            raise IndexError("La cola esta vacia")
        return self.items[0]

    def tam(self):
        return len(self.items)
'''
