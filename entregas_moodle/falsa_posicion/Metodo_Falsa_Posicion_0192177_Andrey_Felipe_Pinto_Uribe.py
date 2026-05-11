"""
Método de la Falsa Posición
Estudiante: Andrey Felipe Pinto Uribe
Código: 0192177

Archivo preparado para entrega en Moodle. Contiene la implementación,
un ejemplo de ejecución y validaciones básicas de entrada.
"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class IteracionFalsaPosicion:
    numero: int
    a: float
    b: float
    c: float
    fc: float
    error: float


@dataclass
class ResultadoFalsaPosicion:
    raiz: float
    iteraciones: int
    convergio: bool
    historial: List[IteracionFalsaPosicion]


def falsa_posicion(
    funcion: Callable[[float], float],
    a: float,
    b: float,
    tolerancia: float = 1e-6,
    max_iter: int = 100,
) -> ResultadoFalsaPosicion:
    if a >= b:
        raise ValueError("El extremo izquierdo debe ser menor que el derecho.")
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser positivo.")

    fa = funcion(a)
    fb = funcion(b)

    if fa == 0:
        return ResultadoFalsaPosicion(raiz=a, iteraciones=0, convergio=True, historial=[])
    if fb == 0:
        return ResultadoFalsaPosicion(raiz=b, iteraciones=0, convergio=True, historial=[])
    if fa * fb > 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")

    historial: List[IteracionFalsaPosicion] = []
    c_anterior = None

    for numero in range(1, max_iter + 1):
        c = b - fb * (b - a) / (fb - fa)
        fc = funcion(c)
        error = abs(c - c_anterior) if c_anterior is not None else abs(b - a)

        historial.append(
            IteracionFalsaPosicion(
                numero=numero,
                a=a,
                b=b,
                c=c,
                fc=fc,
                error=error,
            )
        )

        if fc == 0 or error <= tolerancia:
            return ResultadoFalsaPosicion(
                raiz=c,
                iteraciones=numero,
                convergio=True,
                historial=historial,
            )

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c_anterior = c

    return ResultadoFalsaPosicion(
        raiz=historial[-1].c,
        iteraciones=max_iter,
        convergio=False,
        historial=historial,
    )


def imprimir_tabla(historial: List[IteracionFalsaPosicion]) -> None:
    encabezado = f"{'i':>3} {'a':>12} {'b':>12} {'c':>12} {'f(c)':>14} {'error':>12}"
    print(encabezado)
    print("-" * len(encabezado))
    for paso in historial:
        print(
            f"{paso.numero:>3} "
            f"{paso.a:>12.6f} "
            f"{paso.b:>12.6f} "
            f"{paso.c:>12.6f} "
            f"{paso.fc:>14.6e} "
            f"{paso.error:>12.6e}"
        )


def funcion_ejemplo(x: float) -> float:
    return x**3 - x - 2


def main() -> None:
    resultado = falsa_posicion(funcion_ejemplo, 1.0, 2.0)
    print("Método de la Falsa Posición")
    imprimir_tabla(resultado.historial)
    print(f"\nRaiz aproximada: {resultado.raiz:.10f}")
    print(f"Iteraciones: {resultado.iteraciones}")
    print(f"Verificacion f(raiz): {funcion_ejemplo(resultado.raiz):.10e}")


if __name__ == "__main__":
    main()
