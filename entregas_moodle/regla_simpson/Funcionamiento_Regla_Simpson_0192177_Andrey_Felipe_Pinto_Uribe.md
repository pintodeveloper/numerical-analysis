# Funcionamiento del programa - Regla de Simpson

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Regla_Simpson_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa la regla de Simpson compuesta para aproximar integrales definidas.

## Funcionamiento

El intervalo `[a, b]` se divide en un número par de subintervalos. La fórmula suma los valores de los extremos, multiplica por cuatro los puntos internos impares y por dos los puntos internos pares. Finalmente multiplica la suma por `h / 3`.

## Estructura del código

- `regla_simpson()`: calcula la integral aproximada.
- `funcion_ejemplo()`: define `f(x) = x^2`.
- `main()`: aproxima la integral de `x^2` en `[0, 1]` con `n = 4`.

## Validaciones

El programa valida que `n` sea positivo y par. Si los límites de integración son iguales, retorna `0.0`.

## Ejecución

```bash
python Metodo_Regla_Simpson_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra la aproximación de la integral y el valor exacto de referencia.

## Explicación de la salida

- La salida muestra la aproximación de la integral de `x^2` en `[0, 1]`.
- La regla de Simpson usa pesos `4` y `2` sobre los puntos internos.
- El número de subintervalos debe ser par.
- El valor exacto se muestra para comparar la aproximación obtenida.
