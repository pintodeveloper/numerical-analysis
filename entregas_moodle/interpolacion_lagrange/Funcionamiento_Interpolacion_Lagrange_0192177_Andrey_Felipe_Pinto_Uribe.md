# Funcionamiento del programa - Interpolación de Lagrange

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Interpolacion_Lagrange_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa la interpolación de Lagrange para aproximar un valor a partir de varios puntos conocidos.

## Funcionamiento

El método calcula el polinomio interpolante como suma de términos base de Lagrange. Cada término usa un nodo y se multiplica por factores que dependen de los demás nodos. La suma final entrega el valor interpolado.

## Estructura del código

- `interpolacion_lagrange()`: calcula el valor interpolado.
- `main()`: define los nodos de ejemplo y evalúa el polinomio en un punto.

## Validaciones

El programa verifica que las listas de nodos y valores tengan la misma longitud, que no estén vacías y que no existan valores `x` repetidos.

## Ejecución

```bash
python Metodo_Interpolacion_Lagrange_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra los nodos usados y el valor interpolado para el `x` seleccionado.

## Explicación de la salida

- La salida muestra los nodos y valores usados.
- El método construye términos base de Lagrange para cada nodo.
- La suma de los términos entrega el valor interpolado.
- El resultado corresponde a la evaluación del polinomio en el punto elegido.
