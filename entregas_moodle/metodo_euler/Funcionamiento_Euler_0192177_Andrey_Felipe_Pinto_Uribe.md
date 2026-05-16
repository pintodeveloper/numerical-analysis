# Funcionamiento del programa - Método de Euler

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Euler_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método de Euler para aproximar la solución de una ecuación diferencial ordinaria de primer orden.

## Funcionamiento

El método parte de una condición inicial `(x0, y0)` y avanza con paso `h`. En cada iteración calcula `y_nuevo = y + h * f(x, y)` y luego actualiza el valor de `x`. El historial permite ver la aproximación en cada paso.

## Estructura del código

- `PasoEuler`: almacena la iteración, el valor de `x` y el valor aproximado de `y`.
- `euler()`: ejecuta el método numérico.
- `funcion_ejemplo()`: define la ecuación diferencial `y' = x + y`.
- `solucion_exacta()`: calcula un valor de referencia para comparar.
- `main()`: ejecuta el ejemplo y muestra la tabla de pasos.

## Validaciones

El programa valida que el paso `h` y el número de pasos sean positivos.

## Ejecución

```bash
python Metodo_Euler_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra la tabla de aproximaciones, la aproximación final y el valor exacto de referencia.

## Explicación de la salida

- La tabla muestra cada paso con el valor de `x` y la aproximación `y`.
- El método avanza usando `y_nuevo = y + h * f(x, y)`.
- La aproximación final se compara con una solución exacta de referencia.
- La diferencia entre ambos valores permite observar el error del método.
