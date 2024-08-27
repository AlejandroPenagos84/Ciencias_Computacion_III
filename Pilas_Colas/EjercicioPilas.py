from Estructuras_Datos import Pila

# A partir de la expresión posfija, obtiene el valor de la expresión
def operar(expresion):
    op = obtener_notacion_polaca(expresion)
    pila = Pila()

    if op is not None:
        print(op)
        for termino in op:
            if termino.isnumeric():
                pila.push(float(termino))
            else:
                num1 = pila.pop()
                num2 = pila.pop()
                res = 0
                if termino == "+":
                    res = num2 + num1
                elif termino == "-":
                    res = num2 - num1
                elif termino == "*":
                    res = num2 * num1
                elif termino == "/":
                    res = num2 / num1
                pila.push(res)
        return pila.pop()
    else:
        return "La expresion no esta balanceada"

# Genera la notación polaca postfija de una expresión infija, verificando primero que los simbolos este equilibrados
def obtener_notacion_polaca(expresion):
    if equilibrar_simbolos(expresion):
        pila = Pila()
        salida = []
        terminos = obtener_terminos_expresion(expresion)

        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}

        for termino in terminos:
            if termino.isnumeric():
                salida.append(termino)
            elif termino in "+-*/":
                while (not pila.esta_vacia() and
                       pila.top() in precedencia and
                       precedencia[termino] <= precedencia[pila.top()]):
                    salida.append(pila.pop())
                pila.push(termino)
            elif termino in "({[":
                pila.push(termino)
            elif termino in ")}]":
                while not pila.esta_vacia() and pila.top() not in "({[":
                    salida.append(pila.pop())
                pila.pop()

        while not pila.esta_vacia():
            salida.append(pila.pop())

        return salida
    else:
        return None


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

def obtener_terminos_expresion(expresion):
    numero = ""
    salida = []
    for item in expresion:
        if item.isnumeric():
            numero= numero+item
        else:
            salida.append(numero)
            salida.append(item)
            numero = ""

    if numero != "":
        salida.append(numero)
    return list(filter(lambda x:x!="",salida))

# Verifica que el simbolo de apaertura corresponda con el de cierre
def verificar_simbolo_cierre(apertura,cierre):
    simbolos_apertura = "({["
    simbolos_cierre = ")}]"
    return simbolos_apertura.index(apertura) == simbolos_cierre.index(cierre)


print(equilibrar_simbolos(input()))


#print(operar(input()))