from biseccion import biseccion, imprimir_tabla


def funcion_ejemplo(x: float) -> float:
    return x**3 - x - 2


def main() -> None:
    a = 1.0
    b = 2.0
    tolerancia = 1e-6
    max_iter = 100

    resultado = biseccion(funcion_ejemplo, a, b, tolerancia, max_iter)
    error_final = resultado.historial[-1].error if resultado.historial else 0.0

    print("Metodo de Biseccion")
    print(f"Funcion: f(x) = x^3 - x - 2")
    print(f"Intervalo inicial: [{a}, {b}]")
    print(f"Tolerancia: {tolerancia}")
    print(f"Maximo de iteraciones: {max_iter}\n")

    imprimir_tabla(resultado.historial)

    print("\nResultado final")
    print(f"Convergio: {resultado.convergio}")
    print(f"Raiz aproximada: {resultado.raiz:.10f}")
    print(f"Iteraciones realizadas: {resultado.iteraciones}")
    print(f"Error estimado final: {error_final:.10e}")
    print(f"Verificacion f(raiz): {funcion_ejemplo(resultado.raiz):.10e}")


if __name__ == "__main__":
    main()
