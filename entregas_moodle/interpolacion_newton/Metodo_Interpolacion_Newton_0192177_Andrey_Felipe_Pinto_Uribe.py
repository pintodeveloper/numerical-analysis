"""
Interpolación de Newton
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from typing import List


def diferencias_divididas(x: List[float], y: List[float]) -> List[float]:
    if len(x) != len(y) or len(x) == 0:
        raise ValueError("Las listas x e y deben tener la misma longitud y no ser vacias.")

    n = len(x)
    coeficientes = y[:]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            denominador = x[i] - x[i - j]
            if denominador == 0:
                raise ValueError("Los valores de x no deben repetirse.")
            coeficientes[i] = (coeficientes[i] - coeficientes[i - 1]) / denominador

    return coeficientes


def evaluar_newton(x_nodos: List[float], coeficientes: List[float], x: float) -> float:
    resultado = coeficientes[-1]
    for i in range(len(coeficientes) - 2, -1, -1):
        resultado = resultado * (x - x_nodos[i]) + coeficientes[i]
    return resultado


def main() -> None:
    x_nodos = [0.0, 1.0, 2.0]
    y_nodos = [1.0, 2.0, 5.0]
    x = 1.5

    coeficientes = diferencias_divididas(x_nodos, y_nodos)
    y = evaluar_newton(x_nodos, coeficientes, x)

    print("Interpolación de Newton")
    print(f"Nodos x: {x_nodos}")
    print(f"Valores y: {y_nodos}")
    print(f"Coeficientes: {[round(valor, 6) for valor in coeficientes]}")
    print(f"Valor interpolado en x = {x}: {y:.6f}")


if __name__ == "__main__":
    main()
