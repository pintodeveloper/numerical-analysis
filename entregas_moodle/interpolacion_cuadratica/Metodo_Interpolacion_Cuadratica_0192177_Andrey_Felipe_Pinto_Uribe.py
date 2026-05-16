"""
Interpolación Cuadrática
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import List, Tuple


Punto = Tuple[float, float]


def interpolacion_cuadratica(puntos: List[Punto], x: float) -> float:
    if len(puntos) != 3:
        raise ValueError("La interpolacion cuadratica requiere exactamente tres puntos.")

    resultado = 0.0
    for i in range(3):
        xi, yi = puntos[i]
        termino = yi
        for j in range(3):
            if i == j:
                continue
            xj, _ = puntos[j]
            if xi == xj:
                raise ValueError("Los puntos no deben tener valores x repetidos.")
            termino *= (x - xj) / (xi - xj)
        resultado += termino
    return resultado


def main() -> None:
    puntos = [(0.0, 1.0), (1.0, 2.0), (2.0, 5.0)]
    x = 1.5
    y = interpolacion_cuadratica(puntos, x)

    print("Interpolación Cuadrática")
    print(f"Puntos: {puntos}")
    print(f"Valor interpolado en x = {x}: {y:.6f}")


if __name__ == "__main__":
    main()
