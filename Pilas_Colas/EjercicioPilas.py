from Estructuras_Datos import Pila


# Muestra si una expresión tiene el número de parentesis correctos
def equilibrar_simbolos(expresion):
    pila = Pila()
    terminos_palabras = expresion.replace("\\s", "")

    for termino in terminos_palabras:
        if termino in "({[":
            pila.push(termino)
        elif termino in ")}]":
            if pila.esta_vacia() or not verificar_simbolo_cierre(pila.pop(), termino):
                return False
    return pila.esta_vacia()


# Verifica que el simbolo de apaertura corresponda con el de cierre
def verificar_simbolo_cierre(apertura,cierre):
    simbolos_apertura = "({["
    simbolos_cierre = ")}]"
    return simbolos_apertura.index(apertura) == simbolos_cierre.index(cierre)


print(equilibrar_simbolos(input()))
