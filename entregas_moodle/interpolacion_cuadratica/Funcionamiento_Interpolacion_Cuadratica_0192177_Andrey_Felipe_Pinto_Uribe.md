# Funcionamiento del programa - Interpolación Cuadrática

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Interpolacion_Cuadratica_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa interpolación cuadrática para estimar valores usando tres puntos conocidos.

## Funcionamiento

El método construye un polinomio de grado dos mediante la forma de Lagrange para tres puntos. Para cada punto se calcula un término base y luego se suman los términos para obtener el valor interpolado en `x`.

## Estructura del código

- `interpolacion_cuadratica()`: recibe tres puntos y el valor `x` donde se desea interpolar.
- `main()`: define puntos de ejemplo y muestra el resultado calculado.

## Validaciones

El programa exige exactamente tres puntos y verifica que no existan valores `x` repetidos.

## Ejecución

```bash
python Metodo_Interpolacion_Cuadratica_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra los puntos usados y el valor interpolado para el punto indicado.

## Explicación de la salida

- La salida muestra los tres puntos utilizados.
- El valor interpolado se obtiene con un polinomio de grado dos.
- El método usa términos base de Lagrange para cada punto.
- El resultado es la evaluación del polinomio en el valor `x` indicado.
