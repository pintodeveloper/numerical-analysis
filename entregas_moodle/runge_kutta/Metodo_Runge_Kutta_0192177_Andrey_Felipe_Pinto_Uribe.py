"""
Método de Runge-Kutta
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

import math
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class PasoRungeKutta:
    iteracion: int
    x: float
    y: float


def runge_kutta_4(
    funcion: Callable[[float, float], float],
    x0: float,
    y0: float,
    h: float,
    pasos: int,
) -> List[PasoRungeKutta]:
    if h <= 0:
        raise ValueError("El paso h debe ser positivo.")
    if pasos <= 0:
        raise ValueError("El número de pasos debe ser positivo.")

    historial = [PasoRungeKutta(iteracion=0, x=x0, y=y0)]
    x = x0
    y = y0

    for iteracion in range(1, pasos + 1):
        k1 = funcion(x, y)
        k2 = funcion(x + h / 2, y + h * k1 / 2)
        k3 = funcion(x + h / 2, y + h * k2 / 2)
        k4 = funcion(x + h, y + h * k3)

        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h
        historial.append(PasoRungeKutta(iteracion=iteracion, x=x, y=y))

    return historial


def funcion_ejemplo(x: float, y: float) -> float:
    return x + y


def solucion_exacta(x: float) -> float:
    return 2 * math.exp(x) - x - 1


def main() -> None:
    historial = runge_kutta_4(funcion_ejemplo, 0.0, 1.0, 0.1, 5)
    print("Método de Runge-Kutta de cuarto orden")
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
