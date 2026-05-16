# Funcionamiento del programa - Regla Trapezoidal

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Regla_Trapezoidal_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa la regla trapezoidal compuesta para aproximar integrales definidas.

## Funcionamiento

El intervalo `[a, b]` se divide en `n` subintervalos. La función se evalúa en los extremos y en los puntos internos. Los valores internos se multiplican por dos y finalmente se aplica la fórmula del trapecio compuesto.

## Estructura del código

- `regla_trapezoidal()`: calcula la integral aproximada.
- `funcion_ejemplo()`: define `f(x) = x^2`.
- `main()`: aproxima la integral de `x^2` en `[0, 1]` con `n = 4`.

## Validaciones

El programa valida que el número de subintervalos sea positivo. Si `a` y `b` son iguales, retorna `0.0`.

## Ejecución

```bash
python Metodo_Regla_Trapezoidal_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra la integral aproximada y el valor exacto de referencia para comparar.

## Explicación de la salida

- La salida muestra la integral aproximada de `x^2` en `[0, 1]`.
- El intervalo se divide en subintervalos y se aplica la fórmula del trapecio.
- El valor exacto se imprime como referencia para medir la calidad de la aproximación.
- La diferencia entre la aproximación y el valor exacto representa el error numérico del método.
