"""
Método de Euler
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

import math
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class PasoEuler:
    iteracion: int
    x: float
    y: float


def euler(
    funcion: Callable[[float, float], float],
    x0: float,
    y0: float,
    h: float,
    pasos: int,
) -> List[PasoEuler]:
    if h <= 0:
        raise ValueError("El paso h debe ser positivo.")
    if pasos <= 0:
        raise ValueError("El número de pasos debe ser positivo.")

    historial = [PasoEuler(iteracion=0, x=x0, y=y0)]
    x = x0
    y = y0

    for iteracion in range(1, pasos + 1):
        y = y + h * funcion(x, y)
        x = x + h
        historial.append(PasoEuler(iteracion=iteracion, x=x, y=y))

    return historial


def funcion_ejemplo(x: float, y: float) -> float:
    return x + y


def solucion_exacta(x: float) -> float:
    return 2 * math.exp(x) - x - 1


def main() -> None:
    historial = euler(funcion_ejemplo, 0.0, 1.0, 0.1, 5)
    print("Método de Euler")
    print(f"{'i':>3} {'x':>8} {'y':>12}")
    print("-" * 25)
    for paso in historial:
        print(f"{paso.iteracion:>3} {paso.x:>8.3f} {paso.y:>12.6f}")

    ultimo = historial[-1]
    exacto = solucion_exacta(ultimo.x)
    print(f"\nAproximacion final: {ultimo.y:.6f}")
    print(f"Valor exacto en x = {ultimo.x:.1f}: {exacto:.6f}")


if __name__ == "__main__":
    main()
