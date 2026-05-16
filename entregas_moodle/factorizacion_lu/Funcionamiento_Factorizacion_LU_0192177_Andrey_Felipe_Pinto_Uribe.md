# Funcionamiento del programa - Factorización LU

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Factorizacion_LU_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa la factorización LU para resolver un sistema de ecuaciones lineales de la forma `Ax = b`.

## Funcionamiento

La matriz `A` se descompone en dos matrices: `L`, triangular inferior con unos en la diagonal, y `U`, triangular superior. Luego se resuelve primero `Ly = b` mediante sustitución hacia adelante y después `Ux = y` mediante sustitución hacia atrás.

## Estructura del código

- `ResultadoLU`: almacena las matrices `L`, `U` y el vector solución.
- `factorizacion_lu()`: obtiene las matrices `L` y `U`.
- `sustitucion_adelante()`: resuelve el sistema triangular inferior.
- `sustitucion_atras()`: resuelve el sistema triangular superior.
- `resolver_lu()`: coordina la factorización y las sustituciones.
- `main()`: resuelve un sistema de ejemplo de dimensión 3.

## Validaciones

El programa verifica que la matriz sea cuadrada y no vacía. También controla pivotes cero para evitar divisiones inválidas.

## Ejecución

```bash
python Metodo_Factorizacion_LU_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra las matrices `L` y `U`, y finalmente el vector solución aproximado del sistema.

## Explicación de la salida

- La salida muestra la matriz `L` triangular inferior y la matriz `U` triangular superior.
- Después de factorizar, se resuelve `Ly = b` por sustitución hacia adelante.
- Luego se resuelve `Ux = y` por sustitución hacia atrás.
- El vector final corresponde a la solución aproximada del sistema lineal.
