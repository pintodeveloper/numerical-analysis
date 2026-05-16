"""
Regla Trapezoidal
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import Callable


def regla_trapezoidal(funcion: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0:
        raise ValueError("El número de subintervalos debe ser positivo.")
    if a == b:
        return 0.0

    h = (b - a) / n
    suma = funcion(a) + funcion(b)

    for i in range(1, n):
        suma += 2 * funcion(a + i * h)

    return h * suma / 2


def funcion_ejemplo(x: float) -> float:
    return x**2


def main() -> None:
    aproximacion = regla_trapezoidal(funcion_ejemplo, 0.0, 1.0, 4)
    print("Regla Trapezoidal")
    print(f"Integral aproximada de x^2 en [0, 1]: {aproximacion:.6f}")
    print(f"Valor exacto: {1 / 3:.6f}")


if __name__ == "__main__":
    main()
