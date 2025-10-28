"""
Proyecto de análisis de datos con Pandas
"""
import pandas as pd
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def main():
    """
    Función principal del proyecto
    """
    print("Proyecto Pandas iniciado correctamente")
    print(f"Versión de Pandas: {pd.__version__}")

if __name__ == "__main__":
    main()

