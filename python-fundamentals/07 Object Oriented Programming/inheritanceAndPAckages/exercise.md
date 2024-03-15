# Ejercicio #

## Pila ##

Una [pila](https://es.wikipedia.org/wiki/Pila_(inform%C3%A1tica) en informática es una estructura de datos que 
permite coleccionar elementos y define una serie de comportamientos.

Tu tarea es implementar la clase Stack siguiendo la interfaz:

    class StackBase:
        
    # Construye una pila vacía.
        def __init__():
            pass

    # Devuelve un entero, el número de elementos en la pila.
        def size():

    # Agrega un elemento al final de la pila.
        def push():

    # Elimina un elemento del final de la pila y lo devuelve.
        def pop():

    # Devuelve un elemento del final de la pila sin eliminarlo.
        def top():

    # Devuelve True si la pila está vacía, en caso contrario devuelve False.
        def empty():

    # Elimina todos los elementos de la pila.
        def clear():

        def __str__():

Ninguno de los métodos debe debería tener un costo en tiempo que dependa del tamaño de la Pila.
