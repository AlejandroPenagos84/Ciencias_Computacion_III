from Estructuras_Datos import Cola
from Tareas import Tareas, tareasPrediseñadas

"""
'Ejercicio 2: Colas '
Tenemos un conjunto de n tareas, cada una de las cuales tarda un tiempo
predefinido ti, y n procesadores donde se ejecutan las tareas. El objetivo es
dar una planificación de las tareas (un orden de ejecución de las mismas)
de manera que se minimice el tiempo medio de finalización. El tiempo de
finalización de una tarea es el tiempo que transcurre entre el instante
inicial (instante 0) y el momento en el que concluye una tarea.
 Realiza funciones de dar de alta a las tareas, eliminar, mostrar ,salir y
proceso para realizar todas las tareas.
"""

# primero instanciaremos la cola para usarla:
colaPlanificacion = Cola()
todasTareas = []

# lo segundo es meter las tareas, y luego planificarlas:
print("Elija cuantas tareas quiere implementar")
numeroTareas = int(input())

# despues usaremos un for para añadir las tareas, si se quiere usar prediseñadas, usar del modulo Tareas "tareasPrediseñadas()"
for i in range(0, numeroTareas):
    auxTarea = Tareas(input("Nombre Tarea: "), int(input("Beneficio: ")), int(input("Plazo: ")))
    todasTareas.append(auxTarea)


# ahora haremos el código para planificar.

def buscar(rotulos,elemento):  # lo que hace esta funcion es buscar un elemento y reducir la altura para que sea mas facil de buscar
    rotulo = elemento  # igualamos el elemento buscado como si se tratase un rotulo y miramos si coincide con los rotulos enviados, si r = [0,1,2,3,4] y elemento e 3 se acaba

    while rotulos[rotulo] != rotulo:
        rotulo = rotulos[rotulo]  # suponiendo que no son iguales lo que hace es igualar al que esta, es decir: [0,0,0,3,3], si buscamos 4, esta en 3
        # luego lo pone en 0 porque 3 es 0, y asi encontramos al rotulo principal que es 0.
    j = elemento  # ahora mandamos el rotulo principal y una nueva organizacio para una busqueda efectiva, en este caso seria: [0,0,0,0,0]
    while j != rotulo:
        temp = rotulos[j]
        rotulos[j] = rotulo
        j = temp
        #aqui entonces rotulo es 0 , entonces el elemenoto donde esta el rotulo lo iguala al rotulo rpincipal, y i lo iguala
        #al elemenoto en la psocion i.
    return [rotulo, rotulos]  # retornamos el rotulo princiapl, y el roden de los rotulos en "compresion"


def fusionar(rotulos, rangos, rotulo1,
             rotulo2):  # Se usa para no tener separadas dos monituclos, por decirlo asi, es decir: [0,0,0,3,3] ->(fusionar)-> [0,0,0,0,3]
    a = min(rotulo1, rotulo2)  # sacamos al minimo
    b = max(rotulo1, rotulo2)  # y al maximo de los rotulos
    if rangos[a] == rangos[
        b]:  # si ambos rangos son iguales, lo que hacemos es fusionar, y aumentar de rango al a que pas aa ser el principal
        rotulos[b] = a
        rangos[a] += 1
    elif rangos[a] > rangos[
        b]:  # si el rango a es mayor al de b entonces el rtoulo de b es igual al de a, uniendolo sin ponerle rango porque se conserva
        rotulos[b] = a
    else:  # igual al revez, si ya tiene un rango de 2 y el otro es de 2, no cambiara ya que no se une a una rama sino al principal
        rotulos[a] = b
    return [rotulos, rangos]


def construir(conjuntos):
    totalE = [item for sublist in conjuntos for item in
              sublist]  # obtenemos el total de elemenos quitando los agrupados
    # lenE = len(totalE)
    rotulos = []
    for conjunto in conjuntos:
        rotulo = min(conjunto)  # establecemos cual es el rotulo ya que siempre es el menor de los mini conjuntos
        for l in range(len(conjunto)):  # establecemos los consecutivos es decir [0,0,0,3,3 , ...] como ejemplo.
            rotulos.append(rotulo)
    rangos = [0] * len(rotulos)

    return [rotulos, rangos, totalE]


def planificacion(tareas):
    tareas = sorted(tareas, key=lambda x: x.getBeneficio(), reverse=True)  # los ordenamos por beneficio
    plazos = [0]
    n = len(tareas)
    for tarea in tareas:
        plazos.append(tarea.getPlazo())
    maximoPlazo = min(n,max(plazos))  # Obtenemos cual es el maximo plazo que pueda ser añadido que no alcance el maximo de celdas
    resultado = [0] * (maximoPlazo+1)  # Creamos un array de 0 [0,0,0,0,...] -> para añadir en como seran las tareas se hace +1 porque se obvia el primero
    menores = list(range(maximoPlazo + 1))  # creamos un array ordenado para luego ver como ordenar en rotulos [0,1,2,3,4,...] , tambien +1 ya que resultado lo hace

    conjuntosIni = [[k] for k in range(maximoPlazo+1)]  # los conjuntos iniciales serian los primeros rotulos individuales de rango 0
    [rotulos, rangos, elementos] = construir(
        conjuntosIni)  # construiimos los conjuntos iniciales y los vamos a guardar en las variables del retorno
    # haremos un for en el tamaño de las tareas:
    numTareas = 0
    rotulo = None
    rotuloAnterior = None
    for p in range(n):
        [rotulo, rotulos] = buscar(rotulos, min(maximoPlazo, plazos[p]))  # Aqui elije el plazo mas grande que sea por lo menos igual al tamaño de plazos
        menor = menores[rotulo]  # escoje como menor al menor mediante la posicion del rotulo escogido
        if menor > 0:
            resultado[menor] = p  # en el candidato de resultado ponemos como i , es ecir, si el menor es 1, quedaria: [0,1,...] (1mera iteracion)
            [rotuloAnterior, rotulos] = buscar(rotulos, menor - 1)
            menores[rotulo] = menores[rotuloAnterior]
            [rotulos, rangos] = fusionar(rotulos, rangos, rotulo, rotuloAnterior)
        if numTareas >= maximoPlazo:
            break
    resultado = [v for v in resultado if v > 0]
    return resultado

res = planificacion(tareasPrediseñadas())

print(res)
otro = []
for i in range(len(res)):
    otro.append(tareasPrediseñadas()[res[i]].nombreTarea)
print(otro)