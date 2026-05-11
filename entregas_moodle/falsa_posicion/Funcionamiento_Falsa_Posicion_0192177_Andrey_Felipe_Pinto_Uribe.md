# Funcionamiento del programa - Método de la Falsa Posición

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Falsa_Posicion_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método de la falsa posición para aproximar una raíz de una función continua usando un intervalo inicial con cambio de signo.

## Funcionamiento

El método calcula una aproximación `c` usando la recta secante que une los puntos `(a, f(a))` y `(b, f(b))`. Después evalúa `f(c)` y actualiza el intervalo según el cambio de signo. El proceso continúa hasta que el error entre aproximaciones sea menor o igual que la tolerancia.

## Estructura del código

- `IteracionFalsaPosicion`: almacena los datos de cada paso.
- `ResultadoFalsaPosicion`: guarda la raíz, iteraciones, convergencia e historial.
- `falsa_posicion()`: contiene el algoritmo principal.
- `imprimir_tabla()`: presenta los valores calculados por iteración.
- `main()`: ejecuta un ejemplo con `f(x) = x^3 - x - 2`.

## Validaciones

El programa verifica que el intervalo sea válido, que la tolerancia y el número de iteraciones sean positivos, y que la función cambie de signo en `[a, b]`.

## Ejecución

```bash
python Metodo_Falsa_Posicion_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra la tabla de iteraciones, la raíz aproximada, el número de iteraciones y la evaluación de la función en la raíz encontrada.

## Explicación de la salida

- La tabla muestra el intervalo actual, la aproximación `c` calculada por falsa posición, `f(c)` y el error.
- El método actualiza el extremo correspondiente según el signo de `f(c)`.
- El error se calcula como la diferencia entre aproximaciones consecutivas.
- La verificación `f(raiz)` permite comprobar que el resultado está cerca de una raíz real.
