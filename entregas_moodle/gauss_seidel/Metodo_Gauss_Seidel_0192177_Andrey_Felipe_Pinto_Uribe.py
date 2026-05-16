"""
Método de Gauss-Seidel
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from dataclasses import dataclass
from typing import List


Matriz = List[List[float]]
Vector = List[float]


@dataclass
class IteracionGaussSeidel:
    numero: int
    aproximacion: Vector
    error: float


@dataclass
class ResultadoGaussSeidel:
    solucion: Vector
    iteraciones: int
    convergio: bool
    historial: List[IteracionGaussSeidel]


def gauss_seidel(
    a: Matriz,
    b: Vector,
    x0: Vector | None = None,
    tolerancia: float = 1e-6,
    max_iter: int = 100,
) -> ResultadoGaussSeidel:
    n = len(a)
    if n == 0 or any(len(fila) != n for fila in a):
        raise ValueError("La matriz debe ser cuadrada y no vacia.")
    if len(b) != n:
        raise ValueError("El vector b debe tener la misma dimension que la matriz.")
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser positivo.")

    x = [0.0] * n if x0 is None else x0[:]
    historial: List[IteracionGaussSeidel] = []

    for numero in range(1, max_iter + 1):
        x_anterior = x[:]

        for i in range(n):
            if a[i][i] == 0:
                raise ZeroDivisionError("La diagonal contiene un cero.")
            suma_1 = sum(a[i][j] * x[j] for j in range(i))
            suma_2 = sum(a[i][j] * x_anterior[j] for j in range(i + 1, n))
            x[i] = (b[i] - suma_1 - suma_2) / a[i][i]

        error = max(abs(x[i] - x_anterior[i]) for i in range(n))
        historial.append(IteracionGaussSeidel(numero=numero, aproximacion=x[:], error=error))

        if error <= tolerancia:
            return ResultadoGaussSeidel(
                solucion=x,
                iteraciones=numero,
                convergio=True,
                historial=historial,
            )

    return ResultadoGaussSeidel(
        solucion=x,
        iteraciones=max_iter,
        convergio=False,
        historial=historial,
    )


def imprimir_tabla(historial: List[IteracionGaussSeidel]) -> None:
    print(f"{'i':>3} {'x':>32} {'error':>12}")
    print("-" * 52)
    for paso in historial:
        vector = ", ".join(f"{valor:.6f}" for valor in paso.aproximacion)
        print(f"{paso.numero:>3} {vector:>32} {paso.error:>12.6e}")


def main() -> None:
    a = [
        [4.0, -1.0, 0.0],
        [-1.0, 4.0, -1.0],
        [0.0, -1.0, 3.0],
    ]
    b = [15.0, 10.0, 10.0]

    resultado = gauss_seidel(a, b)
    print("Método de Gauss-Seidel")
    imprimir_tabla(resultado.historial)
    print(f"\nSolucion aproximada: {[round(valor, 6) for valor in resultado.solucion]}")
    print(f"Iteraciones: {resultado.iteraciones}")


if __name__ == "__main__":
    main()
