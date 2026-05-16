# Funcionamiento del programa - Interpolación de Newton

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Interpolacion_Newton_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa la interpolación de Newton usando diferencias divididas.

## Funcionamiento

Primero se calculan los coeficientes del polinomio interpolante mediante diferencias divididas. Luego el polinomio se evalúa en el valor `x` solicitado usando una forma anidada, lo que permite obtener el valor interpolado.

## Estructura del código

- `diferencias_divididas()`: calcula los coeficientes del polinomio de Newton.
- `evaluar_newton()`: evalúa el polinomio interpolante.
- `main()`: define nodos, calcula coeficientes y obtiene el valor interpolado.

## Validaciones

El programa valida que las listas `x` e `y` tengan la misma longitud, que no estén vacías y que no haya valores `x` repetidos.

## Ejecución

```bash
python Metodo_Interpolacion_Newton_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra los nodos, los valores, los coeficientes calculados y el valor interpolado.

## Explicación de la salida

- La salida muestra los nodos `x` y los valores `y` usados.
- Los coeficientes corresponden a las diferencias divididas.
- El valor interpolado se obtiene evaluando el polinomio de Newton.
- El resultado final es la estimación en el punto `x` solicitado.
