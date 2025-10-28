# Curso: Pandas desde la Perspectiva de POO

## 📋 Índice General del Curso

Este curso enseña Pandas desde una perspectiva de Programación Orientada a Objetos, permitiendo entender no solo cómo usar Pandas, sino cómo está construido y diseñado.

---

## 📚 Módulos

### **Módulo 0: Fundamentos de POO aplicados a Pandas**
**Archivos:** `Modulo_0_Fundamentos_POO.ipynb`, `modulo_0_fundamentos_poo.py`

**Contenido:**
- Pandas como biblioteca orientada a objetos
- Jerarquía de herencia (NDFrame)
- Clases, instancias, atributos y métodos
- Composición: DataFrame contiene Series
- Herramientas de exploración: `type()`, `isinstance()`, `dir()`

**Conceptos POO:**
- Clases e instancias
- Atributos y métodos
- Herencia
- Composición
- Encapsulamiento

---

### **Módulo 1: Series - El Objeto Fundamental**
**Archivos:** `Modulo_1_Series.ipynb`, `modulo_1_series.py`

**Contenido:**
- Anatomía completa de la clase Series
- Atributos: `values`, `index`, `dtype`, `name`, `shape`, `size`
- Constructores: crear Series de múltiples formas
- Propiedades mutables vs inmutables
- Métodos de acceso: `iloc`, `loc`, `at`, `iat`
- Métodos estadísticos y de transformación
- Encapsulamiento: atributos públicos vs privados

**Conceptos POO:**
- Constructores y sobrecarga
- Propiedades (properties)
- Métodos de instancia
- Inmutabilidad
- Encapsulamiento

---

### **Módulo 2: DataFrame - Colección de Series**
**Archivos:** `Modulo_2_DataFrame.ipynb`, `modulo_2_dataframe.py`

**Contenido:**
- DataFrame como composición de Series
- Cada columna es un objeto Series
- Constructores: crear DataFrames de múltiples formas
- Atributos: `values`, `index`, `columns`, `dtypes`, `shape`
- Métodos de acceso 2D: `loc`, `iloc`, `at`, `iat`
- Métodos de agregación: `sum()`, `mean()`, etc.
- Relación bidireccional Series ↔ DataFrame

**Conceptos POO:**
- Composición y agregación
- Relaciones entre objetos
- Interfaces de acceso

---

### **Módulo 3: Index - La Columna Vertebral**
**Archivos:** `Modulo_3_Index.ipynb`, `modulo_3_index.py`

**Contenido:**
- Index como clase inmutable
- Jerarquía de subclases: RangeIndex, DatetimeIndex, MultiIndex
- Inmutabilidad: no se puede modificar
- Operaciones de conjuntos: union, intersection, difference
- Index en Series y DataFrame
- Métodos útiles: `get_loc()`, `insert()`, `delete()`

**Conceptos POO:**
- Inmutabilidad
- Herencia y jerarquía de clases
- Polimorfismo (diferentes tipos de Index)
- Optimización (RangeIndex)

---

### **Módulo 3B: Sintaxis de Índices - Guía Práctica** ⭐ NUEVO
**Archivos:** `Modulo_3B_Sintaxis_Indices.ipynb`, `modulo_3b_sintaxis_indices.py`

**Contenido:**
- Sintaxis completa de acceso con índices en Series
- Acceso bidimensional en DataFrames
- Diferencias entre `[]`, `.loc[]`, `.iloc[]`, `.at[]`, `.iat[]`
- Filtrado booleano con índices
- Modificación de datos usando índices
- MultiIndex en profundidad
- Ejemplos prácticos y comparaciones directas
- Errores comunes y cómo evitarlos

**Características Especiales:**
- Guía de referencia rápida
- Tabla comparativa de métodos
- Buenas prácticas y consejos pro
- Ejemplos interactivos ejecutables

**Conceptos Prácticos:**
- Sintaxis de acceso
- Slicing (incluir vs excluir final)
- Operadores booleanos (&, |, ~)
- Optimización de acceso

---

### **Módulo 4: Métodos y Encadenamiento**
**Archivos:** `Modulo_4_Encadenamiento.ipynb`, `modulo_4_encadenamiento.py`

**Contenido:**
- Patrón Fluent Interface
- Method chaining (encadenamiento de métodos)
- Métodos que retornan copia vs self
- `inplace=True` vs copias
- `copy()` vs referencias
- Métodos especiales: `pipe()`, `assign()`, `query()`
- Pipeline completo de análisis

**Conceptos POO:**
- Fluent Interface
- Retorno de self
- Gestión de memoria
- Programación funcional

---

### **Módulo 5: Herencia y Polimorfismo en Pandas**
**Archivos:** `Modulo_5_Herencia.ipynb`, `modulo_5_herencia.py`

**Contenido:**
- Jerarquía: NDFrame → Series/DataFrame
- Métodos compartidos por herencia
- Polimorfismo: mismo método, comportamiento diferente
- Duck typing en Pandas
- IndexOpsMixin y otras clases base
- Crear subclases personalizadas
- Herencia múltiple en Pandas

**Conceptos POO:**
- Herencia
- Polimorfismo
- Duck typing
- Clases base abstractas
- Herencia múltiple
- Extensión de clases

---

### **Módulo 6: Atributos Especiales y Métodos Mágicos**
**Archivos:** `Modulo_6_Metodos_Magicos.ipynb`, `modulo_6_metodos_magicos.py`

**Contenido:**
- Métodos mágicos (dunder methods)
- `__getitem__`, `__setitem__`: operador `[]`
- `__len__`: función `len()`
- `__repr__`, `__str__`: representación
- `__iter__`: iteración con `for`
- Operadores aritméticos: `__add__`, `__sub__`, `__mul__`, etc.
- Operadores de comparación: `__eq__`, `__gt__`, `__lt__`, etc.
- `__contains__`: operador `in`

**Conceptos POO:**
- Métodos especiales
- Sobrecarga de operadores
- Protocolos de Python
- Interfaces implícitas

---

## 🎯 Objetivos de Aprendizaje General

Al completar este curso, serás capaz de:

1. **Entender Pandas desde adentro**: No solo usar, sino comprender cómo funciona
2. **Aplicar conceptos de POO**: Usar Pandas como caso de estudio de buen diseño
3. **Leer código fuente**: Capacidad para explorar el código de Pandas
4. **Crear extensiones**: Desarrollar tus propias subclases y extensiones
5. **Pensar como programador**: No solo como analista de datos

---

## 🛠️ Estructura de Archivos

Cada módulo incluye:
- **Notebook (`.ipynb`)**: Para ejecución interactiva y experimentación
- **Archivo Python (`.py`)**: Funciones organizadas que se ejecutan desde el notebook

Esta estructura permite:
- Ejecutar todo el módulo con `%run modulo_X.py`
- Usar funciones individuales según necesidad
- Mantener código organizado y reutilizable

---

## 📖 Cómo Usar Este Curso

### Opción 1: Secuencial
Estudia los módulos en orden (0 → 1 → 2 → 3 → 4 → 5 → 6)

### Opción 2: Por Tema
Si ya conoces Pandas:
- **POO Básico**: Módulos 0, 1
- **Estructuras**: Módulos 2, 3
- **Patrones avanzados**: Módulos 4, 5, 6

### Opción 3: Referencia
Usa los archivos `.py` como referencia rápida de conceptos

---

## 🔧 Requisitos

- Python 3.8+
- Pandas 2.0+
- NumPy
- Entorno virtual configurado en `.env/`

Ver `requirements.txt` para versiones específicas.

---

## 💡 Filosofía del Curso

Este curso es diferente porque:
- **No es solo tutorial**: Es educación en diseño de software
- **Profundidad sobre amplitud**: Mejor entender bien que saber superficialmente
- **POO práctica**: Conceptos abstractos con ejemplos concretos
- **Pensamiento crítico**: No solo "qué" sino "por qué" y "cómo"

---

## 📈 Próximos Pasos

Después de completar este curso:
1. Explora el código fuente de Pandas en GitHub
2. Crea tus propias extensiones de Pandas
3. Contribuye a proyectos open source
4. Aplica estos patrones en tu propio código

---

**¡Feliz aprendizaje! 🚀**

