"""
Módulo 6: Atributos Especiales y Métodos Mágicos
=================================================
Exploración de los métodos especiales (dunder methods) en Pandas.
"""

import pandas as pd
import numpy as np


def introduccion_metodos_magicos():
    """
    Introducción a los métodos mágicos en Python.
    """
    print("="*70)
    print("MÉTODOS MÁGICOS (DUNDER METHODS)")
    print("="*70)
    
    print("""
Los métodos mágicos son métodos especiales en Python que:
- Comienzan y terminan con doble guion bajo (__método__)
- Permiten que los objetos se comporten como tipos nativos
- Son invocados automáticamente por Python en ciertas operaciones

Ejemplos:
- __init__: Constructor
- __repr__: Representación del objeto
- __str__: Conversión a string
- __len__: Longitud (cuando usas len())
- __getitem__: Acceso con [] (indexación)
- __setitem__: Asignación con []
- __add__: Operador + (suma)
    """)


def demostrar_getitem():
    """
    Demuestra __getitem__ (operador []).
    """
    print("\n" + "="*70)
    print("__getitem__: Operador de indexación []")
    print("="*70)
    
    serie = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    print("\nSeries:")
    print(serie)
    
    print("\n1. Acceso con []:")
    print(f"   serie['a'] llama a serie.__getitem__('a'): {serie['a']}")
    print(f"   Equivalente directo: {serie.__getitem__('a')}")
    
    print("\n2. Slicing con []:")
    print(f"   serie['a':'c']:\n{serie['a':'c']}")
    
    print("\n3. Lista de índices:")
    print(f"   serie[['a', 'c', 'e']]:\n{serie[['a', 'c', 'e']]}")
    
    print("\n" + "-"*70)
    print("\nDataFrame:")
    print(df)
    
    print("\n1. Acceso a columna:")
    print(f"   df['A'] llama a df.__getitem__('A'):\n{df['A']}")
    
    print("\n2. Múltiples columnas:")
    print(f"   df[['A', 'B']]:\n{df[['A', 'B']]}")


def demostrar_setitem():
    """
    Demuestra __setitem__ (asignación con []).
    """
    print("\n" + "="*70)
    print("__setitem__: Asignación con []")
    print("="*70)
    
    serie = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print("Serie original:")
    print(serie)
    
    print("\n1. Modificar un valor:")
    print("   serie['a'] = 999")
    serie['a'] = 999
    print(f"   Resultado: {serie['a']}")
    
    print("\n2. Agregar un nuevo índice:")
    print("   serie['d'] = 40")
    serie['d'] = 40
    print(f"   Serie actualizada:\n{serie}")
    
    print("\n" + "-"*70)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("\nDataFrame original:")
    print(df)
    
    print("\n1. Modificar una columna:")
    print("   df['A'] = [10, 20, 30]")
    df['A'] = [10, 20, 30]
    print(f"   DataFrame actualizado:\n{df}")
    
    print("\n2. Agregar una columna nueva:")
    print("   df['C'] = [7, 8, 9]")
    df['C'] = [7, 8, 9]
    print(f"   DataFrame actualizado:\n{df}")


def demostrar_len():
    """
    Demuestra __len__ (función len()).
    """
    print("\n" + "="*70)
    print("__len__: Función len()")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    print("Serie:", serie.tolist())
    print(f"len(serie) llama a serie.__len__(): {len(serie)}")
    print(f"Equivalente directo: {serie.__len__()}")
    
    print(f"\nDataFrame:\n{df}")
    print(f"len(df) retorna número de FILAS: {len(df)}")
    print(f"Equivalente directo: {df.__len__()}")
    
    print("\n💡 len() en DataFrame retorna el número de filas, no elementos totales")


def demostrar_repr_str():
    """
    Demuestra __repr__ y __str__ (representación del objeto).
    """
    print("\n" + "="*70)
    print("__repr__ y __str__: Representación de objetos")
    print("="*70)
    
    serie = pd.Series([1, 2, 3], name='mi_serie')
    
    print("\n1. __repr__ (representación técnica):")
    print(f"   repr(serie):\n{repr(serie)}")
    
    print("\n2. __str__ (representación legible):")
    print(f"   str(serie):\n{str(serie)}")
    
    print("\n3. print() usa __str__:")
    print("   print(serie):")
    print(serie)
    
    print("\n💡 En Pandas, __repr__ y __str__ suelen retornar lo mismo")


def demostrar_iter():
    """
    Demuestra __iter__ (iteración).
    """
    print("\n" + "="*70)
    print("__iter__: Iteración con for")
    print("="*70)
    
    serie = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    
    print("Serie:")
    print(serie)
    
    print("\n1. Iterar sobre Serie (itera sobre VALORES):")
    print("   for valor in serie:")
    for valor in serie:
        print(f"     {valor}")
    
    print("\n2. Iterar sobre índices:")
    print("   for indice in serie.index:")
    for indice in serie.index:
        print(f"     {indice}")
    
    print("\n3. Iterar sobre items (índice, valor):")
    print("   for idx, val in serie.items():")
    for idx, val in serie.items():
        print(f"     {idx}: {val}")
    
    print("\n" + "-"*70)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("\nDataFrame:")
    print(df)
    
    print("\n1. Iterar sobre DataFrame (itera sobre COLUMNAS):")
    print("   for columna in df:")
    for columna in df:
        print(f"     {columna}")
    
    print("\n2. Iterar sobre filas con iterrows():")
    print("   for idx, fila in df.iterrows():")
    for idx, fila in df.iterrows():
        print(f"     Fila {idx}: {fila.tolist()}")


def demostrar_operadores_aritmeticos():
    """
    Demuestra operadores aritméticos sobrecargados.
    """
    print("\n" + "="*70)
    print("OPERADORES ARITMÉTICOS SOBRECARGADOS")
    print("="*70)
    
    serie1 = pd.Series([1, 2, 3])
    serie2 = pd.Series([10, 20, 30])
    
    print(f"Serie 1: {serie1.tolist()}")
    print(f"Serie 2: {serie2.tolist()}")
    
    print("\n1. __add__ (operador +):")
    print(f"   serie1 + serie2 = {(serie1 + serie2).tolist()}")
    print(f"   Equivalente: serie1.__add__(serie2)")
    
    print("\n2. __sub__ (operador -):")
    print(f"   serie1 - serie2 = {(serie1 - serie2).tolist()}")
    
    print("\n3. __mul__ (operador *):")
    print(f"   serie1 * serie2 = {(serie1 * serie2).tolist()}")
    
    print("\n4. __truediv__ (operador /):")
    print(f"   serie2 / serie1 = {(serie2 / serie1).tolist()}")
    
    print("\n5. __pow__ (operador **):")
    print(f"   serie1 ** 2 = {(serie1 ** 2).tolist()}")
    
    # Con escalares
    print("\n" + "-"*70)
    print("\nOperaciones con escalares:")
    print(f"   serie1 * 10 = {(serie1 * 10).tolist()}")
    print(f"   serie1 + 100 = {(serie1 + 100).tolist()}")


def demostrar_operadores_comparacion():
    """
    Demuestra operadores de comparación sobrecargados.
    """
    print("\n" + "="*70)
    print("OPERADORES DE COMPARACIÓN SOBRECARGADOS")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    print(f"Serie: {serie.tolist()}")
    
    print("\n1. __eq__ (operador ==):")
    print(f"   serie == 3:\n{serie == 3}")
    
    print("\n2. __gt__ (operador >):")
    print(f"   serie > 3:\n{serie > 3}")
    
    print("\n3. __lt__ (operador <):")
    print(f"   serie < 3:\n{serie < 3}")
    
    print("\n4. __ge__ (operador >=):")
    print(f"   serie >= 3:\n{serie >= 3}")
    
    print("\n5. __le__ (operador <=):")
    print(f"   serie <= 3:\n{serie <= 3}")
    
    print("\n6. __ne__ (operador !=):")
    print(f"   serie != 3:\n{serie != 3}")
    
    # Filtrado booleano
    print("\n" + "-"*70)
    print("\nUso en filtrado booleano:")
    filtro = serie > 3
    print(f"   filtro = serie > 3: {filtro.tolist()}")
    print(f"   serie[filtro] = {serie[filtro].tolist()}")


def demostrar_contains():
    """
    Demuestra __contains__ (operador in).
    """
    print("\n" + "="*70)
    print("__contains__: Operador 'in'")
    print("="*70)
    
    serie = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    
    print("Serie:")
    print(serie)
    
    print("\n1. Verificar si un índice existe:")
    print(f"   'a' in serie: {'a' in serie}")
    print(f"   'd' in serie: {'d' in serie}")
    
    print("\n💡 'in' verifica el ÍNDICE, no los valores")
    print(f"   10 in serie.values: {10 in serie.values}")
    
    print("\n" + "-"*70)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("\nDataFrame:")
    print(df)
    
    print("\n1. Verificar si una columna existe:")
    print(f"   'A' in df: {'A' in df}")
    print(f"   'C' in df: {'C' in df}")


def demostrar_call():
    """
    Demuestra métodos que actúan como callable.
    """
    print("\n" + "="*70)
    print("OBJETOS CALLABLE EN PANDAS")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    
    print("Serie:")
    print(serie)
    
    print("\n1. Usar apply con función lambda:")
    print("   serie.apply(lambda x: x ** 2)")
    resultado = serie.apply(lambda x: x ** 2)
    print(f"   {resultado.tolist()}")
    
    print("\n2. Usar map con función:")
    def clasificar(x):
        return 'bajo' if x < 3 else 'alto'
    
    print("   serie.map(clasificar)")
    resultado = serie.map(clasificar)
    print(f"   {resultado.tolist()}")


def explorar_metodos_magicos_disponibles():
    """
    Explora todos los métodos mágicos disponibles en Series.
    """
    print("\n" + "="*70)
    print("MÉTODOS MÁGICOS DISPONIBLES EN SERIES")
    print("="*70)
    
    serie = pd.Series([1, 2, 3])
    
    metodos_magicos = [attr for attr in dir(serie) 
                       if attr.startswith('__') and attr.endswith('__')
                       and not attr.startswith('___')]
    
    print(f"\nTotal de métodos mágicos: {len(metodos_magicos)}")
    
    # Categorizar métodos mágicos
    categorias = {
        'Construcción': ['__init__', '__new__'],
        'Representación': ['__repr__', '__str__', '__format__'],
        'Acceso': ['__getitem__', '__setitem__', '__delitem__', '__contains__'],
        'Iteración': ['__iter__', '__next__', '__reversed__'],
        'Longitud': ['__len__', '__length_hint__'],
        'Aritméticos': ['__add__', '__sub__', '__mul__', '__truediv__', '__floordiv__', 
                       '__mod__', '__pow__'],
        'Aritméticos (reverso)': ['__radd__', '__rsub__', '__rmul__', '__rtruediv__'],
        'Aritméticos (in-place)': ['__iadd__', '__isub__', '__imul__', '__itruediv__'],
        'Comparación': ['__eq__', '__ne__', '__lt__', '__le__', '__gt__', '__ge__'],
        'Booleanos': ['__bool__', '__nonzero__'],
        'Otros': ['__hash__', '__sizeof__', '__dir__', '__class__', '__doc__']
    }
    
    for categoria, metodos in categorias.items():
        disponibles = [m for m in metodos if m in metodos_magicos]
        if disponibles:
            print(f"\n{categoria}:")
            for metodo in disponibles:
                print(f"  - {metodo}")


def ejemplo_practico_completo():
    """
    Ejemplo práctico usando varios métodos mágicos.
    """
    print("\n" + "="*70)
    print("EJEMPLO PRÁCTICO: Análisis de ventas")
    print("="*70)
    
    ventas = pd.Series([100, 150, 200, 175, 225], 
                       index=['Lun', 'Mar', 'Mie', 'Jue', 'Vie'],
                       name='ventas_diarias')
    
    print("Datos de ventas:")
    print(ventas)
    
    # Usar múltiples métodos mágicos
    print("\n1. Calcular promedio (usa __iter__, __len__):")
    promedio = sum(ventas) / len(ventas)
    print(f"   Promedio: {promedio}")
    
    print("\n2. Encontrar días con ventas > 150 (usa __gt__):")
    dias_altos = ventas[ventas > 150]
    print(f"   {dias_altos}")
    
    print("\n3. Aumentar todas las ventas 10% (usa __mul__):")
    ventas_aumentadas = ventas * 1.10
    print(f"   {ventas_aumentadas}")
    
    print("\n4. Verificar si hay datos del sábado (usa __contains__):")
    tiene_sabado = 'Sab' in ventas
    print(f"   ¿Tiene datos del sábado? {tiene_sabado}")
    
    print("\n5. Acceder a venta específica (usa __getitem__):")
    venta_miercoles = ventas['Mie']
    print(f"   Venta del miércoles: {venta_miercoles}")
    
    print("\n💡 Todo esto usa métodos mágicos internamente!")


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 6: ATRIBUTOS ESPECIALES Y MÉTODOS MÁGICOS")
    print("="*70)
    
    introduccion_metodos_magicos()
    demostrar_getitem()
    demostrar_setitem()
    demostrar_len()
    demostrar_repr_str()
    demostrar_iter()
    demostrar_operadores_aritmeticos()
    demostrar_operadores_comparacion()
    demostrar_contains()
    demostrar_call()
    explorar_metodos_magicos_disponibles()
    ejemplo_practico_completo()

