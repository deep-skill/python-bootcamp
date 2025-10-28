"""
Módulo 5: Herencia y Polimorfismo en Pandas
============================================
Exploración de la jerarquía de clases y polimorfismo en Pandas.
"""

import pandas as pd
import numpy as np


def explorar_jerarquia_ndframe():
    """
    Explora la jerarquía de herencia: NDFrame → Series/DataFrame
    """
    print("="*70)
    print("JERARQUÍA DE HERENCIA: NDFrame")
    print("="*70)
    
    serie = pd.Series([1, 2, 3])
    df = pd.DataFrame({'A': [1, 2, 3]})
    
    print("\n1. SERIES:")
    print(f"   Tipo: {type(serie)}")
    print(f"   Hereda de NDFrame: {isinstance(serie, pd.core.generic.NDFrame)}")
    print(f"\n   Jerarquía (MRO):")
    for i, clase in enumerate(serie.__class__.__mro__[:6]):
        print(f"     {i}. {clase}")
    
    print("\n2. DATAFRAME:")
    print(f"   Tipo: {type(df)}")
    print(f"   Hereda de NDFrame: {isinstance(df, pd.core.generic.NDFrame)}")
    print(f"\n   Jerarquía (MRO):")
    for i, clase in enumerate(df.__class__.__mro__[:6]):
        print(f"     {i}. {clase}")
    
    print("\n💡 NDFrame es la clase base compartida")


def demostrar_metodos_compartidos():
    """
    Demuestra métodos compartidos entre Series y DataFrame.
    """
    print("\n" + "="*70)
    print("MÉTODOS COMPARTIDOS (heredados de NDFrame)")
    print("="*70)
    
    serie = pd.Series([10, 20, 30, 40, 50], name='valores')
    df = pd.DataFrame({
        'A': [10, 20, 30, 40, 50],
        'B': [5, 10, 15, 20, 25]
    })
    
    print("Serie:")
    print(serie)
    print("\nDataFrame:")
    print(df)
    
    # Métodos compartidos
    metodos_comunes = ['head', 'tail', 'describe', 'sum', 'mean', 
                       'copy', 'info', 'isna', 'dropna', 'fillna']
    
    print("\n" + "-"*70)
    print("Métodos que ambos comparten:")
    for metodo in metodos_comunes:
        tiene_serie = hasattr(serie, metodo)
        tiene_df = hasattr(df, metodo)
        print(f"  {metodo:15} - Serie: {tiene_serie}, DataFrame: {tiene_df}")
    
    # Ejecutar algunos métodos
    print("\n" + "-"*70)
    print("Ejecutando métodos compartidos:")
    print(f"\nserie.head(3):\n{serie.head(3)}")
    print(f"\ndf.head(3):\n{df.head(3)}")
    
    print(f"\nserie.sum(): {serie.sum()}")
    print(f"\ndf.sum():\n{df.sum()}")


def demostrar_polimorfismo():
    """
    Demuestra polimorfismo: mismo método, comportamiento diferente.
    """
    print("\n" + "="*70)
    print("POLIMORFISMO: Mismo método, comportamiento diferente")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    
    # El método sum() se comporta diferente
    print("\n1. Método sum():")
    print(f"   serie.sum() (retorna escalar): {serie.sum()}")
    print(f"   Tipo: {type(serie.sum())}")
    
    print(f"\n   df.sum() (retorna Series):\n{df.sum()}")
    print(f"   Tipo: {type(df.sum())}")
    
    # El método describe() se comporta diferente
    print("\n2. Método describe():")
    print(f"   serie.describe() (retorna Series):\n{serie.describe()}")
    print(f"   Tipo: {type(serie.describe())}")
    
    print(f"\n   df.describe() (retorna DataFrame):\n{df.describe()}")
    print(f"   Tipo: {type(df.describe())}")
    
    print("\n💡 Polimorfismo: mismo nombre, implementación diferente")


def demostrar_duck_typing():
    """
    Demuestra duck typing en Pandas.
    """
    print("\n" + "="*70)
    print("DUCK TYPING: 'Si camina como pato y grazna como pato...'")
    print("="*70)
    
    def procesar_datos(datos):
        """
        Función que acepta Series o DataFrame.
        No verifica el tipo, solo que tenga los métodos necesarios.
        """
        print(f"\nProcesando objeto tipo: {type(datos).__name__}")
        print(f"  Suma: {datos.sum()}")
        print(f"  Media: {datos.mean()}")
        print(f"  Primeras 3 filas:\n{datos.head(3)}")
    
    # Funciona con Series
    serie = pd.Series([10, 20, 30, 40, 50])
    procesar_datos(serie)
    
    # Funciona con DataFrame
    df = pd.DataFrame({'A': [10, 20, 30, 40, 50]})
    procesar_datos(df)
    
    print("\n💡 Duck typing: no importa el tipo, importan los métodos")


def explorar_clase_indexopsmixin():
    """
    Explora IndexOpsMixin, otra clase base importante.
    """
    print("\n" + "="*70)
    print("INDEXOPSMIXIN: Operaciones con índices")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    index = pd.Index([10, 20, 30])
    
    print(f"Serie hereda de IndexOpsMixin: {isinstance(serie, pd.core.base.IndexOpsMixin)}")
    print(f"Index hereda de IndexOpsMixin: {isinstance(index, pd.core.base.IndexOpsMixin)}")
    
    # Métodos compartidos de IndexOpsMixin
    metodos = ['value_counts', 'unique', 'nunique', 'is_unique', 'duplicated']
    
    print("\nMétodos compartidos de IndexOpsMixin:")
    for metodo in metodos:
        tiene_serie = hasattr(serie, metodo)
        tiene_index = hasattr(index, metodo)
        print(f"  {metodo:15} - Series: {tiene_serie}, Index: {tiene_index}")


def demostrar_metodos_especificos():
    """
    Demuestra métodos específicos de cada clase.
    """
    print("\n" + "="*70)
    print("MÉTODOS ESPECÍFICOS DE CADA CLASE")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Métodos solo en Series
    print("\n1. Métodos SOLO en Series:")
    metodos_serie = ['autocorr', 'between', 'item', 'argmax', 'argmin']
    for metodo in metodos_serie:
        tiene_serie = hasattr(serie, metodo)
        tiene_df = hasattr(df, metodo)
        print(f"  {metodo:15} - Series: {tiene_serie}, DataFrame: {tiene_df}")
    
    # Métodos solo en DataFrame
    print("\n2. Métodos SOLO en DataFrame:")
    metodos_df = ['pivot', 'pivot_table', 'stack', 'unstack', 'melt']
    for metodo in metodos_df:
        tiene_serie = hasattr(serie, metodo)
        tiene_df = hasattr(df, metodo)
        print(f"  {metodo:15} - Series: {tiene_serie}, DataFrame: {tiene_df}")


def crear_subclase_personalizada():
    """
    Demuestra cómo crear una subclase de Series.
    """
    print("\n" + "="*70)
    print("CREAR SUBCLASE PERSONALIZADA")
    print("="*70)
    
    class SerieConUnidades(pd.Series):
        """
        Subclase de Series que incluye unidades de medida.
        """
        
        @property
        def _constructor(self):
            return SerieConUnidades
        
        def __init__(self, *args, unidad=None, **kwargs):
            super().__init__(*args, **kwargs)
            self.unidad = unidad
        
        def __repr__(self):
            repr_normal = super().__repr__()
            if self.unidad:
                return f"{repr_normal}\nUnidad: {self.unidad}"
            return repr_normal
        
        def convertir_a(self, nueva_unidad, factor):
            """Convierte a otra unidad."""
            nueva_serie = self * factor
            nueva_serie.unidad = nueva_unidad
            return nueva_serie
    
    # Usar la subclase
    print("\nCreando SerieConUnidades:")
    distancias = SerieConUnidades([100, 200, 300], unidad='metros', name='distancia')
    print(distancias)
    
    print("\nConvertir a kilómetros:")
    distancias_km = distancias.convertir_a('kilómetros', 0.001)
    print(distancias_km)
    
    print("\n💡 Podemos extender Pandas con nuestras propias clases")


def demostrar_herencia_multiple():
    """
    Explora la herencia múltiple en Pandas.
    """
    print("\n" + "="*70)
    print("HERENCIA MÚLTIPLE EN PANDAS")
    print("="*70)
    
    serie = pd.Series([1, 2, 3])
    
    print("Series hereda de múltiples clases:")
    print(f"\nClases base directas de Series:")
    for i, clase in enumerate(pd.Series.__bases__):
        print(f"  {i+1}. {clase}")
    
    print(f"\nMRO completo (primeras 10 clases):")
    for i, clase in enumerate(pd.Series.__mro__[:10]):
        print(f"  {i+1}. {clase}")
    
    print("\n💡 Series usa herencia múltiple para combinar funcionalidad")


def comparar_estructuras_completo():
    """
    Comparación completa de las estructuras desde POO.
    """
    print("\n" + "="*70)
    print("COMPARACIÓN COMPLETA: Series vs DataFrame vs Index")
    print("="*70)
    
    estructuras = {
        'Series': pd.Series([1, 2, 3]),
        'DataFrame': pd.DataFrame({'A': [1, 2, 3]}),
        'Index': pd.Index([1, 2, 3])
    }
    
    clases_base = [
        'NDFrame',
        'IndexOpsMixin',
        'PandasObject',
        'SelectionMixin'
    ]
    
    print("\nHerencia de clases base:")
    print(f"{'Estructura':<12} | {'NDFrame':<10} | {'IndexOpsMixin':<15} | {'PandasObject':<15}")
    print("-" * 70)
    
    for nombre, obj in estructuras.items():
        ndframe = isinstance(obj, pd.core.generic.NDFrame)
        indexops = isinstance(obj, pd.core.base.IndexOpsMixin)
        pandasobj = isinstance(obj, pd.core.base.PandasObject)
        
        print(f"{nombre:<12} | {str(ndframe):<10} | {str(indexops):<15} | {str(pandasobj):<15}")


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 5: HERENCIA Y POLIMORFISMO EN PANDAS")
    print("="*70)
    
    explorar_jerarquia_ndframe()
    demostrar_metodos_compartidos()
    demostrar_polimorfismo()
    demostrar_duck_typing()
    explorar_clase_indexopsmixin()
    demostrar_metodos_especificos()
    crear_subclase_personalizada()
    demostrar_herencia_multiple()
    comparar_estructuras_completo()

