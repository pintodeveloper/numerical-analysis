# Metodo de Biseccion

**Estudiante:** Andrey Felipe Pinto Uribe  - 192177
**Curso:** Analisis Numerico  
**Fecha:** 25/04/2026

## 1. Objetivo

Implementar en Python el metodo de biseccion para aproximar la raiz de una funcion continua en un intervalo `[a, b]`, verificando que exista cambio de signo y mostrando el proceso iterativo hasta cumplir una tolerancia dada.

## 2. Fundamento teorico

El metodo de biseccion permite encontrar una raiz de una funcion continua cuando:

`f(a) * f(b) < 0`

Esto indica que la funcion cambia de signo en el intervalo, por lo tanto existe al menos una raiz dentro de `[a, b]`.

En cada iteracion se calcula el punto medio:

`c = (a + b) / 2`

Luego se evalua el signo de `f(c)` para decidir si la nueva raiz aproximada se encuentra en `[a, c]` o en `[c, b]`. El proceso se repite hasta que el error sea menor o igual a la tolerancia establecida.

## 3. Descripcion de la implementacion

Se desarrollaron los siguientes archivos:

- `biseccion.py`: contiene la funcion principal del metodo y la impresion de la tabla de iteraciones.
- `main.py`: ejecuta un ejemplo completo con una funcion de prueba.
- `test_biseccion.py`: incluye pruebas automatizadas para validar el funcionamiento.

La implementacion realiza estas validaciones:

- Verifica que `a < b`.
- Verifica que la tolerancia sea positiva.
- Verifica que el numero maximo de iteraciones sea positivo.
- Verifica que exista cambio de signo en el intervalo.
- Retorna inmediatamente si uno de los extremos ya es una raiz exacta.

## 4. Algoritmo aplicado

1. Definir la funcion `f(x)`, el intervalo inicial `[a, b]`, la tolerancia y el numero maximo de iteraciones.
2. Evaluar `f(a)` y `f(b)`.
3. Comprobar si existe cambio de signo en el intervalo.
4. Calcular el punto medio `c`.
5. Evaluar `f(c)`.
6. Elegir el nuevo subintervalo segun el signo de `f(c)`.
7. Repetir el proceso hasta cumplir la tolerancia o llegar al maximo de iteraciones.

## 5. Prueba principal realizada

Se uso la funcion:

`f(x) = x^3 - x - 2`

con:

- Intervalo inicial: `[1, 2]`
- Tolerancia: `1e-6`
- Maximo de iteraciones: `100`

### Resultado obtenido

- Raiz aproximada: `1.5213804245`
- Iteraciones realizadas: `20`
- Error estimado final: `9.5367431641e-07`
- Verificacion: `f(1.5213804245) = 4.2658294048e-06`

Este resultado confirma que el metodo converge correctamente hacia la raiz de la funcion y cumple el criterio de paro basado en el tamano del intervalo.

## 6. Evidencia de ejecucion

Comando ejecutado:

```bash
python main.py
```

Fragmento de salida:

```text
Metodo de Biseccion
Funcion: f(x) = x^3 - x - 2
Intervalo inicial: [1.0, 2.0]
Tolerancia: 1e-06
Maximo de iteraciones: 100

Resultado final
Convergio: True
Raiz aproximada: 1.5213804245
Iteraciones realizadas: 20
Error estimado final: 9.5367431641e-07
Verificacion f(raiz): 4.2658294048e-06
```

## 7. Pruebas de validacion

Tambien se ejecutaron pruebas automatizadas con:

```bash
python -m unittest test_biseccion.py
```

Casos validados:

- Aproximacion correcta de la raiz de `x^2 - 2`.
- Deteccion de raiz exacta en un extremo del intervalo.
- Error cuando no existe cambio de signo en el intervalo.

Resultado:

```text
Ran 3 tests in 0.000s

OK
```

## 8. Conclusion

La implementacion realizada en Python cumple con el funcionamiento esperado del metodo de biseccion. El programa aproxima la raiz de una funcion continua, valida los datos de entrada y muestra evidencia de convergencia mediante pruebas manuales y automatizadas.
