"""
Método de Newton Raphson
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class IteracionNewton:
    numero: int
    x: float
    fx: float
    dfx: float
    error: float


@dataclass
class ResultadoNewton:
    raiz: float
    iteraciones: int
    convergio: bool
    historial: List[IteracionNewton]


def newton_raphson(
    funcion: Callable[[float], float],
    derivada: Callable[[float], float],
    x0: float,
    tolerancia: float = 1e-6,
    max_iter: int = 100,
) -> ResultadoNewton:
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser positivo.")

    historial: List[IteracionNewton] = []
    x = x0

    for numero in range(1, max_iter + 1):
        fx = funcion(x)
        dfx = derivada(x)
        if dfx == 0:
            raise ZeroDivisionError("La derivada es cero; el metodo no puede continuar.")

        x_nuevo = x - fx / dfx
        error = abs(x_nuevo - x)

        historial.append(
            IteracionNewton(
                numero=numero,
                x=x_nuevo,
                fx=funcion(x_nuevo),
                dfx=derivada(x_nuevo),
                error=error,
            )
        )

        if error <= tolerancia or abs(funcion(x_nuevo)) <= tolerancia:
            return ResultadoNewton(
                raiz=x_nuevo,
                iteraciones=numero,
                convergio=True,
                historial=historial,
            )

        x = x_nuevo

    return ResultadoNewton(
        raiz=historial[-1].x,
        iteraciones=max_iter,
        convergio=False,
        historial=historial,
    )


def imprimir_tabla(historial: List[IteracionNewton]) -> None:
    encabezado = f"{'i':>3} {'x':>12} {'f(x)':>14} {'df(x)':>14} {'error':>12}"
    print(encabezado)
    print("-" * len(encabezado))
    for paso in historial:
        print(
            f"{paso.numero:>3} "
            f"{paso.x:>12.6f} "
            f"{paso.fx:>14.6e} "
            f"{paso.dfx:>14.6e} "
            f"{paso.error:>12.6e}"
        )


def funcion_ejemplo(x: float) -> float:
    return x**3 - x - 2


def derivada_ejemplo(x: float) -> float:
    return 3 * x**2 - 1


def main() -> None:
    resultado = newton_raphson(funcion_ejemplo, derivada_ejemplo, 1.5)
    print("Método de Newton-Raphson")
    imprimir_tabla(resultado.historial)
    print(f"\nRaiz aproximada: {resultado.raiz:.10f}")
    print(f"Iteraciones: {resultado.iteraciones}")
    print(f"Verificacion f(raiz): {funcion_ejemplo(resultado.raiz):.10e}")


if __name__ == "__main__":
    main()
