# Funcionamiento del programa - Método de Gauss-Seidel

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Gauss_Seidel_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método iterativo de Gauss-Seidel para resolver sistemas de ecuaciones lineales.

## Funcionamiento

El método inicia con una aproximación inicial del vector solución. En cada iteración actualiza cada componente usando los valores nuevos disponibles y los valores anteriores que aún no han sido actualizados. El proceso termina cuando el error máximo entre iteraciones cumple la tolerancia.

## Estructura del código

- `IteracionGaussSeidel`: guarda la aproximación y el error de cada iteración.
- `ResultadoGaussSeidel`: almacena la solución, iteraciones, convergencia e historial.
- `gauss_seidel()`: ejecuta el algoritmo iterativo.
- `imprimir_tabla()`: muestra el historial.
- `main()`: resuelve un sistema lineal de ejemplo.

## Validaciones

El programa valida que la matriz sea cuadrada, que el vector `b` tenga dimensión compatible, que la tolerancia y las iteraciones sean positivas, y que la diagonal no contenga ceros.

## Ejecución

```bash
python Metodo_Gauss_Seidel_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

El programa imprime las aproximaciones por iteración, el error y la solución aproximada final del sistema.

## Explicación de la salida

- Cada fila muestra la iteración, el vector aproximado `x` y el error máximo.
- El método usa los valores más recientes disponibles en cada actualización.
- El error mide el mayor cambio entre la aproximación anterior y la nueva.
- La solución final se acepta cuando el error cumple la tolerancia.
