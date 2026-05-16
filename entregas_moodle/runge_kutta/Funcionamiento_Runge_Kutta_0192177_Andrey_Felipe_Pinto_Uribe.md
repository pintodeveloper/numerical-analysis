# Funcionamiento del programa - Método de Runge-Kutta

**Estudiante:** Andrey Felipe Pinto Uribe  
**Código:** 0192177  
**Archivo fuente:** `Metodo_Runge_Kutta_0192177_Andrey_Felipe_Pinto_Uribe.py`

## Objetivo

El programa implementa el método de Runge-Kutta de cuarto orden para aproximar la solución de una ecuación diferencial ordinaria.

## Funcionamiento

En cada paso el método calcula cuatro pendientes `k1`, `k2`, `k3` y `k4`. Estas pendientes se combinan con pesos para obtener una aproximación más precisa que la del método de Euler. Después se actualizan `x` y `y` hasta completar el número de pasos.

## Estructura del código

- `PasoRungeKutta`: almacena la iteración y los valores aproximados.
- `runge_kutta_4()`: ejecuta el método RK4.
- `funcion_ejemplo()`: define la ecuación diferencial `y' = x + y`.
- `solucion_exacta()`: calcula un valor de referencia.
- `main()`: ejecuta el ejemplo y muestra los resultados.

## Validaciones

El programa valida que el paso `h` y el número de pasos sean positivos.

## Ejecución

```bash
python Metodo_Runge_Kutta_0192177_Andrey_Felipe_Pinto_Uribe.py
```

## Resultado esperado

La salida muestra la tabla de aproximaciones, la aproximación final y el valor exacto usado como referencia.

## Explicación de la salida

- La tabla muestra la aproximación en cada paso.
- En cada iteración se calculan las pendientes `k1`, `k2`, `k3` y `k4`.
- La combinación ponderada de pendientes mejora la precisión frente a Euler.
- La aproximación final se compara con la solución exacta de referencia.
