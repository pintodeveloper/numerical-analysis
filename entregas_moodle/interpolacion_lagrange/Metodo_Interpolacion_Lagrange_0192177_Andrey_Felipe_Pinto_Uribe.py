"""
Interpolación de Lagrange
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import List


def interpolacion_lagrange(x_nodos: List[float], y_nodos: List[float], x: float) -> float:
    if len(x_nodos) != len(y_nodos) or len(x_nodos) == 0:
        raise ValueError("Las listas x e y deben tener la misma longitud y no ser vacias.")

    n = len(x_nodos)
    resultado = 0.0

    for i in range(n):
        termino = y_nodos[i]
        for j in range(n):
            if i == j:
                continue
            denominador = x_nodos[i] - x_nodos[j]
            if denominador == 0:
                raise ValueError("Los valores de x no deben repetirse.")
            termino *= (x - x_nodos[j]) / denominador
        resultado += termino

    return resultado


def main() -> None:
    x_nodos = [0.0, 1.0, 2.0]
    y_nodos = [1.0, 2.0, 5.0]
    x = 1.5
    y = interpolacion_lagrange(x_nodos, y_nodos, x)

    print("Interpolación de Lagrange")
    print(f"Nodos x: {x_nodos}")
    print(f"Valores y: {y_nodos}")
    print(f"Valor interpolado en x = {x}: {y:.6f}")


if __name__ == "__main__":
    main()
