"""
Módulo 3B: Sintaxis de Índices - Guía Práctica Completa
========================================================
Guía detallada sobre cómo usar índices en Series y DataFrames.
"""

import pandas as pd
import numpy as np


def introduccion_indices():
    """
    Introducción a los índices en Pandas.
    """
    print("="*70)
    print("ÍNDICES EN PANDAS: CONCEPTOS FUNDAMENTALES")
    print("="*70)
    
    print("""
Los ÍNDICES son etiquetas que permiten identificar y acceder a datos:

EN SERIES:
- Una Serie tiene UN índice (para las filas)
- Por defecto: RangeIndex(0, 1, 2, 3, ...)
- Puede ser personalizado con cualquier valor

EN DATAFRAMES:
- Un DataFrame tiene DOS índices:
  1. Index para FILAS (df.index)
  2. Index para COLUMNAS (df.columns)
- Ambos son objetos Index

VENTAJAS DE LOS ÍNDICES:
✓ Acceso rápido por etiqueta
✓ Alineación automática en operaciones
✓ Agrupación y agregación eficiente
✓ Series temporales con fechas
    """)


def sintaxis_basica_series():
    """
    Sintaxis básica de índices en Series.
    """
    print("\n" + "="*70)
    print("SINTAXIS BÁSICA: ÍNDICES EN SERIES")
    print("="*70)
    
    # Serie con índice por defecto
    serie_default = pd.Series([10, 20, 30, 40, 50])
    print("\n1. ÍNDICE POR DEFECTO (RangeIndex):")
    print(serie_default)
    print(f"\nTipo de índice: {type(serie_default.index)}")
    print(f"Índice: {serie_default.index}")
    
    # Serie con índice personalizado
    serie_custom = pd.Series(
        [10, 20, 30, 40, 50],
        index=['a', 'b', 'c', 'd', 'e']
    )
    print("\n2. ÍNDICE PERSONALIZADO:")
    print(serie_custom)
    print(f"Índice: {serie_custom.index.tolist()}")
    
    # Acceso por índice
    print("\n3. FORMAS DE ACCEDER A DATOS:")
    print(f"   serie_custom['a'] = {serie_custom['a']}")
    print(f"   serie_custom.loc['a'] = {serie_custom.loc['a']}")
    print(f"   serie_custom.iloc[0] = {serie_custom.iloc[0]}")
    
    # Slicing con índice
    print("\n4. SLICING CON ÍNDICES:")
    print(f"   serie_custom['a':'c'] (INCLUYE el final):")
    print(serie_custom['a':'c'])
    
    print(f"\n   serie_custom.iloc[0:3] (EXCLUYE el final):")
    print(serie_custom.iloc[0:3])


def acceso_series_detallado():
    """
    Guía detallada de acceso a Series.
    """
    print("\n" + "="*70)
    print("GUÍA COMPLETA: ACCESO A SERIES")
    print("="*70)
    
    serie = pd.Series(
        [100, 200, 300, 400, 500],
        index=['ene', 'feb', 'mar', 'abr', 'may'],
        name='ventas'
    )
    
    print("Serie de ejemplo:")
    print(serie)
    
    # 1. Acceso por etiqueta con []
    print("\n" + "-"*70)
    print("1. ACCESO DIRECTO CON [] (por etiqueta)")
    print("-"*70)
    print(f"serie['feb'] = {serie['feb']}")
    print(f"Tipo: {type(serie['feb'])}")
    
    # 2. Acceso múltiple
    print("\n2. ACCESO MÚLTIPLE:")
    print(f"serie[['ene', 'mar', 'may']]:")
    print(serie[['ene', 'mar', 'may']])
    print(f"Tipo: {type(serie[['ene', 'mar', 'may']])}")
    
    # 3. Slicing con etiquetas
    print("\n3. SLICING CON ETIQUETAS (incluye ambos extremos):")
    print(f"serie['feb':'abr']:")
    print(serie['feb':'abr'])
    
    # 4. loc - acceso por etiqueta (explícito)
    print("\n4. .loc[] - ACCESO POR ETIQUETA (explícito):")
    print(f"serie.loc['feb'] = {serie.loc['feb']}")
    print(f"serie.loc['feb':'abr']:")
    print(serie.loc['feb':'abr'])
    
    # 5. iloc - acceso por posición
    print("\n5. .iloc[] - ACCESO POR POSICIÓN (índice numérico):")
    print(f"serie.iloc[1] = {serie.iloc[1]}")
    print(f"serie.iloc[1:4]:")
    print(serie.iloc[1:4])
    print(f"serie.iloc[-1] = {serie.iloc[-1]}")
    
    # 6. at/iat - acceso rápido a un solo valor
    print("\n6. .at[] / .iat[] - ACCESO RÁPIDO (solo un valor):")
    print(f"serie.at['feb'] = {serie.at['feb']}")
    print(f"serie.iat[1] = {serie.iat[1]}")
    print("💡 at/iat son ~2x más rápidos para un solo valor")


def sintaxis_basica_dataframe():
    """
    Sintaxis básica de índices en DataFrames.
    """
    print("\n" + "="*70)
    print("SINTAXIS BÁSICA: ÍNDICES EN DATAFRAMES")
    print("="*70)
    
    # DataFrame simple
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
        'edad': [25, 30, 28, 35],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
    })
    
    print("\n1. DATAFRAME CON ÍNDICES POR DEFECTO:")
    print(df)
    print(f"\nÍndice de filas: {df.index}")
    print(f"Índice de columnas: {df.columns.tolist()}")
    
    # DataFrame con índice personalizado
    df_custom = pd.DataFrame({
        'edad': [25, 30, 28, 35],
        'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
    }, index=['Ana', 'Luis', 'María', 'Carlos'])
    
    print("\n2. DATAFRAME CON ÍNDICE PERSONALIZADO:")
    print(df_custom)
    print(f"\nÍndice de filas: {df_custom.index.tolist()}")
    
    # Establecer índice desde columna
    print("\n3. ESTABLECER ÍNDICE DESDE COLUMNA:")
    df_indexed = df.set_index('nombre')
    print(df_indexed)
    print(f"\nÍndice de filas: {df_indexed.index.tolist()}")
    
    # Resetear índice
    print("\n4. RESETEAR ÍNDICE (volver a RangeIndex):")
    df_reset = df_indexed.reset_index()
    print(df_reset)


def acceso_dataframe_columnas():
    """
    Acceso a columnas en DataFrame.
    """
    print("\n" + "="*70)
    print("ACCESO A COLUMNAS EN DATAFRAME")
    print("="*70)
    
    df = pd.DataFrame({
        'producto': ['A', 'B', 'C', 'D'],
        'precio': [10.5, 20.0, 15.75, 30.25],
        'stock': [100, 50, 75, 25],
        'categoria': ['X', 'Y', 'X', 'Y']
    })
    
    print("DataFrame:")
    print(df)
    
    # 1. Acceso a una columna con []
    print("\n1. ACCESO A UNA COLUMNA CON []:")
    print(f"df['precio'] (retorna Series):")
    print(df['precio'])
    print(f"Tipo: {type(df['precio'])}")
    
    # 2. Acceso como atributo
    print("\n2. ACCESO COMO ATRIBUTO (si el nombre es válido):")
    print(f"df.precio:")
    print(df.precio)
    print("⚠️ Solo funciona si el nombre no tiene espacios ni caracteres especiales")
    
    # 3. Acceso a múltiples columnas
    print("\n3. ACCESO A MÚLTIPLES COLUMNAS (retorna DataFrame):")
    print(f"df[['producto', 'precio']]:")
    print(df[['producto', 'precio']])
    print(f"Tipo: {type(df[['producto', 'precio']])}")
    
    # 4. Reordenar columnas
    print("\n4. REORDENAR COLUMNAS:")
    df_reordenado = df[['producto', 'stock', 'precio', 'categoria']]
    print(df_reordenado)
    
    # 5. Seleccionar y renombrar
    print("\n5. SELECCIONAR Y RENOMBRAR COLUMNAS:")
    df_rename = df[['producto', 'precio']].rename(columns={'producto': 'item'})
    print(df_rename)


def acceso_dataframe_filas():
    """
    Acceso a filas en DataFrame.
    """
    print("\n" + "="*70)
    print("ACCESO A FILAS EN DATAFRAME")
    print("="*70)
    
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
        'edad': [25, 30, 28, 35],
        'salario': [30000, 45000, 38000, 52000]
    }, index=['E001', 'E002', 'E003', 'E004'])
    
    print("DataFrame:")
    print(df)
    
    # 1. Slicing de filas con []
    print("\n1. SLICING DE FILAS CON []:")
    print(f"df[0:2] (primeras 2 filas por posición):")
    print(df[0:2])
    print(f"\ndf['E001':'E003'] (por etiqueta, INCLUYE el final):")
    print(df['E001':'E003'])
    
    # 2. loc - por etiqueta de fila
    print("\n2. .loc[] - POR ETIQUETA DE FILA:")
    print(f"df.loc['E002'] (retorna Series):")
    print(df.loc['E002'])
    
    print(f"\ndf.loc[['E001', 'E003']] (retorna DataFrame):")
    print(df.loc[['E001', 'E003']])
    
    print(f"\ndf.loc['E001':'E003'] (slicing con etiquetas):")
    print(df.loc['E001':'E003'])
    
    # 3. iloc - por posición de fila
    print("\n3. .iloc[] - POR POSICIÓN DE FILA:")
    print(f"df.iloc[1] (segunda fila, retorna Series):")
    print(df.iloc[1])
    
    print(f"\ndf.iloc[[0, 2]] (filas 1 y 3, retorna DataFrame):")
    print(df.iloc[[0, 2]])
    
    print(f"\ndf.iloc[1:3] (filas 2 y 3, EXCLUYE el final):")
    print(df.iloc[1:3])


def acceso_dataframe_bidimensional():
    """
    Acceso bidimensional en DataFrame (filas y columnas).
    """
    print("\n" + "="*70)
    print("ACCESO BIDIMENSIONAL: FILAS Y COLUMNAS")
    print("="*70)
    
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12],
        'D': [13, 14, 15, 16]
    }, index=['fila1', 'fila2', 'fila3', 'fila4'])
    
    print("DataFrame:")
    print(df)
    
    # loc - etiquetas [filas, columnas]
    print("\n1. .loc[FILAS, COLUMNAS] - POR ETIQUETAS:")
    print("\na) Un valor específico:")
    print(f"df.loc['fila2', 'B'] = {df.loc['fila2', 'B']}")
    
    print("\nb) Una fila, múltiples columnas:")
    print(f"df.loc['fila2', ['A', 'C']]:")
    print(df.loc['fila2', ['A', 'C']])
    
    print("\nc) Múltiples filas, una columna:")
    print(f"df.loc[['fila1', 'fila3'], 'B']:")
    print(df.loc[['fila1', 'fila3'], 'B'])
    
    print("\nd) Múltiples filas y columnas:")
    print(f"df.loc[['fila1', 'fila3'], ['A', 'C']]:")
    print(df.loc[['fila1', 'fila3'], ['A', 'C']])
    
    print("\ne) Slicing de filas y columnas:")
    print(f"df.loc['fila1':'fila3', 'A':'C']:")
    print(df.loc['fila1':'fila3', 'A':'C'])
    
    print("\nf) Todas las filas, algunas columnas:")
    print(f"df.loc[:, ['A', 'C']]:")
    print(df.loc[:, ['A', 'C']])
    
    # iloc - posiciones [filas, columnas]
    print("\n2. .iloc[FILAS, COLUMNAS] - POR POSICIONES:")
    print("\na) Un valor específico:")
    print(f"df.iloc[1, 1] = {df.iloc[1, 1]}")
    
    print("\nb) Una fila, múltiples columnas:")
    print(f"df.iloc[1, [0, 2]]:")
    print(df.iloc[1, [0, 2]])
    
    print("\nc) Múltiples filas, una columna:")
    print(f"df.iloc[[0, 2], 1]:")
    print(df.iloc[[0, 2], 1])
    
    print("\nd) Slicing de filas y columnas:")
    print(f"df.iloc[0:3, 0:2]:")
    print(df.iloc[0:3, 0:2])
    
    print("\ne) Todas las filas, algunas columnas:")
    print(f"df.iloc[:, [0, 2]]:")
    print(df.iloc[:, [0, 2]])


def filtrado_con_indices():
    """
    Filtrado usando índices booleanos.
    """
    print("\n" + "="*70)
    print("FILTRADO CON ÍNDICES BOOLEANOS")
    print("="*70)
    
    df = pd.DataFrame({
        'producto': ['A', 'B', 'C', 'D', 'E'],
        'precio': [10, 25, 15, 30, 20],
        'stock': [100, 50, 75, 25, 60]
    })
    
    print("DataFrame:")
    print(df)
    
    # 1. Crear máscara booleana
    print("\n1. CREAR MÁSCARA BOOLEANA:")
    mascara = df['precio'] > 15
    print(f"mascara = df['precio'] > 15:")
    print(mascara)
    
    # 2. Aplicar máscara
    print("\n2. APLICAR MÁSCARA:")
    print(f"df[mascara]:")
    print(df[mascara])
    
    # 3. Filtrado en una línea
    print("\n3. FILTRADO EN UNA LÍNEA:")
    print(f"df[df['precio'] > 15]:")
    print(df[df['precio'] > 15])
    
    # 4. Múltiples condiciones con & (AND)
    print("\n4. MÚLTIPLES CONDICIONES CON & (AND):")
    print(f"df[(df['precio'] > 15) & (df['stock'] > 50)]:")
    print(df[(df['precio'] > 15) & (df['stock'] > 50)])
    
    # 5. Múltiples condiciones con | (OR)
    print("\n5. MÚLTIPLES CONDICIONES CON | (OR):")
    print(f"df[(df['precio'] < 15) | (df['stock'] < 50)]:")
    print(df[(df['precio'] < 15) | (df['stock'] < 50)])
    
    # 6. Negación con ~
    print("\n6. NEGACIÓN CON ~:")
    print(f"df[~(df['precio'] > 15)] (precio NO mayor que 15):")
    print(df[~(df['precio'] > 15)])
    
    # 7. isin() para valores en lista
    print("\n7. .isin() - VALORES EN LISTA:")
    print(f"df[df['producto'].isin(['A', 'C', 'E'])]:")
    print(df[df['producto'].isin(['A', 'C', 'E'])])


def modificacion_con_indices():
    """
    Modificar datos usando índices.
    """
    print("\n" + "="*70)
    print("MODIFICACIÓN DE DATOS CON ÍNDICES")
    print("="*70)
    
    df = pd.DataFrame({
        'producto': ['A', 'B', 'C'],
        'precio': [10, 20, 15],
        'stock': [100, 50, 75]
    }, index=['P1', 'P2', 'P3'])
    
    print("DataFrame original:")
    print(df)
    
    # 1. Modificar un valor
    print("\n1. MODIFICAR UN VALOR ESPECÍFICO:")
    df_mod = df.copy()
    df_mod.loc['P2', 'precio'] = 25
    print(f"df.loc['P2', 'precio'] = 25:")
    print(df_mod)
    
    # 2. Modificar una columna completa
    print("\n2. MODIFICAR UNA COLUMNA COMPLETA:")
    df_mod = df.copy()
    df_mod['precio'] = df_mod['precio'] * 1.10
    print(f"df['precio'] = df['precio'] * 1.10:")
    print(df_mod)
    
    # 3. Modificar una fila completa
    print("\n3. MODIFICAR UNA FILA COMPLETA:")
    df_mod = df.copy()
    df_mod.loc['P2'] = ['X', 999, 999]
    print(f"df.loc['P2'] = ['X', 999, 999]:")
    print(df_mod)
    
    # 4. Modificar con condición
    print("\n4. MODIFICAR CON CONDICIÓN:")
    df_mod = df.copy()
    df_mod.loc[df_mod['stock'] < 60, 'stock'] = 100
    print(f"df.loc[df['stock'] < 60, 'stock'] = 100:")
    print(df_mod)
    
    # 5. Agregar nueva columna
    print("\n5. AGREGAR NUEVA COLUMNA:")
    df_mod = df.copy()
    df_mod['total'] = df_mod['precio'] * df_mod['stock']
    print(f"df['total'] = df['precio'] * df['stock']:")
    print(df_mod)
    
    # 6. Agregar nueva fila
    print("\n6. AGREGAR NUEVA FILA:")
    df_mod = df.copy()
    df_mod.loc['P4'] = ['D', 30, 40]
    print(f"df.loc['P4'] = ['D', 30, 40]:")
    print(df_mod)


def indices_multiindex():
    """
    Trabajar con MultiIndex (índices jerárquicos).
    """
    print("\n" + "="*70)
    print("MULTIINDEX: ÍNDICES JERÁRQUICOS")
    print("="*70)
    
    # Crear MultiIndex
    arrays = [
        ['España', 'España', 'Francia', 'Francia', 'Italia', 'Italia'],
        ['Madrid', 'Barcelona', 'París', 'Lyon', 'Roma', 'Milán']
    ]
    index = pd.MultiIndex.from_arrays(arrays, names=['país', 'ciudad'])
    
    df = pd.DataFrame({
        'población': [3200000, 1600000, 2200000, 500000, 2800000, 1400000],
        'area_km2': [604, 101, 105, 48, 1285, 181]
    }, index=index)
    
    print("DataFrame con MultiIndex:")
    print(df)
    
    # 1. Acceso a nivel superior
    print("\n1. ACCESO A NIVEL SUPERIOR:")
    print(f"df.loc['España']:")
    print(df.loc['España'])
    
    # 2. Acceso a nivel específico
    print("\n2. ACCESO A NIVEL ESPECÍFICO:")
    print(f"df.loc[('España', 'Madrid')]:")
    print(df.loc[('España', 'Madrid')])
    
    # 3. Acceso con slice
    print("\n3. ACCESO CON SLICE:")
    print(f"df.loc[('España', slice(None)), :]:")
    print(df.loc[('España', slice(None)), :])
    
    # 4. Cross-section (xs)
    print("\n4. CROSS-SECTION (xs):")
    print(f"df.xs('España', level='país'):")
    print(df.xs('España', level='país'))


def ejemplos_practicos():
    """
    Ejemplos prácticos combinando diferentes técnicas.
    """
    print("\n" + "="*70)
    print("EJEMPLOS PRÁCTICOS COMPLETOS")
    print("="*70)
    
    # Datos de ventas
    df = pd.DataFrame({
        'fecha': pd.date_range('2024-01-01', periods=10, freq='D'),
        'producto': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
        'cantidad': [10, 15, 12, 8, 20, 11, 9, 18, 13, 7],
        'precio': [100, 150, 100, 200, 150, 100, 200, 150, 100, 200]
    })
    
    print("Datos de ventas:")
    print(df)
    
    # Ejemplo 1: Filtrar y calcular
    print("\n1. VENTAS DE PRODUCTO 'A' CON CANTIDAD > 10:")
    resultado = df[(df['producto'] == 'A') & (df['cantidad'] > 10)]
    print(resultado)
    
    # Ejemplo 2: Agrupar por producto
    print("\n2. TOTAL DE VENTAS POR PRODUCTO:")
    df['total'] = df['cantidad'] * df['precio']
    ventas_por_producto = df.groupby('producto')['total'].sum()
    print(ventas_por_producto)
    
    # Ejemplo 3: Usar fecha como índice
    print("\n3. USAR FECHA COMO ÍNDICE:")
    df_fecha = df.set_index('fecha')
    print(df_fecha.head())
    print(f"\nAcceso por fecha: df_fecha.loc['2024-01-05']:")
    print(df_fecha.loc['2024-01-05'])
    
    # Ejemplo 4: Selección compleja
    print("\n4. PRODUCTOS B O C CON CANTIDAD > 10:")
    resultado = df[df['producto'].isin(['B', 'C']) & (df['cantidad'] > 10)]
    print(resultado[['fecha', 'producto', 'cantidad']])


def comparacion_metodos_acceso():
    """
    Tabla comparativa de métodos de acceso.
    """
    print("\n" + "="*70)
    print("RESUMEN: COMPARACIÓN DE MÉTODOS DE ACCESO")
    print("="*70)
    
    print("""
╔════════════╦═══════════════╦════════════════╦════════════════╗
║ Método     ║ Tipo Acceso   ║ Retorna        ║ Uso Principal  ║
╠════════════╬═══════════════╬════════════════╬════════════════╣
║ []         ║ Mixto         ║ Serie/DF       ║ Columnas, slice║
║ .loc[]     ║ Etiqueta      ║ Serie/DF/Valor ║ Por nombre     ║
║ .iloc[]    ║ Posición      ║ Serie/DF/Valor ║ Por número     ║
║ .at[]      ║ Etiqueta      ║ Valor escalar  ║ 1 valor rápido ║
║ .iat[]     ║ Posición      ║ Valor escalar  ║ 1 valor rápido ║
╚════════════╩═══════════════╩════════════════╩════════════════╝

REGLAS IMPORTANTES:

1. [] EN SERIES:
   - serie['etiqueta'] → acceso por etiqueta
   - serie[0:3] → slicing por posición (si índice numérico)

2. [] EN DATAFRAMES:
   - df['col'] → acceso a columna (retorna Series)
   - df[['col1', 'col2']] → columnas (retorna DataFrame)
   - df[0:3] → slicing de filas (por posición)
   - df['etiq1':'etiq3'] → slicing de filas (por etiqueta)

3. .loc[] (ETIQUETAS):
   - df.loc['fila'] → una fila
   - df.loc[:, 'col'] → una columna
   - df.loc['fila', 'col'] → un valor
   - df.loc['f1':'f3', 'c1':'c3'] → sub-DataFrame

4. .iloc[] (POSICIONES):
   - df.iloc[0] → primera fila
   - df.iloc[:, 0] → primera columna
   - df.iloc[0, 0] → primer valor
   - df.iloc[0:3, 0:2] → sub-DataFrame

5. DIFERENCIAS CLAVE:
   ✓ loc INCLUYE el final en slicing
   ✓ iloc EXCLUYE el final en slicing
   ✓ at/iat son ~2x más rápidos para un solo valor
   ✓ [] es más corto pero menos explícito

💡 RECOMENDACIÓN: Usa .loc[] y .iloc[] para código claro
    """)


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 3B: SINTAXIS DE ÍNDICES - GUÍA PRÁCTICA")
    print("="*70)
    
    introduccion_indices()
    sintaxis_basica_series()
    acceso_series_detallado()
    sintaxis_basica_dataframe()
    acceso_dataframe_columnas()
    acceso_dataframe_filas()
    acceso_dataframe_bidimensional()
    filtrado_con_indices()
    modificacion_con_indices()
    indices_multiindex()
    ejemplos_practicos()
    comparacion_metodos_acceso()

