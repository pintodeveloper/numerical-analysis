"""
Método de la Secante
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class IteracionSecante:
    numero: int
    x0: float
    x1: float
    x2: float
    fx2: float
    error: float


@dataclass
class ResultadoSecante:
    raiz: float
    iteraciones: int
    convergio: bool
    historial: List[IteracionSecante]


def secante(
    funcion: Callable[[float], float],
    x0: float,
    x1: float,
    tolerancia: float = 1e-6,
    max_iter: int = 100,
) -> ResultadoSecante:
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser positivo.")

    historial: List[IteracionSecante] = []

    for numero in range(1, max_iter + 1):
        f0 = funcion(x0)
        f1 = funcion(x1)
        if f1 - f0 == 0:
            raise ZeroDivisionError("La diferencia de valores de la funcion es cero.")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        fx2 = funcion(x2)
        error = abs(x2 - x1)

        historial.append(
            IteracionSecante(
                numero=numero,
                x0=x0,
                x1=x1,
                x2=x2,
                fx2=fx2,
                error=error,
            )
        )

        if error <= tolerancia or abs(fx2) <= tolerancia:
            return ResultadoSecante(
                raiz=x2,
                iteraciones=numero,
                convergio=True,
                historial=historial,
            )

        x0, x1 = x1, x2

    return ResultadoSecante(
        raiz=historial[-1].x2,
        iteraciones=max_iter,
        convergio=False,
        historial=historial,
    )


def imprimir_tabla(historial: List[IteracionSecante]) -> None:
    encabezado = f"{'i':>3} {'x0':>12} {'x1':>12} {'x2':>12} {'f(x2)':>14} {'error':>12}"
    print(encabezado)
    print("-" * len(encabezado))
    for paso in historial:
        print(
            f"{paso.numero:>3} "
            f"{paso.x0:>12.6f} "
            f"{paso.x1:>12.6f} "
            f"{paso.x2:>12.6f} "
            f"{paso.fx2:>14.6e} "
            f"{paso.error:>12.6e}"
        )


def funcion_ejemplo(x: float) -> float:
    return x**3 - x - 2


def main() -> None:
    resultado = secante(funcion_ejemplo, 1.0, 2.0)
    print("Método de la Secante")
    imprimir_tabla(resultado.historial)
    print(f"\nRaiz aproximada: {resultado.raiz:.10f}")
    print(f"Iteraciones: {resultado.iteraciones}")
    print(f"Verificacion f(raiz): {funcion_ejemplo(resultado.raiz):.10e}")


if __name__ == "__main__":
    main()
