from Estructuras_Datos import Pila

"""
A partir de la expresión posfija, obtiene el valor de la expresión
"""
def operar(expresion):
    op = obtener_notacion_polaca(expresion)
    pila = Pila()

    for termino in op:
        if termino.isdigit():
            pila.push(termino)
        else:
            num1 = int(pila.pop())
            num2 = int(pila.pop())
            res = 0
            if termino == "+":
                res = num1+num2
            elif termino == "-":
                res = num1-num2
            elif termino == "*":
                res = num1*num2
            elif termino == "-/":
                res = num1/num2

            pila.push(str(res))

    return pila.pop()

"""
Genera la notación polaca postfija de una expresión infija, verificando primero que los simbolos este equilibrados
"""
def obtener_notacion_polaca(expresion):
    if equilibrar_simbolos(expresion):
        pila = Pila()
        salida = []
        terminos_palabras = obtener_terminos(expresion)

        for termino in terminos_palabras:
            if termino.isdigit():
                salida.append(termino)
            elif termino in "+-*/":
                pila.push(termino)
            elif termino in "({[":
                pila.push(termino)
            elif termino in ")}]":
                elemento_final = pila.pop()
                while elemento_final not in "({[":
                    salida.append(elemento_final)
                    elemento_final = pila.pop()

        while not pila.esta_vacia():
            elemento_final = pila.pop()
            salida.append(elemento_final)

        return "".join(salida)
    else:
        return "La expresión no está balanceada"

"""
Muestra si una expresión tiene el número de parentesis correctos
"""
def equilibrar_simbolos(expresion):
    balanceado = True
    pila = Pila()
    terminos_palabras = obtener_terminos(expresion)

    #Voy por cada caracter que sea "({[" o ")}]". Si es ({[ lo agrego en la pila, de lo contrario primero verifico si la pila esta vacia
    #en caso de estarlo se pone balanceado como False, ya que hay más terminos de cierre. Si no esta vacio, verifico que el ultimo elemento
    #de la pila corresponda con su respectivo elemento de cierre, en caso de que no, no esta balanceado. Por ultimo si la pila no esta vacia,
    #eso significa que hay más terminos de apertura, lo cual daria tambien false.

    for termino in terminos_palabras:
        if termino in "({[":
            pila.push(termino)
        elif termino in ")}]":
            if pila.esta_vacia():
               balanceado = False
            else:
                balanceado = verificar_simbolo_cierre(pila.pop(),termino)

            if not balanceado:
                break

    if not(pila.esta_vacia()):
        balanceado = False

    return balanceado

"""
Convierte el string en una lista
"""
def obtener_terminos(expresion):
    terminos_palabras = []

    # Obtengo los terminos de la expresión
    for caracter in expresion:
        if caracter != " ":
            terminos_palabras.append(caracter)

    return terminos_palabras

"""
Verifica que el simbolo de apaertura corresponda con el de cierre
"""
def verificar_simbolo_cierre(apertura,cierre):
    simbolos_apertura = "({["
    simbolos_cierre = ")}]"
    return simbolos_apertura.index(apertura) == simbolos_cierre.index(cierre)


print(operar("(9+5)*{8+4}"))