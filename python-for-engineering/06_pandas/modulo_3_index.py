"""
Módulo 3: Index - La Columna Vertebral
=======================================
Exploración de la clase Index y sus subclases desde perspectiva de POO.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def explorar_index_base():
    """
    Explora la clase Index base.
    """
    print("="*70)
    print("LA CLASE INDEX BASE")
    print("="*70)
    
    # Crear un Index simple
    idx = pd.Index([1, 2, 3, 4, 5])
    
    print(f"\nTipo: {type(idx)}")
    print(f"Clase: {idx.__class__.__name__}")
    print(f"Contenido: {idx}")
    
    print("\nATRIBUTOS PRINCIPALES:")
    print(f"  values: {idx.values}")
    print(f"  dtype: {idx.dtype}")
    print(f"  name: {idx.name}")
    print(f"  shape: {idx.shape}")
    print(f"  size: {idx.size}")
    print(f"  ndim: {idx.ndim}")
    
    print("\nPROPIEDADES:")
    print(f"  is_unique: {idx.is_unique}")
    print(f"  is_monotonic_increasing: {idx.is_monotonic_increasing}")
    print(f"  is_monotonic_decreasing: {idx.is_monotonic_decreasing}")
    print(f"  has_duplicates: {idx.has_duplicates}")


def demostrar_inmutabilidad():
    """
    Demuestra que Index es inmutable.
    """
    print("\n" + "="*70)
    print("INMUTABILIDAD DE INDEX")
    print("="*70)
    
    idx = pd.Index([1, 2, 3, 4, 5])
    print(f"Index original: {idx}")
    
    print("\n💡 Index es INMUTABLE - no se puede modificar directamente")
    
    # Intentar modificar causará error (comentado)
    try:
        idx[0] = 10
    except TypeError as e:
        print(f"\n❌ Error al intentar modificar: {e}")
    
    print("\n✅ Para 'modificar', crear un nuevo Index:")
    idx_nuevo = pd.Index([10, 2, 3, 4, 5])
    print(f"Nuevo Index: {idx_nuevo}")
    print(f"¿Es el mismo objeto? {idx is idx_nuevo}")
    print(f"ID original: {id(idx)}")
    print(f"ID nuevo: {id(idx_nuevo)}")


def jerarquia_de_index():
    """
    Muestra la jerarquía de clases de Index.
    """
    print("\n" + "="*70)
    print("JERARQUÍA DE CLASES INDEX")
    print("="*70)
    
    tipos_index = [
        ("Index base", pd.Index([1, 2, 3])),
        ("RangeIndex", pd.RangeIndex(start=0, stop=10, step=2)),
        ("Int64Index", pd.Index([1, 2, 3], dtype='int64')),
        ("Float64Index", pd.Index([1.1, 2.2, 3.3])),
        ("DatetimeIndex", pd.date_range('2024-01-01', periods=5)),
        ("TimedeltaIndex", pd.timedelta_range('1 day', periods=5)),
        ("PeriodIndex", pd.period_range('2024-01', periods=5, freq='M')),
        ("MultiIndex", pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1)])),
        ("CategoricalIndex", pd.CategoricalIndex(['a', 'b', 'c', 'a', 'b'])),
    ]
    
    for nombre, idx in tipos_index:
        print(f"\n{nombre}:")
        print(f"  Tipo: {type(idx).__name__}")
        print(f"  Hereda de Index: {isinstance(idx, pd.Index)}")
        print(f"  Contenido: {idx}")
        print(f"  dtype: {idx.dtype}")


def demostrar_range_index():
    """
    Demuestra RangeIndex - optimizado para memoria.
    """
    print("\n" + "="*70)
    print("RANGEINDEX: Índice optimizado para memoria")
    print("="*70)
    
    # RangeIndex no almacena todos los valores, solo start, stop, step
    idx_range = pd.RangeIndex(start=0, stop=1000000, step=1)
    idx_normal = pd.Index(range(1000000))
    
    print(f"RangeIndex(0, 1000000, 1):")
    print(f"  Tipo: {type(idx_range)}")
    print(f"  Primeros 10: {idx_range[:10]}")
    print(f"  Memoria: {idx_range.memory_usage(deep=True)} bytes")
    
    print(f"\nIndex normal (0 a 999999):")
    print(f"  Tipo: {type(idx_normal)}")
    print(f"  Memoria: {idx_normal.memory_usage(deep=True)} bytes")
    
    print(f"\n💡 RangeIndex usa ~{idx_normal.memory_usage(deep=True) // idx_range.memory_usage(deep=True)}x menos memoria")


def demostrar_datetime_index():
    """
    Demuestra DatetimeIndex para series temporales.
    """
    print("\n" + "="*70)
    print("DATETIMEINDEX: Índice para series temporales")
    print("="*70)
    
    # Crear DatetimeIndex
    fechas = pd.date_range('2024-01-01', periods=10, freq='D')
    
    print(f"Tipo: {type(fechas)}")
    print(f"Contenido:\n{fechas}")
    
    print("\nATRIBUTOS ESPECIALES:")
    print(f"  year: {fechas.year}")
    print(f"  month: {fechas.month}")
    print(f"  day: {fechas.day}")
    print(f"  dayofweek: {fechas.dayofweek}")
    print(f"  day_name(): {fechas.day_name()}")
    
    print("\nMÉTODOS ESPECIALES:")
    print(f"  freq: {fechas.freq}")
    print(f"  freqstr: {fechas.freqstr}")
    
    # Usar con Series
    serie_temporal = pd.Series(
        np.random.randn(10),
        index=fechas,
        name='valores'
    )
    print(f"\nSeries con DatetimeIndex:")
    print(serie_temporal)


def demostrar_multiindex():
    """
    Demuestra MultiIndex (índice jerárquico).
    """
    print("\n" + "="*70)
    print("MULTIINDEX: Índice jerárquico (multinivel)")
    print("="*70)
    
    # Crear MultiIndex desde tuplas
    idx = pd.MultiIndex.from_tuples([
        ('España', 'Madrid'),
        ('España', 'Barcelona'),
        ('Francia', 'París'),
        ('Francia', 'Lyon'),
        ('Italia', 'Roma'),
        ('Italia', 'Milán')
    ], names=['país', 'ciudad'])
    
    print(f"Tipo: {type(idx)}")
    print(f"Niveles: {idx.nlevels}")
    print(f"Nombres: {idx.names}")
    print(f"\nContenido:\n{idx}")
    
    # Usar con Series
    poblacion = pd.Series(
        [3200000, 1600000, 2200000, 500000, 2800000, 1400000],
        index=idx,
        name='población'
    )
    
    print(f"\nSeries con MultiIndex:")
    print(poblacion)
    
    print(f"\nAcceso por nivel:")
    print(f"  población['España']:\n{poblacion['España']}")


def demostrar_operaciones_index():
    """
    Demuestra operaciones con Index.
    """
    print("\n" + "="*70)
    print("OPERACIONES CON INDEX")
    print("="*70)
    
    idx1 = pd.Index([1, 2, 3, 4, 5])
    idx2 = pd.Index([4, 5, 6, 7, 8])
    
    print(f"Index 1: {idx1}")
    print(f"Index 2: {idx2}")
    
    print("\n1. UNIÓN (union):")
    union = idx1.union(idx2)
    print(f"  {union}")
    
    print("\n2. INTERSECCIÓN (intersection):")
    interseccion = idx1.intersection(idx2)
    print(f"  {interseccion}")
    
    print("\n3. DIFERENCIA (difference):")
    diferencia = idx1.difference(idx2)
    print(f"  {diferencia}")
    
    print("\n4. DIFERENCIA SIMÉTRICA (symmetric_difference):")
    sim_dif = idx1.symmetric_difference(idx2)
    print(f"  {sim_dif}")
    
    print("\n💡 Estas son operaciones de TEORÍA DE CONJUNTOS")


def demostrar_index_en_series_dataframe():
    """
    Demuestra cómo Index se usa en Series y DataFrame.
    """
    print("\n" + "="*70)
    print("INDEX EN SERIES Y DATAFRAME")
    print("="*70)
    
    # Index en Series
    print("\n1. Index en Series:")
    serie = pd.Series(
        [10, 20, 30, 40],
        index=['a', 'b', 'c', 'd']
    )
    print(f"Serie:\n{serie}")
    print(f"Tipo de índice: {type(serie.index)}")
    print(f"serie.index: {serie.index}")
    
    # Index en DataFrame (filas y columnas)
    print("\n2. Index en DataFrame:")
    df = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        index=['fila1', 'fila2', 'fila3'],
        columns=['col1', 'col2', 'col3']
    )
    print(f"DataFrame:\n{df}")
    print(f"\nÍndice de filas: {df.index}")
    print(f"Tipo: {type(df.index)}")
    print(f"\nÍndice de columnas: {df.columns}")
    print(f"Tipo: {type(df.columns)}")
    
    print("\n💡 DataFrame tiene DOS Index: uno para filas, otro para columnas")


def demostrar_metodos_index():
    """
    Demuestra métodos útiles de Index.
    """
    print("\n" + "="*70)
    print("MÉTODOS ÚTILES DE INDEX")
    print("="*70)
    
    idx = pd.Index(['a', 'b', 'c', 'd', 'e'])
    
    print(f"Index: {idx}")
    
    print("\n1. BÚSQUEDA:")
    print(f"  get_loc('c'): {idx.get_loc('c')}")
    print(f"  'c' in idx: {'c' in idx}")
    
    print("\n2. TRANSFORMACIÓN:")
    print(f"  to_list(): {idx.to_list()}")
    print(f"  to_numpy(): {idx.to_numpy()}")
    
    print("\n3. REINDEXACIÓN:")
    nuevo_idx = idx.insert(2, 'x')
    print(f"  insert(2, 'x'): {nuevo_idx}")
    
    eliminado = idx.delete(2)
    print(f"  delete(2): {eliminado}")
    
    print("\n4. RENOMBRAR:")
    idx_con_nombre = idx.rename('letras')
    print(f"  rename('letras'): {idx_con_nombre}")
    print(f"  name: {idx_con_nombre.name}")


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 3: INDEX - LA COLUMNA VERTEBRAL")
    print("="*70)
    
    explorar_index_base()
    demostrar_inmutabilidad()
    jerarquia_de_index()
    demostrar_range_index()
    demostrar_datetime_index()
    demostrar_multiindex()
    demostrar_operaciones_index()
    demostrar_index_en_series_dataframe()
    demostrar_metodos_index()

