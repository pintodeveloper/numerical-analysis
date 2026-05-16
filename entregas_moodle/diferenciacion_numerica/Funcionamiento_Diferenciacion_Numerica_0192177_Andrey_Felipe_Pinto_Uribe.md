# Funcionamiento del programa - Diferenciación Numérica

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Diferenciacion_Numerica_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa fórmulas de diferenciación numérica para aproximar derivadas de una función.

## Funcionamiento

El código calcula derivadas aproximadas usando diferencia hacia adelante, diferencia hacia atrás, diferencia central y segunda derivada central. En el ejemplo se usa `f(x) = x^2`, el punto `x = 2.0` y un paso `h = 0.001`.

## Estructura del código

- `diferencia_hacia_adelante()`: aproxima la primera derivada usando `f(x + h)`.
- `diferencia_hacia_atras()`: aproxima la primera derivada usando `f(x - h)`.
- `diferencia_central()`: aproxima la primera derivada usando ambos lados del punto.
- `segunda_derivada_central()`: aproxima la segunda derivada.
- `main()`: ejecuta el ejemplo y muestra los resultados.

## Validaciones

Cada función verifica que el paso `h` sea positivo.

## Ejecución

```bash
python Metodo_Diferenciacion_Numerica_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra las aproximaciones obtenidas para cada fórmula de diferenciación numérica.

## Explicación de la salida

- La salida muestra aproximaciones con diferencia hacia adelante, hacia atrás y central.
- También se calcula una aproximación de la segunda derivada central.
- El paso `h` controla la distancia usada para estimar las pendientes.
- Para `f(x) = x^2` en `x = 2`, la derivada exacta es `4` y la segunda derivada exacta es `2`.
