"""
Módulo 1: Series - El Objeto Fundamental
=========================================
Exploración profunda de la clase Series desde la perspectiva de POO.
"""

import pandas as pd
import numpy as np


class AnalizadorSeries:
    """
    Clase para analizar objetos Series de Pandas.
    Demuestra cómo crear clases que interactúan con Series.
    """
    
    def __init__(self, serie):
        """
        Constructor que recibe un objeto Series.
        
        Args:
            serie: Un objeto pd.Series
        """
        if not isinstance(serie, pd.Series):
            raise TypeError("El argumento debe ser un objeto pd.Series")
        self.serie = serie
    
    def anatomia_completa(self):
        """Muestra la anatomía completa de la Serie."""
        print("="*70)
        print("ANATOMÍA COMPLETA DE LA SERIES")
        print("="*70)
        
        print("\n1. IDENTIDAD DEL OBJETO:")
        print(f"   Tipo: {type(self.serie)}")
        print(f"   ID en memoria: {id(self.serie)}")
        print(f"   Tamaño en bytes: {self.serie.memory_usage(deep=True)} bytes")
        
        print("\n2. ATRIBUTOS DE DATOS:")
        print(f"   values: {self.serie.values}")
        print(f"   index: {self.serie.index}")
        print(f"   dtype: {self.serie.dtype}")
        print(f"   name: {self.serie.name}")
        
        print("\n3. ATRIBUTOS DE FORMA:")
        print(f"   shape: {self.serie.shape}")
        print(f"   size: {self.serie.size}")
        print(f"   ndim: {self.serie.ndim}")
        print(f"   empty: {self.serie.empty}")
        
        print("\n4. ATRIBUTOS DE ÍNDICE:")
        print(f"   Tipo de índice: {type(self.serie.index)}")
        print(f"   Nombre del índice: {self.serie.index.name}")
        print(f"   Es único: {self.serie.index.is_unique}")
        print(f"   Es monótono: {self.serie.index.is_monotonic_increasing}")
    
    def mostrar_atributos_de_clase(self):
        """Muestra los atributos de clase vs instancia."""
        print("\n" + "="*70)
        print("ATRIBUTOS DE CLASE VS INSTANCIA")
        print("="*70)
        
        # Atributos de instancia (propios del objeto)
        print("\nATRIBUTOS DE INSTANCIA (propios de este objeto):")
        instancia = vars(self.serie) if hasattr(self.serie, '__dict__') else {}
        print(f"  Cantidad: {len(instancia)}")
        
        # Atributos de clase (compartidos por todas las Series)
        print("\nATRIBUTOS DE CLASE (compartidos por todas las Series):")
        print(f"  __name__: {pd.Series.__name__}")
        print(f"  __module__: {pd.Series.__module__}")


def demostrar_constructores():
    """
    Demuestra las diferentes formas de construir una Serie.
    En POO, estos son diferentes "constructores" o formas de instanciar.
    """
    print("\n" + "="*70)
    print("CONSTRUCTORES: Diferentes formas de crear Series")
    print("="*70)
    
    ejemplos = []
    
    # 1. Desde lista
    s1 = pd.Series([1, 2, 3, 4, 5])
    ejemplos.append(("Lista", s1))
    
    # 2. Desde diccionario
    s2 = pd.Series({'a': 10, 'b': 20, 'c': 30})
    ejemplos.append(("Diccionario", s2))
    
    # 3. Desde escalar
    s3 = pd.Series(100, index=['x', 'y', 'z'])
    ejemplos.append(("Escalar", s3))
    
    # 4. Desde array NumPy
    s4 = pd.Series(np.array([1.1, 2.2, 3.3]))
    ejemplos.append(("NumPy array", s4))
    
    # 5. Con índice personalizado
    s5 = pd.Series([10, 20, 30], index=['primero', 'segundo', 'tercero'], name='valores')
    ejemplos.append(("Con índice y nombre", s5))
    
    # 6. Con dtype específico
    s6 = pd.Series([1, 2, 3], dtype='float64')
    ejemplos.append(("Con dtype específico", s6))
    
    for nombre, serie in ejemplos:
        print(f"\n{nombre}:")
        print(f"  dtype: {serie.dtype}")
        print(f"  index: {serie.index.tolist()}")
        print(f"  values: {serie.values}")


def demostrar_propiedades():
    """
    Demuestra las propiedades (properties) de Series.
    Las propiedades son atributos calculados dinámicamente.
    """
    print("\n" + "="*70)
    print("PROPIEDADES: Atributos calculados dinámicamente")
    print("="*70)
    
    serie = pd.Series([10, 20, 30, 40, 50], name='datos')
    
    print("\nPropiedades de solo lectura (no se pueden modificar):")
    propiedades_readonly = {
        'values': serie.values,
        'size': serie.size,
        'shape': serie.shape,
        'ndim': serie.ndim,
        'empty': serie.empty,
        'hasnans': serie.hasnans,
    }
    
    for nombre, valor in propiedades_readonly.items():
        print(f"  {nombre}: {valor}")
    
    print("\nPropiedades modificables:")
    print(f"  name (original): {serie.name}")
    serie.name = 'datos_modificados'
    print(f"  name (modificado): {serie.name}")
    
    print(f"\n  index (original): {serie.index.tolist()}")
    serie.index = ['a', 'b', 'c', 'd', 'e']
    print(f"  index (modificado): {serie.index.tolist()}")


def demostrar_metodos_acceso():
    """
    Demuestra los métodos de acceso a datos en Series.
    """
    print("\n" + "="*70)
    print("MÉTODOS DE ACCESO A DATOS")
    print("="*70)
    
    serie = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    
    print("\nSerie original:")
    print(serie)
    
    print("\n1. Acceso por posición (iloc):")
    print(f"   serie.iloc[0] = {serie.iloc[0]}")
    print(f"   serie.iloc[1:3] =\n{serie.iloc[1:3]}")
    
    print("\n2. Acceso por etiqueta (loc):")
    print(f"   serie.loc['a'] = {serie.loc['a']}")
    print(f"   serie.loc['b':'d'] =\n{serie.loc['b':'d']}")
    
    print("\n3. Acceso directo con [] (funciona con ambos):")
    print(f"   serie['a'] = {serie['a']}")
    print(f"   serie[0] = {serie[0]}")
    
    print("\n4. Acceso con at e iat (más rápido para valores únicos):")
    print(f"   serie.at['a'] = {serie.at['a']}")
    print(f"   serie.iat[0] = {serie.iat[0]}")


def demostrar_metodos_estadisticos():
    """
    Demuestra los métodos estadísticos de Series.
    Estos son métodos de instancia que calculan estadísticas.
    """
    print("\n" + "="*70)
    print("MÉTODOS ESTADÍSTICOS")
    print("="*70)
    
    serie = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    
    print(f"Serie: {serie.tolist()}")
    print("\nEstadísticas descriptivas:")
    
    metodos = {
        'sum': serie.sum,
        'mean': serie.mean,
        'median': serie.median,
        'std': serie.std,
        'var': serie.var,
        'min': serie.min,
        'max': serie.max,
        'count': serie.count,
        'quantile (0.25)': lambda: serie.quantile(0.25),
        'quantile (0.75)': lambda: serie.quantile(0.75),
    }
    
    for nombre, metodo in metodos.items():
        resultado = metodo()
        print(f"  {nombre}: {resultado}")


def demostrar_encapsulamiento():
    """
    Demuestra el encapsulamiento en Series.
    Algunos atributos internos no deberían modificarse directamente.
    """
    print("\n" + "="*70)
    print("ENCAPSULAMIENTO: Atributos públicos vs privados")
    print("="*70)
    
    serie = pd.Series([1, 2, 3, 4, 5])
    
    # Atributos públicos (recomendado usar)
    print("\nATRIBUTOS PÚBLICOS (usar estos):")
    print(f"  serie.values: {serie.values}")
    print(f"  serie.index: {serie.index}")
    print(f"  serie.dtype: {serie.dtype}")
    
    # Atributos "privados" (comienzan con _)
    print("\nATRIBUTOS 'PRIVADOS' (no usar directamente):")
    atributos_privados = [attr for attr in dir(serie) if attr.startswith('_') and not attr.startswith('__')]
    print(f"  Cantidad: {len(atributos_privados)}")
    print(f"  Ejemplos: {atributos_privados[:5]}")
    
    print("\n💡 En POO, los atributos que comienzan con _ son")
    print("   'privados' y no deberían accederse directamente.")


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 1: SERIES - EL OBJETO FUNDAMENTAL")
    print("="*70)
    
    # Crear una serie para análisis
    mi_serie = pd.Series([10, 20, 30, 40, 50], 
                         index=['a', 'b', 'c', 'd', 'e'],
                         name='ventas')
    
    # Usar la clase AnalizadorSeries
    analizador = AnalizadorSeries(mi_serie)
    analizador.anatomia_completa()
    analizador.mostrar_atributos_de_clase()
    
    # Demostrar constructores
    demostrar_constructores()
    
    # Demostrar propiedades
    demostrar_propiedades()
    
    # Demostrar métodos de acceso
    demostrar_metodos_acceso()
    
    # Demostrar métodos estadísticos
    demostrar_metodos_estadisticos()
    
    # Demostrar encapsulamiento
    demostrar_encapsulamiento()

