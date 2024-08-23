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

