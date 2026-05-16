# Funcionamiento del programa - Método de la Secante

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Secante_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método de la secante para aproximar una raíz sin requerir la derivada analítica de la función.

## Funcionamiento

El método inicia con dos aproximaciones `x0` y `x1`. En cada iteración calcula una nueva aproximación `x2` usando la recta secante entre esos dos puntos. Luego actualiza los valores anteriores y repite el proceso hasta cumplir la tolerancia.

## Estructura del código

- `IteracionSecante`: almacena `x0`, `x1`, `x2`, `f(x2)` y el error.
- `ResultadoSecante`: guarda la raíz, iteraciones, convergencia e historial.
- `secante()`: ejecuta el algoritmo.
- `imprimir_tabla()`: imprime la tabla de resultados.
- `main()`: ejecuta el ejemplo con `f(x) = x^3 - x - 2`.

## Validaciones

El programa verifica que la tolerancia sea positiva, que el máximo de iteraciones sea positivo y evita la división por cero cuando `f(x1) - f(x0)` es cero.

## Ejecución

```bash
python Metodo_Secante_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

El programa imprime la tabla de iteraciones, la raíz aproximada, el número de iteraciones y la verificación de `f(raiz)`.

## Explicación de la salida

- La tabla muestra las dos aproximaciones anteriores `x0` y `x1`, la nueva aproximación `x2`, `f(x2)` y el error.
- La nueva aproximación se obtiene con la recta secante entre los puntos evaluados.
- El método actualiza `x0` y `x1` hasta cumplir la tolerancia.
- La salida final confirma el resultado evaluando la función en la raíz aproximada.
