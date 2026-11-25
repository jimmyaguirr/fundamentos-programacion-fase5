# -*- coding: utf-8 -*-
"""
===============================================================================
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programacion (213022)
Fase 5 - Evaluacion Final POA

BATERIA DE CASOS DE PRUEBA - Problema 5
Estudiante: Jimmy David Aguirre Rivas
===============================================================================

Este archivo NO es la solucion: es la evidencia de que la solucion funciona.
Importa las funciones de Problema_05_JimmyAguirre.py y comprueba, caso por
caso, que el resultado obtenido es igual al resultado esperado.

Para ejecutarlo, los dos archivos deben estar en la misma carpeta:

    python Casos_de_prueba_Problema_05.py
===============================================================================
"""

from Problema_05_JimmyAguirre import (
    UMBRAL_SEMANAL,
    analizar_recurso,
    calcular_total_horas,
    clasificar_jornada,
    formatear_horas,
)

# Contadores globales de la corrida.
pruebas_totales = 0
pruebas_exitosas = 0


def verificar(descripcion, obtenido, esperado):
    """Compara un valor obtenido con el esperado e imprime el resultado."""
    global pruebas_totales, pruebas_exitosas

    pruebas_totales = pruebas_totales + 1

    if obtenido == esperado:
        pruebas_exitosas = pruebas_exitosas + 1
        estado = "OK   "
    else:
        estado = "FALLA"

    print("[" + estado + "]", descripcion)
    if obtenido != esperado:
        print("          esperado:", esperado, "| obtenido:", obtenido)


# =============================================================================
# GRUPO 1: calcular_total_horas() - la suma de los cinco dias
# =============================================================================
print("\n=== GRUPO 1: calcular_total_horas() ===")

verificar("Jornada normal 8+8+8+8+8 suma 40",
          calcular_total_horas(["Prueba", 8, 8, 8, 8, 8]), 40.0)

verificar("Jornada con sobretiempo 9+9+8+9+10 suma 45",
          calcular_total_horas(["Prueba", 9, 9, 8, 9, 10]), 45.0)

verificar("Suma con medias horas 7.5+6+8+5.5+6 da 33",
          calcular_total_horas(["Prueba", 7.5, 6, 8, 5.5, 6]), 33.0)

verificar("Semana sin trabajar suma 0",
          calcular_total_horas(["Prueba", 0, 0, 0, 0, 0]), 0.0)

verificar("Un solo dia trabajado suma ese dia",
          calcular_total_horas(["Prueba", 0, 0, 6, 0, 0]), 6.0)

verificar("No toma el nombre como numero (no falla con texto en la pos. 0)",
          calcular_total_horas(["Nombre Largo De Prueba", 1, 1, 1, 1, 1]), 5.0)


# =============================================================================
# GRUPO 2: clasificar_jornada() - la regla de negocio y su frontera
# =============================================================================
print("\n=== GRUPO 2: clasificar_jornada() ===")

verificar("45 horas es Sobretiempo",
          clasificar_jornada(45), "Sobretiempo")

verificar("40.1 horas ya es Sobretiempo",
          clasificar_jornada(40.1), "Sobretiempo")

verificar("FRONTERA: exactamente 40 horas es Horario estandar",
          clasificar_jornada(40), "Horario estandar")

verificar("39.9 horas es Horario estandar",
          clasificar_jornada(39.9), "Horario estandar")

verificar("0 horas es Horario estandar",
          clasificar_jornada(0), "Horario estandar")

verificar("El umbral configurado del programa es 40",
          UMBRAL_SEMANAL, 40)


# =============================================================================
# GRUPO 3: analizar_recurso() - la funcion que exige el enunciado
# =============================================================================
print("\n=== GRUPO 3: analizar_recurso() ===")

verificar("Ana Maria Castro: 45 horas y Sobretiempo",
          analizar_recurso(["Ana Maria Castro", 9, 9, 8, 9, 10]),
          ("Ana Maria Castro", 45.0, "Sobretiempo"))

verificar("Carlos Andres Mejia: 40 horas y Horario estandar",
          analizar_recurso(["Carlos Andres Mejia", 8, 8, 8, 8, 8]),
          ("Carlos Andres Mejia", 40.0, "Horario estandar"))

verificar("Diana Patricia Rojas: 33 horas y Horario estandar",
          analizar_recurso(["Diana Patricia Rojas", 7.5, 6, 8, 5.5, 6]),
          ("Diana Patricia Rojas", 33.0, "Horario estandar"))

verificar("Jorge Luis Benavides: 46 horas y Sobretiempo",
          analizar_recurso(["Jorge Luis Benavides", 10, 9, 10, 9, 8]),
          ("Jorge Luis Benavides", 46.0, "Sobretiempo"))

verificar("Devuelve el nombre sin modificarlo",
          analizar_recurso(["Laura Gomez Rios", 8, 8, 8, 8, 8])[0],
          "Laura Gomez Rios")


# =============================================================================
# GRUPO 4: formatear_horas() - presentacion de los numeros
# =============================================================================
print("\n=== GRUPO 4: formatear_horas() ===")

verificar("40.0 se muestra como 40", formatear_horas(40.0), "40")
verificar("7.5 se muestra como 7.5", formatear_horas(7.5), "7.5")
verificar("0 se muestra como 0", formatear_horas(0), "0")
verificar("41.25 se redondea a 41.2", formatear_horas(41.25), "41.2")


# =============================================================================
# RESULTADO FINAL
# =============================================================================
print("\n" + "=" * 70)
print("RESULTADO: ", pruebas_exitosas, "de", pruebas_totales, "pruebas exitosas")
if pruebas_exitosas == pruebas_totales:
    print("Todas las pruebas pasaron. La logica de negocio se comporta")
    print("como lo pide el enunciado del Problema 5, incluida la frontera")
    print("de las 40 horas exactas.")
else:
    print("Hay pruebas que fallan: revisar las funciones senaladas arriba.")
print("=" * 70)
