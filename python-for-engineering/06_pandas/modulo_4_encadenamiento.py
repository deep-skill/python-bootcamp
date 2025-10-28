"""
Módulo 4: Métodos y Encadenamiento (Method Chaining)
=====================================================
Exploración del patrón Fluent Interface y method chaining en Pandas.
"""

import pandas as pd
import numpy as np


def demostrar_fluent_interface():
    """
    Demuestra el patrón Fluent Interface en Pandas.
    """
    print("="*70)
    print("FLUENT INTERFACE: Encadenamiento de métodos")
    print("="*70)
    
    # Crear DataFrame de ejemplo
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Laura'],
        'edad': [25, 30, 28, 35, 22],
        'salario': [30000, 45000, 38000, 52000, 28000],
        'departamento': ['IT', 'Ventas', 'IT', 'Ventas', 'IT']
    })
    
    print("\nDataFrame original:")
    print(df)
    
    # Forma tradicional (sin encadenamiento)
    print("\n" + "-"*70)
    print("FORMA TRADICIONAL (paso por paso):")
    df_filtrado = df[df['salario'] > 30000]
    df_ordenado = df_filtrado.sort_values('edad')
    df_final = df_ordenado[['nombre', 'edad', 'salario']]
    print(df_final)
    
    # Forma con encadenamiento
    print("\n" + "-"*70)
    print("FORMA CON ENCADENAMIENTO (method chaining):")
    resultado = (df
        .query('salario > 30000')
        .sort_values('edad')
        [['nombre', 'edad', 'salario']]
    )
    print(resultado)
    
    print("\n💡 Ambas formas producen el mismo resultado")
    print(f"Son iguales: {df_final.equals(resultado)}")


def demostrar_retorno_self():
    """
    Demuestra cómo los métodos retornan self o una copia.
    """
    print("\n" + "="*70)
    print("MÉTODOS QUE RETORNAN SELF VS COPIA")
    print("="*70)
    
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]
    })
    
    print("DataFrame original:")
    print(df)
    print(f"ID: {id(df)}")
    
    # Métodos que retornan COPIA (nuevo objeto)
    print("\n1. Métodos que retornan NUEVA COPIA:")
    df_copia = df.sort_values('A')
    print(f"   sort_values() - ID: {id(df_copia)}")
    print(f"   ¿Es el mismo objeto? {df is df_copia}")
    
    df_multiplicado = df * 2
    print(f"   operador * - ID: {id(df_multiplicado)}")
    print(f"   ¿Es el mismo objeto? {df is df_multiplicado}")
    
    # Métodos con inplace=True (modifican el original)
    print("\n2. Métodos con inplace=True (modifican original):")
    df_inplace = df.copy()
    print(f"   DataFrame antes: {df_inplace['A'].tolist()}")
    print(f"   ID antes: {id(df_inplace)}")
    
    resultado = df_inplace.sort_values('A', ascending=False, inplace=True)
    print(f"   sort_values(inplace=True) retorna: {resultado}")
    print(f"   DataFrame después: {df_inplace['A'].tolist()}")
    print(f"   ID después: {id(df_inplace)}")
    print(f"   💡 Con inplace=True, el método retorna None")


def demostrar_copy_vs_referencia():
    """
    Demuestra la diferencia entre copia y referencia.
    """
    print("\n" + "="*70)
    print("COPY VS REFERENCIA")
    print("="*70)
    
    df_original = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    
    print("DataFrame original:")
    print(df_original)
    print(f"ID: {id(df_original)}")
    
    # Referencia (mismo objeto)
    print("\n1. REFERENCIA (asignación simple):")
    df_ref = df_original
    print(f"   ID de df_ref: {id(df_ref)}")
    print(f"   ¿Es el mismo objeto? {df_original is df_ref}")
    
    df_ref.loc[0, 'A'] = 999
    print(f"\n   Modificando df_ref.loc[0, 'A'] = 999")
    print(f"   df_original también cambió: {df_original.loc[0, 'A']}")
    
    # Copia (nuevo objeto)
    df_original = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("\n2. COPIA (método copy()):")
    df_copia = df_original.copy()
    print(f"   ID de df_copia: {id(df_copia)}")
    print(f"   ¿Es el mismo objeto? {df_original is df_copia}")
    
    df_copia.loc[0, 'A'] = 999
    print(f"\n   Modificando df_copia.loc[0, 'A'] = 999")
    print(f"   df_original NO cambió: {df_original.loc[0, 'A']}")
    print(f"   df_copia sí cambió: {df_copia.loc[0, 'A']}")
    
    print("\n💡 Usar .copy() cuando quieras un objeto independiente")


def demostrar_pipe():
    """
    Demuestra el método pipe() para funciones personalizadas.
    """
    print("\n" + "="*70)
    print("MÉTODO PIPE: Aplicar funciones personalizadas")
    print("="*70)
    
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María'],
        'edad': [25, 30, 28],
        'salario': [30000, 45000, 38000]
    })
    
    print("DataFrame original:")
    print(df)
    
    # Definir funciones personalizadas
    def agregar_columna_senior(df):
        """Agrega columna indicando si es senior (>= 30 años)."""
        df = df.copy()
        df['es_senior'] = df['edad'] >= 30
        return df
    
    def calcular_salario_mensual(df):
        """Calcula salario mensual."""
        df = df.copy()
        df['salario_mensual'] = df['salario'] / 12
        return df
    
    def formatear_nombre(df):
        """Convierte nombres a mayúsculas."""
        df = df.copy()
        df['nombre'] = df['nombre'].str.upper()
        return df
    
    # Aplicar con pipe (encadenamiento)
    print("\nAplicando transformaciones con pipe():")
    resultado = (df
        .pipe(agregar_columna_senior)
        .pipe(calcular_salario_mensual)
        .pipe(formatear_nombre)
    )
    
    print(resultado)
    
    print("\n💡 pipe() permite encadenar funciones personalizadas")


def demostrar_assign():
    """
    Demuestra el método assign() para agregar/modificar columnas.
    """
    print("\n" + "="*70)
    print("MÉTODO ASSIGN: Agregar columnas en cadena")
    print("="*70)
    
    df = pd.DataFrame({
        'producto': ['A', 'B', 'C'],
        'precio': [10, 20, 15],
        'cantidad': [5, 3, 8]
    })
    
    print("DataFrame original:")
    print(df)
    
    # Sin assign (forma tradicional)
    print("\nForma tradicional:")
    df_trad = df.copy()
    df_trad['total'] = df_trad['precio'] * df_trad['cantidad']
    df_trad['con_iva'] = df_trad['total'] * 1.21
    print(df_trad)
    
    # Con assign (encadenable)
    print("\nCon assign (encadenable):")
    resultado = (df
        .assign(total=lambda x: x['precio'] * x['cantidad'])
        .assign(con_iva=lambda x: x['total'] * 1.21)
    )
    print(resultado)
    
    # Assign múltiples columnas a la vez
    print("\nAssign múltiples columnas:")
    resultado2 = df.assign(
        total=lambda x: x['precio'] * x['cantidad'],
        con_iva=lambda x: x['precio'] * x['cantidad'] * 1.21,
        descuento=lambda x: x['precio'] * 0.1
    )
    print(resultado2)


def demostrar_query():
    """
    Demuestra el método query() para filtrado expresivo.
    """
    print("\n" + "="*70)
    print("MÉTODO QUERY: Filtrado expresivo")
    print("="*70)
    
    df = pd.DataFrame({
        'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Laura'],
        'edad': [25, 30, 28, 35, 22],
        'salario': [30000, 45000, 38000, 52000, 28000],
        'departamento': ['IT', 'Ventas', 'IT', 'Ventas', 'IT']
    })
    
    print("DataFrame:")
    print(df)
    
    # Forma tradicional
    print("\nForma tradicional:")
    filtrado = df[(df['edad'] > 25) & (df['salario'] > 30000)]
    print(filtrado)
    
    # Con query
    print("\nCon query() (más legible):")
    filtrado_query = df.query('edad > 25 and salario > 30000')
    print(filtrado_query)
    
    # Query con variables externas
    print("\nQuery con variables externas:")
    edad_minima = 28
    salario_minimo = 35000
    filtrado_var = df.query('edad >= @edad_minima and salario >= @salario_minimo')
    print(filtrado_var)
    
    # Query con strings
    print("\nQuery con strings:")
    filtrado_dept = df.query('departamento == "IT"')
    print(filtrado_dept)


def ejemplo_completo_encadenamiento():
    """
    Ejemplo completo de encadenamiento de métodos.
    """
    print("\n" + "="*70)
    print("EJEMPLO COMPLETO: Análisis con encadenamiento")
    print("="*70)
    
    # Datos de ventas
    df = pd.DataFrame({
        'fecha': pd.date_range('2024-01-01', periods=20, freq='D'),
        'producto': ['A', 'B', 'C', 'A', 'B'] * 4,
        'ventas': np.random.randint(100, 1000, 20),
        'costo': np.random.randint(50, 500, 20)
    })
    
    print("Datos originales:")
    print(df.head(10))
    
    # Pipeline completo con encadenamiento
    print("\nPipeline de análisis:")
    resultado = (df
        .assign(ganancia=lambda x: x['ventas'] - x['costo'])
        .assign(margen=lambda x: (x['ganancia'] / x['ventas'] * 100).round(2))
        .query('ganancia > 0')
        .sort_values('margen', ascending=False)
        .groupby('producto')
        .agg({
            'ventas': 'sum',
            'ganancia': 'sum',
            'margen': 'mean'
        })
        .round(2)
        .sort_values('ganancia', ascending=False)
    )
    
    print(resultado)
    
    print("\n💡 Todo el análisis en una sola expresión encadenada")


def demostrar_ventajas_encadenamiento():
    """
    Resume las ventajas del encadenamiento.
    """
    print("\n" + "="*70)
    print("VENTAJAS DEL METHOD CHAINING")
    print("="*70)
    
    print("""
1. LEGIBILIDAD:
   - Código más expresivo y fácil de leer
   - Flujo de transformaciones claro
   
2. MENOS VARIABLES TEMPORALES:
   - No necesitas df_temp1, df_temp2, etc.
   - Menos uso de memoria
   
3. ESTILO FUNCIONAL:
   - Cada método retorna un nuevo objeto
   - Sin efectos secundarios
   
4. FACILITA DEBUGGING:
   - Puedes comentar líneas individuales
   - Fácil agregar/quitar pasos
   
5. COMPOSICIÓN:
   - Puedes construir pipelines complejos
   - Reutilizable y testeable
    """)


if __name__ == "__main__":
    print("="*70)
    print("MÓDULO 4: MÉTODOS Y ENCADENAMIENTO")
    print("="*70)
    
    demostrar_fluent_interface()
    demostrar_retorno_self()
    demostrar_copy_vs_referencia()
    demostrar_pipe()
    demostrar_assign()
    demostrar_query()
    ejemplo_completo_encadenamiento()
    demostrar_ventajas_encadenamiento()

