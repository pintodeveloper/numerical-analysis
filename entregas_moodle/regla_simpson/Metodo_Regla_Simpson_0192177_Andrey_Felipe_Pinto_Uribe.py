"""
Regla de Simpson
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import Callable


def regla_simpson(funcion: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser positivo y par.")
    if a == b:
        return 0.0

    h = (b - a) / n
    suma = funcion(a) + funcion(b)

    for i in range(1, n):
        factor = 4 if i % 2 != 0 else 2
        suma += factor * funcion(a + i * h)

    return h * suma / 3


def funcion_ejemplo(x: float) -> float:
    return x**2


def main() -> None:
    aproximacion = regla_simpson(funcion_ejemplo, 0.0, 1.0, 4)
    print("Regla de Simpson")
    print(f"Integral aproximada de x^2 en [0, 1]: {aproximacion:.6f}")
    print(f"Valor exacto: {1 / 3:.6f}")


if __name__ == "__main__":
    main()
