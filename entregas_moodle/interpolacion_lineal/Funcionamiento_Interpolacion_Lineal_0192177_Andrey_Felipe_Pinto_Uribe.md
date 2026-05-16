# Funcionamiento del programa - Interpolación Lineal

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Interpolacion_Lineal_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa la interpolación lineal para estimar el valor de una función entre dos puntos conocidos.

## Funcionamiento

El método usa dos puntos `(x0, y0)` y `(x1, y1)`. A partir de ellos calcula el valor interpolado en un punto `x` mediante la ecuación de la recta que pasa por ambos puntos.

## Estructura del código

- `interpolacion_lineal()`: calcula el valor interpolado.
- `main()`: define dos puntos, selecciona un valor de `x` y muestra el resultado.

## Validaciones

El programa verifica que `x0` y `x1` sean distintos para evitar la división por cero.

## Ejecución

```bash
python Metodo_Interpolacion_Lineal_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra los puntos usados y el valor interpolado para el `x` seleccionado.

## Explicación de la salida

- La salida muestra los dos puntos usados para construir la recta.
- El programa calcula el valor interpolado en el `x` solicitado.
- La fórmula usa la pendiente entre los dos puntos.
- El resultado corresponde al valor de la recta en el punto indicado.
