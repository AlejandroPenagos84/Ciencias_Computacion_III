from Estructuras_Datos import Pila

def equilibrar_simbolos(palabra):
    terminos_palabras = []

    # Obtengo los terminos de la expresión
    for caracter in palabra:
        if caracter != " ":
            terminos_palabras.append(caracter)


    balanceado = True
    pila = Pila()

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

def verificar_simbolo_cierre(apertura,cierre):
    simbolos_apertura = "({["
    simbolos_cierre = ")}]"
    return simbolos_apertura.index(apertura) == simbolos_cierre.index(cierre)

print(equilibrar_simbolos("{[a](n[a])"))