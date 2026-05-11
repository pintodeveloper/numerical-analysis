# Funcionamiento del programa - Método de Bisección

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Biseccion_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método de bisección para aproximar una raíz de una función continua en un intervalo cerrado `[a, b]`.

## Funcionamiento

El método parte de un intervalo donde la función cambia de signo. En cada iteración calcula el punto medio `c = (a + b) / 2`, evalúa `f(c)` y selecciona el subintervalo donde se conserva el cambio de signo. El proceso se repite hasta alcanzar la tolerancia definida o el número máximo de iteraciones.

## Estructura del código

- `IteracionBiseccion`: almacena los datos de cada iteración.
- `ResultadoBiseccion`: guarda la raíz aproximada, número de iteraciones, estado de convergencia e historial.
- `biseccion()`: ejecuta el algoritmo numérico.
- `imprimir_tabla()`: muestra el historial de iteraciones.
- `main()`: define un ejemplo con `f(x) = x^3 - x - 2` en el intervalo `[1, 2]`.

## Validaciones

El programa verifica que `a < b`, que la tolerancia sea positiva, que el máximo de iteraciones sea positivo y que exista cambio de signo en el intervalo.

## Ejecución

```bash
python Metodo_Biseccion_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La ejecución imprime una tabla de iteraciones y al final muestra si el método convergió, la raíz aproximada, el error estimado final y la verificación `f(raiz)`.

## Explicación de la salida

- La tabla muestra los valores del intervalo `a` y `b`, el punto medio `c`, el valor `f(c)` y el error estimado.
- Cuando `f(c)` cambia de signo con uno de los extremos, el programa conserva el subintervalo donde se encuentra la raíz.
- La raíz aproximada corresponde al último punto medio calculado cuando se cumple la tolerancia.
- La verificación `f(raiz)` debe quedar cercana a cero, lo cual confirma que la aproximación es coherente.
