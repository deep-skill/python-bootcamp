"""
Módulo 0: Fundamentos de POO aplicados a Pandas
================================================
Este módulo introduce los conceptos básicos de POO y cómo se aplican en Pandas.
"""

import pandas as pd
import numpy as np


def explorar_objeto(obj, nombre="objeto"):
    """
    Explora un objeto mostrando su tipo, clase y algunos métodos.
    
    Args:
        obj: El objeto a explorar
        nombre: Nombre descriptivo del objeto
    """
    print(f"\n{'='*60}")
    print(f"EXPLORANDO: {nombre}")
    print(f"{'='*60}")
    print(f"Tipo: {type(obj)}")
    print(f"Clase: {obj.__class__.__name__}")
    print(f"Módulo: {obj.__class__.__module__}")
    print(f"\nJerarquía de herencia (MRO):")
    for i, clase in enumerate(obj.__class__.__mro__):
        print(f"  {i}. {clase}")
    

def mostrar_atributos_publicos(obj, limite=10):
    """
    Muestra los atributos públicos de un objeto.
    
    Args:
        obj: El objeto a inspeccionar
        limite: Número máximo de atributos a mostrar
    """
    atributos = [attr for attr in dir(obj) if not attr.startswith('_')]
    print(f"\nAtributos públicos (mostrando {min(limite, len(atributos))} de {len(atributos)}):")
    for attr in atributos[:limite]:
        print(f"  - {attr}")


def mostrar_metodos_especiales(obj, limite=15):
    """
    Muestra los métodos especiales (dunder methods) de un objeto.
    
    Args:
        obj: El objeto a inspeccionar
        limite: Número máximo de métodos a mostrar
    """
    metodos = [attr for attr in dir(obj) if attr.startswith('__') and attr.endswith('__')]
    print(f"\nMétodos especiales (mostrando {min(limite, len(metodos))} de {len(metodos)}):")
    for metodo in metodos[:limite]:
        print(f"  - {metodo}")


def comparar_estructuras():
    """
    Compara las estructuras básicas de Pandas desde perspectiva de POO.
    """
    # Crear ejemplos
    serie = pd.Series([1, 2, 3, 4, 5])
    dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    index = pd.Index([0, 1, 2])
    
    estructuras = [
        ("Series", serie),
        ("DataFrame", dataframe),
        ("Index", index)
    ]
    
    print("\n" + "="*70)
    print("COMPARACIÓN DE ESTRUCTURAS DE PANDAS")
    print("="*70)
    
    for nombre, obj in estructuras:
        print(f"\n{nombre}:")
        print(f"  Tipo: {type(obj).__name__}")
        print(f"  Padre directo: {type(obj).__bases__}")
        print(f"  Es NDFrame: {isinstance(obj, pd.core.generic.NDFrame)}")
        print(f"  Es IndexOpsMixin: {isinstance(obj, pd.core.ops.OpsMixin)}")


def demostrar_herencia():
    """
    Demuestra cómo Series y DataFrame heredan de NDFrame.
    """
    serie = pd.Series([1, 2, 3])
    df = pd.DataFrame({'A': [1, 2, 3]})
    
    print("\n" + "="*70)
    print("JERARQUÍA DE HERENCIA EN PANDAS")
    print("="*70)
    
    # Encontrar métodos compartidos
    metodos_serie = set(dir(serie))
    metodos_df = set(dir(df))
    compartidos = metodos_serie & metodos_df
    
    print(f"\nMétodos compartidos entre Series y DataFrame: {len(compartidos)}")
    print(f"Métodos solo en Series: {len(metodos_serie - metodos_df)}")
    print(f"Métodos solo en DataFrame: {len(metodos_df - metodos_serie)}")
    
    # Algunos métodos compartidos importantes
    print("\nAlgunos métodos compartidos importantes:")
    metodos_importantes = ['head', 'tail', 'describe', 'sum', 'mean', 'info', 'copy']
    for metodo in metodos_importantes:
        print(f"  - {metodo}")


def ejemplo_instanciacion():
    """
    Muestra diferentes formas de crear objetos en Pandas.
    """
    print("\n" + "="*70)
    print("INSTANCIACIÓN DE OBJETOS EN PANDAS")
    print("="*70)
    
    # Series - diferentes constructores
    print("\n1. Creando Series de diferentes formas:")
    
    print("\n  a) Desde lista:")
    s1 = pd.Series([1, 2, 3, 4, 5])
    print(f"     {s1.tolist()}")
    
    print("\n  b) Desde diccionario:")
    s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
    print(f"     {s2.to_dict()}")
    
    print("\n  c) Desde escalar:")
    s3 = pd.Series(5, index=['a', 'b', 'c'])
    print(f"     {s3.tolist()}")
    
    print("\n  d) Desde array de NumPy:")
    s4 = pd.Series(np.array([1, 2, 3, 4]))
    print(f"     {s4.tolist()}")
    
    # DataFrame - diferentes constructores
    print("\n2. Creando DataFrame de diferentes formas:")
    
    print("\n  a) Desde diccionario de listas:")
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print(f"     Shape: {df1.shape}")
    
    print("\n  b) Desde lista de diccionarios:")
    df2 = pd.DataFrame([{'A': 1, 'B': 4}, {'A': 2, 'B': 5}])
    print(f"     Shape: {df2.shape}")
    
    print("\n  c) Desde array de NumPy:")
    df3 = pd.DataFrame(np.random.randn(3, 3), columns=['X', 'Y', 'Z'])
    print(f"     Shape: {df3.shape}")


def ejemplo_composicion():
    """
    Demuestra cómo DataFrame es una composición de Series.
    """
    print("\n" + "="*70)
    print("COMPOSICIÓN: DataFrame como colección de Series")
    print("="*70)
    
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María'],
        'edad': [25, 30, 28],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia']
    })
    
    print("\nDataFrame creado:")
    print(df)
    
    print("\n\nAccediendo a una columna (retorna Series):")
    columna_edad = df['edad']
    print(f"Tipo: {type(columna_edad)}")
    print(f"Es una Serie: {isinstance(columna_edad, pd.Series)}")
    print(f"Contenido: {columna_edad.tolist()}")
    
    print("\n\nIterando por columnas (cada una es una Series):")
    for nombre_col in df.columns:
        col = df[nombre_col]
        print(f"  {nombre_col}: tipo={type(col).__name__}, dtype={col.dtype}")


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 0: FUNDAMENTOS DE POO APLICADOS A PANDAS")
    print("="*70)
    
    # Crear una serie simple para explorar
    mi_serie = pd.Series([10, 20, 30, 40, 50], name='ventas')
    
    # Explorar la serie
    explorar_objeto(mi_serie, "Series de Pandas")
    mostrar_atributos_publicos(mi_serie, 15)
    mostrar_metodos_especiales(mi_serie, 15)
    
    # Comparar estructuras
    comparar_estructuras()
    
    # Demostrar herencia
    demostrar_herencia()
    
    # Ejemplos de instanciación
    ejemplo_instanciacion()
    
    # Ejemplo de composición
    ejemplo_composicion()

