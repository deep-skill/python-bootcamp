"""
Primalidad comprobantees.

Este archivo contiene dos funciones para determinar si un número es primo:
1. `es_primo()` - Implementación eficiente usando la raíz cuadrada.
2. `método_ineficiente()` - Implementación con bucle hasta n-1.

Métodos de primalidad:

1. **Es primal (eficiente):**
   - Verifica si el número es divisible por cualquier entero entre 2 y su raíz cuadrada.
   
2. **Método ineficiente:**
   - Verifica si el número es divisible por cualquier entero entre 2 y n-1.

Pruebas:
- Muestra el resultado de ambos métodos con ejemplos.
"""

def es_primo(n: int) -> bool:
    """
    Determine si un número es primo con un método eficiente.
    
    Args:
        n (int): El número a evaluar.
        
    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def método_ineficiente(n: int) -> bool:
    """
    Determine si un número es primo con un método ineficiente.
    
    Args:
        n (int): El número a evaluar.
        
    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Pruebas de los métodos
print("Primalidad de números (True = primo):")
print(f"7 es primo: {es_primo(7)}")   # Debería imprime True
print(f"9 es primo: {es_primo(9)}")   # Debería imprime False
print(f"15 es primo: {método_ineficiente(15)}")  # Debería imprime False

print("\nComparación de rendimiento:")
print("Primer método (eficiente) en comparación con el segundo (ineficiente):")
print("Es probable que el método eficiente sea más rápido para números grandes.")
