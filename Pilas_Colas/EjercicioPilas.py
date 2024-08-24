from Estructuras_Datos import Pila

#A partir de la expresión posfija, obtiene el valor de la expresión
def operar(expresion):
    op = obtener_notacion_polaca(expresion)
    pila = Pila()

    if op is not None:
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
    else:
        return "La expresion no esta balanceada"

# Genera la notación polaca postfija de una expresión infija, verificando primero que los simbolos este equilibrados
def obtener_notacion_polaca(expresion):
    if equilibrar_simbolos(expresion):
        pila = Pila()
        salida = []
        terminos_palabras = convertir_a_lista(expresion)

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
        return None


# Muestra si una expresión tiene el número de parentesis correctos
def equilibrar_simbolos(expresion):
    balanceado = True
    pila = Pila()
    terminos_palabras = convertir_a_lista(expresion)

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


# Convierte el string en una lista
def convertir_a_lista(expresion):
    terminos_palabras = []

    # Obtengo los terminos de la expresión
    for caracter in expresion:
        if caracter != " ":
            terminos_palabras.append(caracter)

    return terminos_palabras


# Verifica que el simbolo de apaertura corresponda con el de cierre
def verificar_simbolo_cierre(apertura,cierre):
    simbolos_apertura = "({["
    simbolos_cierre = ")}]"
    return simbolos_apertura.index(apertura) == simbolos_cierre.index(cierre)


print(operar("(9+5)*{8+4}*(5)"))