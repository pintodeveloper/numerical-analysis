from dataclasses import dataclass
from typing import Callable, List, Optional


@dataclass
class IteracionBiseccion:
    numero: int
    a: float
    b: float
    c: float
    fa: float
    fb: float
    fc: float
    error: float


@dataclass
class ResultadoBiseccion:
    raiz: float
    iteraciones: int
    convergio: bool
    historial: List[IteracionBiseccion]


def biseccion(
    funcion: Callable[[float], float],
    a: float,
    b: float,
    tolerancia: float = 1e-6,
    max_iter: int = 100,
) -> ResultadoBiseccion:
    if a >= b:
        raise ValueError("El extremo izquierdo del intervalo debe ser menor que el derecho.")
    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser un numero positivo.")
    if max_iter <= 0:
        raise ValueError("El numero maximo de iteraciones debe ser positivo.")

    fa = funcion(a)
    fb = funcion(b)

    if fa == 0:
        return ResultadoBiseccion(raiz=a, iteraciones=0, convergio=True, historial=[])
    if fb == 0:
        return ResultadoBiseccion(raiz=b, iteraciones=0, convergio=True, historial=[])
    if fa * fb > 0:
        raise ValueError("La funcion debe cambiar de signo en el intervalo [a, b].")

    historial: List[IteracionBiseccion] = []

    for numero in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = funcion(c)
        error = abs(b - a) / 2

        historial.append(
            IteracionBiseccion(
                numero=numero,
                a=a,
                b=b,
                c=c,
                fa=fa,
                fb=fb,
                fc=fc,
                error=error,
            )
        )

        if fc == 0 or error <= tolerancia:
            return ResultadoBiseccion(
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

    return ResultadoBiseccion(
        raiz=historial[-1].c,
        iteraciones=max_iter,
        convergio=False,
        historial=historial,
    )


def imprimir_tabla(historial: List[IteracionBiseccion]) -> None:
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
