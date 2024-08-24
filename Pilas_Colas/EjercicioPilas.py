from Estructuras_Datos import Pila

# A partir de la expresión posfija, obtiene el valor de la expresión
def operar(expresion):
    op = obtener_notacion_polaca(expresion)
    pila = Pila()  # Asegúrate de que esta clase esté definida correctamente

    if op is not None:
        numero_actual = ""
        for termino in op:
            if termino.isdigit():
                numero_actual = numero_actual + termino
            elif termino == " ":
                pila.push(int(numero_actual))
                numero_actual = ""
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

        for termino in terminos:
            if termino.isnumeric():
                salida.append(termino)
                salida.append(" ")
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

def obtener_terminos_expresion(expresion):
    numero = ""
    salida = []
    for item in expresion:
        if item.isdigit():
            numero= numero+item
        else:
            salida.append(numero)
            salida.append(item)
            numero = ""
    return list(filter(lambda x:x!="",salida))

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


print(operar(input()))