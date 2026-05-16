"""
Interpolación Lineal
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import Tuple


def interpolacion_lineal(x0: float, y0: float, x1: float, y1: float, x: float) -> float:
    if x0 == x1:
        raise ValueError("Los valores x0 y x1 deben ser distintos.")
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def main() -> None:
    puntos: Tuple[float, float, float, float] = (1.0, 2.0, 3.0, 6.0)
    x = 2.0
    y = interpolacion_lineal(*puntos, x)

    print("Interpolación Lineal")
    print(f"Puntos: (1, 2) y (3, 6)")
    print(f"Valor interpolado en x = {x}: {y:.6f}")


if __name__ == "__main__":
    main()
