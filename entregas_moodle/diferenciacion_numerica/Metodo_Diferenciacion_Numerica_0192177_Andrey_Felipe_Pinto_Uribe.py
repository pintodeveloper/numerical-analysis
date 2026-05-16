"""
Diferenciación Numérica
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import Callable


def diferencia_hacia_adelante(funcion: Callable[[float], float], x: float, h: float) -> float:
    if h <= 0:
        raise ValueError("El paso h debe ser positivo.")
    return (funcion(x + h) - funcion(x)) / h


def diferencia_hacia_atras(funcion: Callable[[float], float], x: float, h: float) -> float:
    if h <= 0:
        raise ValueError("El paso h debe ser positivo.")
    return (funcion(x) - funcion(x - h)) / h


def diferencia_central(funcion: Callable[[float], float], x: float, h: float) -> float:
    if h <= 0:
        raise ValueError("El paso h debe ser positivo.")
    return (funcion(x + h) - funcion(x - h)) / (2 * h)


def segunda_derivada_central(funcion: Callable[[float], float], x: float, h: float) -> float:
    if h <= 0:
        raise ValueError("El paso h debe ser positivo.")
    return (funcion(x + h) - 2 * funcion(x) + funcion(x - h)) / (h**2)


def funcion_ejemplo(x: float) -> float:
    return x**2


def main() -> None:
    x = 2.0
    h = 0.001

    adelante = diferencia_hacia_adelante(funcion_ejemplo, x, h)
    atras = diferencia_hacia_atras(funcion_ejemplo, x, h)
    central = diferencia_central(funcion_ejemplo, x, h)
    segunda = segunda_derivada_central(funcion_ejemplo, x, h)

    print("Diferenciación Numérica")
    print(f"f(x) = x^2, x = {x}, h = {h}")
    print(f"Diferencia hacia adelante: {adelante:.6f}")
    print(f"Diferencia hacia atras: {atras:.6f}")
    print(f"Diferencia central: {central:.6f}")
    print(f"Segunda derivada central: {segunda:.6f}")


if __name__ == "__main__":
    main()
