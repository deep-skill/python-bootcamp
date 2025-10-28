"""
Módulo 2: DataFrame - Colección de Series
==========================================
Exploración del DataFrame como composición de Series desde perspectiva de POO.
"""

import pandas as pd
import numpy as np


def anatomia_dataframe(df):
    """
    Muestra la anatomía completa de un DataFrame.
    
    Args:
        df: Un objeto pd.DataFrame
    """
    print("="*70)
    print("ANATOMÍA COMPLETA DEL DATAFRAME")
    print("="*70)
    
    print("\n1. IDENTIDAD DEL OBJETO:")
    print(f"   Tipo: {type(df)}")
    print(f"   Clase: {df.__class__.__name__}")
    print(f"   ID en memoria: {id(df)}")
    
    print("\n2. ATRIBUTOS DE DATOS:")
    print(f"   values (array 2D):\n{df.values}")
    print(f"\n   index (filas): {df.index}")
    print(f"   columns (columnas): {df.columns}")
    print(f"   dtypes:\n{df.dtypes}")
    
    print("\n3. ATRIBUTOS DE FORMA:")
    print(f"   shape: {df.shape}")
    print(f"   size: {df.size}")
    print(f"   ndim: {df.ndim}")
    print(f"   empty: {df.empty}")
    
    print("\n4. COMPOSICIÓN (columnas como Series):")
    print(f"   Número de columnas: {len(df.columns)}")
    for col in df.columns:
        print(f"   - '{col}': tipo={type(df[col]).__name__}, dtype={df[col].dtype}")


def demostrar_composicion():
    """
    Demuestra cómo DataFrame es una composición de Series.
    """
    print("\n" + "="*70)
    print("COMPOSICIÓN: DataFrame contiene Series")
    print("="*70)
    
    # Crear DataFrame
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
        'edad': [25, 30, 28, 35],
        'salario': [30000, 45000, 38000, 52000],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
    })
    
    print("\nDataFrame completo:")
    print(df)
    print(f"\nTipo: {type(df)}")
    
    # Acceder a una columna (retorna Series)
    print("\n" + "-"*70)
    print("Accediendo a columna 'edad':")
    columna_edad = df['edad']
    print(f"Tipo: {type(columna_edad)}")
    print(f"Es una Series: {isinstance(columna_edad, pd.Series)}")
    print(f"Contenido:\n{columna_edad}")
    
    # La columna tiene todos los métodos de Series
    print(f"\nMétodos de Series disponibles:")
    print(f"  mean(): {columna_edad.mean()}")
    print(f"  max(): {columna_edad.max()}")
    print(f"  min(): {columna_edad.min()}")
    
    # Todas las columnas son Series
    print("\n" + "-"*70)
    print("Verificando que todas las columnas son Series:")
    for col_name in df.columns:
        col = df[col_name]
        print(f"  {col_name}: {isinstance(col, pd.Series)}")


def demostrar_constructores():
    """
    Demuestra las diferentes formas de crear DataFrames.
    """
    print("\n" + "="*70)
    print("CONSTRUCTORES: Diferentes formas de crear DataFrame")
    print("="*70)
    
    # 1. Desde diccionario de listas
    print("\n1. Desde diccionario de listas:")
    df1 = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })
    print(df1)
    
    # 2. Desde lista de diccionarios
    print("\n2. Desde lista de diccionarios:")
    df2 = pd.DataFrame([
        {'nombre': 'Ana', 'edad': 25},
        {'nombre': 'Luis', 'edad': 30},
        {'nombre': 'María', 'edad': 28}
    ])
    print(df2)
    
    # 3. Desde diccionario de Series
    print("\n3. Desde diccionario de Series:")
    df3 = pd.DataFrame({
        'ventas': pd.Series([100, 200, 300]),
        'costos': pd.Series([50, 80, 120])
    })
    print(df3)
    
    # 4. Desde array de NumPy
    print("\n4. Desde array de NumPy:")
    df4 = pd.DataFrame(
        np.random.randn(3, 4),
        columns=['A', 'B', 'C', 'D'],
        index=['fila1', 'fila2', 'fila3']
    )
    print(df4)
    
    # 5. Desde otro DataFrame
    print("\n5. Desde otro DataFrame (copia):")
    df5 = pd.DataFrame(df1)
    print(df5)
    print(f"¿Es el mismo objeto? {df1 is df5}")
    print(f"¿Tienen mismos valores? {df1.equals(df5)}")


def demostrar_atributos():
    """
    Demuestra los atributos principales de DataFrame.
    """
    print("\n" + "="*70)
    print("ATRIBUTOS PRINCIPALES DE DATAFRAME")
    print("="*70)
    
    df = pd.DataFrame({
        'producto': ['A', 'B', 'C', 'D'],
        'precio': [10.5, 20.0, 15.75, 30.25],
        'stock': [100, 50, 75, 25]
    }, index=['P1', 'P2', 'P3', 'P4'])
    
    print("\nDataFrame:")
    print(df)
    
    print("\n📊 ATRIBUTOS DE DATOS:")
    print(f"values (array 2D):\n{df.values}")
    print(f"values.dtype: {df.values.dtype}")
    
    print("\n🏷️  ATRIBUTOS DE ÍNDICES:")
    print(f"index: {df.index}")
    print(f"index.name: {df.index.name}")
    print(f"columns: {df.columns}")
    print(f"columns.name: {df.columns.name}")
    print(f"axes: {df.axes}")
    
    print("\n📏 ATRIBUTOS DE FORMA:")
    print(f"shape: {df.shape}")
    print(f"size: {df.size}")
    print(f"ndim: {df.ndim}")
    print(f"empty: {df.empty}")
    
    print("\n🔤 ATRIBUTOS DE TIPOS:")
    print(f"dtypes:\n{df.dtypes}")


def demostrar_acceso_datos():
    """
    Demuestra los métodos de acceso a datos en DataFrame.
    """
    print("\n" + "="*70)
    print("MÉTODOS DE ACCESO A DATOS")
    print("="*70)
    
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    }, index=['fila1', 'fila2', 'fila3', 'fila4'])
    
    print("DataFrame original:")
    print(df)
    
    print("\n1. ACCESO A COLUMNAS:")
    print(f"df['A'] (retorna Series):\n{df['A']}")
    print(f"\ndf[['A', 'C']] (retorna DataFrame):\n{df[['A', 'C']]}")
    
    print("\n2. ACCESO CON loc (por etiqueta):")
    print(f"df.loc['fila1'] (retorna Series):\n{df.loc['fila1']}")
    print(f"\ndf.loc['fila1', 'A']: {df.loc['fila1', 'A']}")
    print(f"\ndf.loc['fila1':'fila3', 'A':'B']:\n{df.loc['fila1':'fila3', 'A':'B']}")
    
    print("\n3. ACCESO CON iloc (por posición):")
    print(f"df.iloc[0] (retorna Series):\n{df.iloc[0]}")
    print(f"\ndf.iloc[0, 0]: {df.iloc[0, 0]}")
    print(f"\ndf.iloc[0:2, 0:2]:\n{df.iloc[0:2, 0:2]}")
    
    print("\n4. ACCESO CON at/iat (valores únicos):")
    print(f"df.at['fila1', 'A']: {df.at['fila1', 'A']}")
    print(f"df.iat[0, 0]: {df.iat[0, 0]}")


def demostrar_metodos_agregacion():
    """
    Demuestra métodos de agregación en DataFrame.
    """
    print("\n" + "="*70)
    print("MÉTODOS DE AGREGACIÓN")
    print("="*70)
    
    df = pd.DataFrame({
        'ventas': [100, 200, 150, 300],
        'costos': [50, 80, 60, 120],
        'ganancia': [50, 120, 90, 180]
    }, index=['Q1', 'Q2', 'Q3', 'Q4'])
    
    print("DataFrame:")
    print(df)
    
    print("\n1. Agregación por COLUMNAS (axis=0, default):")
    print(f"sum():\n{df.sum()}")
    print(f"\nmean():\n{df.mean()}")
    
    print("\n2. Agregación por FILAS (axis=1):")
    print(f"sum(axis=1):\n{df.sum(axis=1)}")
    print(f"\nmean(axis=1):\n{df.mean(axis=1)}")
    
    print("\n3. Describe (resumen estadístico):")
    print(df.describe())


def demostrar_relacion_series_dataframe():
    """
    Demuestra la relación bidireccional entre Series y DataFrame.
    """
    print("\n" + "="*70)
    print("RELACIÓN SERIES ↔ DATAFRAME")
    print("="*70)
    
    # DataFrame → Series
    print("\n1. DataFrame → Series (acceso a columna):")
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    print(f"DataFrame:\n{df}")
    serie = df['A']
    print(f"\nColumna 'A' (Series):\n{serie}")
    
    # Series → DataFrame
    print("\n2. Series → DataFrame (to_frame()):")
    df_from_series = serie.to_frame()
    print(f"DataFrame desde Series:\n{df_from_series}")
    print(f"Tipo: {type(df_from_series)}")
    
    # Múltiples Series → DataFrame
    print("\n3. Múltiples Series → DataFrame:")
    s1 = pd.Series([1, 2, 3], name='col1')
    s2 = pd.Series([4, 5, 6], name='col2')
    s3 = pd.Series([7, 8, 9], name='col3')
    
    df_from_multiple = pd.DataFrame({
        s1.name: s1,
        s2.name: s2,
        s3.name: s3
    })
    print(df_from_multiple)


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 2: DATAFRAME - COLECCIÓN DE SERIES")
    print("="*70)
    
    # Crear DataFrame de ejemplo
    df_ejemplo = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María'],
        'edad': [25, 30, 28],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia']
    })
    
    # Demostrar conceptos
    anatomia_dataframe(df_ejemplo)
    demostrar_composicion()
    demostrar_constructores()
    demostrar_atributos()
    demostrar_acceso_datos()
    demostrar_metodos_agregacion()
    demostrar_relacion_series_dataframe()

