"""
Factorización LU
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from dataclasses import dataclass
from typing import List, Tuple


Matriz = List[List[float]]
Vector = List[float]


@dataclass
class ResultadoLU:
    l: Matriz
    u: Matriz
    solucion: Vector


def factorizacion_lu(a: Matriz) -> Tuple[Matriz, Matriz]:
    n = len(a)
    if n == 0 or any(len(fila) != n for fila in a):
        raise ValueError("La matriz debe ser cuadrada y no vacia.")

    l = [[0.0] * n for _ in range(n)]
    u = [[0.0] * n for _ in range(n)]

    for i in range(n):
        l[i][i] = 1.0

    for j in range(n):
        for i in range(j + 1):
            suma = sum(l[i][k] * u[k][j] for k in range(i))
            u[i][j] = a[i][j] - suma

        if u[j][j] == 0:
            raise ZeroDivisionError("Se encontro un pivote cero durante la factorizacion LU.")

        for i in range(j + 1, n):
            suma = sum(l[i][k] * u[k][j] for k in range(j))
            l[i][j] = (a[i][j] - suma) / u[j][j]

    return l, u


def sustitucion_adelante(l: Matriz, b: Vector) -> Vector:
    n = len(l)
    y = [0.0] * n
    for i in range(n):
        suma = sum(l[i][j] * y[j] for j in range(i))
        y[i] = b[i] - suma
    return y


def sustitucion_atras(u: Matriz, y: Vector) -> Vector:
    n = len(u)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(u[i][j] * x[j] for j in range(i + 1, n))
        if u[i][i] == 0:
            raise ZeroDivisionError("Se encontro un pivote cero en la sustitucion hacia atrás.")
        x[i] = (y[i] - suma) / u[i][i]
    return x


def resolver_lu(a: Matriz, b: Vector) -> ResultadoLU:
    l, u = factorizacion_lu(a)
    y = sustitucion_adelante(l, b)
    x = sustitucion_atras(u, y)
    return ResultadoLU(l=l, u=u, solucion=x)


def imprimir_matriz(nombre: str, matriz: Matriz) -> None:
    print(nombre)
    for fila in matriz:
        print(" ".join(f"{valor:10.6f}" for valor in fila))


def main() -> None:
    a = [
        [4.0, -1.0, 0.0],
        [-1.0, 4.0, -1.0],
        [0.0, -1.0, 3.0],
    ]
    b = [15.0, 10.0, 10.0]

    resultado = resolver_lu(a, b)
    print("Factorización LU")
    imprimir_matriz("Matriz L:", resultado.l)
    print()
    imprimir_matriz("Matriz U:", resultado.u)
    print(f"\nSolucion aproximada: {[round(valor, 6) for valor in resultado.solucion]}")


if __name__ == "__main__":
    main()
