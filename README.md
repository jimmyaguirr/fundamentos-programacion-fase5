# Control de horas trabajadas y clasificación de la jornada laboral

Solución en Python del **Problema 5** del *Anexo 4 – Banco de problemas* de la
**Fase 5 – Evaluación Final POA** del curso **Fundamentos de Programación
(213022)** de la Universidad Nacional Abierta y a Distancia – UNAD.

**Estudiante:** Jimmy David Aguirre Rivas
**Programa:** Ingeniería de Sistemas – ECBTI

---

## El problema

Una matriz registra las horas trabajadas por un equipo durante la semana con el
siguiente formato por fila:

```
[Nombre del recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
```

Se requiere calcular el total de horas semanales por persona y clasificar su
jornada laboral.

### Regla de negocio

| Condición | Clasificación |
|---|---|
| Total semanal **mayor a 40** horas | `Sobretiempo` |
| Total semanal **que no excede** 40 horas | `Horario estandar` |

> Un total de **exactamente 40 horas no es sobretiempo**: el enunciado dice
> *mayor a 40*, no *mayor o igual a 40*. El recurso `Carlos Andres Mejia`
> (40 horas exactas) está en los datos iniciales justamente para dejar ese
> caso frontera a la vista.

---

## Cómo ejecutarlo

Requiere **Python 3** y no usa ninguna librería externa.

```bash
python Problema_05_JimmyAguirre.py
```

El programa abre un menú con cuatro opciones:

1. Ver informe de horas y clasificación
2. Ver resumen del equipo
3. Registrar un recurso nuevo
4. Salir

### Salida de la opción 1

```
===================================================================================
INFORME DE HORAS TRABAJADAS Y CLASIFICACION DE JORNADA
Umbral de la empresa: mas de 40 horas semanales es sobretiempo
===================================================================================
RECURSO                   Lun    Mar    Mie    Jue    Vie   TOTAL     CLASIFICACION
-----------------------------------------------------------------------------------
Ana Maria Castro            9      9      8      9     10      45       Sobretiempo
Carlos Andres Mejia         8      8      8      8      8      40  Horario estandar
Diana Patricia Rojas      7.5      6      8    5.5      6      33  Horario estandar
Jorge Luis Benavides       10      9     10      9      8      46       Sobretiempo
===================================================================================
```

---

## Estructura del repositorio

| Archivo | Contenido |
|---|---|
| `Problema_05_JimmyAguirre.py` | Solución del problema. |
| `Casos_de_prueba_Problema_05.py` | Batería de 21 casos de prueba (21/21 exitosos). |
| `Informe_Fase5_JimmyAguirre.pdf` | Informe: requerimientos, diagrama de flujo, prueba de escritorio y enlaces. |
| `README.md` | Este archivo. |

### Ejecutar las pruebas

```bash
python Casos_de_prueba_Problema_05.py
```

Verifica la suma de horas, la regla de negocio (incluido el caso frontera de
las 40 horas exactas), la función que exige el enunciado y el formato de los
números.

---

## Diseño de la solución

El programa está dividido en nueve funciones, cada una con una sola
responsabilidad:

| Función | Responsabilidad |
|---|---|
| `calcular_total_horas(registro)` | Suma las horas de los cinco días con un ciclo `for` y un acumulador. |
| `clasificar_jornada(total_horas)` | Aplica la regla de negocio del umbral de 40 horas. |
| `analizar_recurso(registro)` | **Función que exige el enunciado:** devuelve `(nombre, total, clasificación)`. |
| `formatear_horas(valor)` | Presenta `40.0` como `40` y conserva `7.5`. |
| `mostrar_informe(matriz)` | Imprime la tabla con dos ciclos `for` anidados. |
| `mostrar_resumen(matriz)` | Horas totales, promedio y recursos en sobretiempo. |
| `leer_horas(mensaje)` | Valida los números que escribe el usuario (`while` + `try/except`). |
| `agregar_recurso(matriz)` | Registra un recurso nuevo en la matriz. |
| `mostrar_menu()` / `menu_principal()` | Controlan el flujo con `while` e `if/elif/else`. |

El umbral de 40 horas está en la constante `UMBRAL_SEMANAL`: si la empresa
cambia su política laboral, se modifica en un solo lugar.

---

## Nota sobre las tildes

Las cadenas que imprime el programa se escriben sin tildes a propósito, para
evitar errores de codificación al ejecutarlo en consolas de Windows. La
documentación sí las utiliza.
