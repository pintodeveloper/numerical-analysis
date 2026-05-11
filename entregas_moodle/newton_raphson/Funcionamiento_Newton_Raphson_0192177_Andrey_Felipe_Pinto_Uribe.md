# Funcionamiento del programa - Método de Newton Raphson

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Newton_Raphson_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método de Newton Raphson para aproximar una raíz a partir de un valor inicial y de la derivada de la función.

## Funcionamiento

En cada iteración se calcula una nueva aproximación con la fórmula `x_nuevo = x - f(x) / f'(x)`. Luego se mide el error como la diferencia absoluta entre la nueva aproximación y la anterior. El procedimiento termina cuando el error o `|f(x)|` cumple la tolerancia.

## Estructura del código

- `IteracionNewton`: registra `x`, `f(x)`, `f'(x)` y el error de cada paso.
- `ResultadoNewton`: almacena la raíz aproximada, iteraciones, convergencia e historial.
- `newton_raphson()`: ejecuta el método.
- `imprimir_tabla()`: imprime el proceso iterativo.
- `main()`: prueba el método con `f(x) = x^3 - x - 2` y su derivada.

## Validaciones

El programa valida que la tolerancia sea positiva, que el máximo de iteraciones sea positivo y evita la división por cero cuando la derivada es cero.

## Ejecución

```bash
python Metodo_Newton_Raphson_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra las iteraciones del método, la raíz aproximada, el número de iteraciones y la verificación de la función en la raíz.

## Explicación de la salida

- Cada fila muestra la nueva aproximación `x`, el valor `f(x)`, la derivada `f'(x)` y el error.
- La fórmula usada es `x_nuevo = x - f(x) / f'(x)`.
- El método se detiene cuando el error o el valor absoluto de `f(x)` cumple la tolerancia.
- Si la derivada fuera cero, el programa detendría el proceso para evitar una división por cero.
