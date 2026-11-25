# -*- coding: utf-8 -*-
"""
===============================================================================
Universidad Nacional Abierta y a Distancia - UNAD
Escuela de Ciencias Basicas, Tecnologia e Ingenieria - ECBTI
Programa: Ingenieria de Sistemas
Curso: Fundamentos de Programacion (213022)
Fase 5 - Evaluacion Final POA

PROBLEMA 5: Control de horas trabajadas y clasificacion de jornada laboral
Estudiante: Jimmy David Aguirre Rivas
Grupo: 213022
Fecha: 25 de noviembre de 2026
===============================================================================

DESCRIPCION DEL PROBLEMA
------------------------
Una matriz registra las horas trabajadas por un equipo durante la semana con
el siguiente formato por fila:

    [Nombre del recurso, Lunes, Martes, Miercoles, Jueves, Viernes]

Se requiere calcular el total de horas semanales por persona y clasificar su
jornada laboral.

REQUISITOS DEL ENUNCIADO Y DONDE SE RESUELVEN
---------------------------------------------
1. Matriz con 4 recursos y las horas de cada dia (valores numericos).
      -> constante MATRIZ_HORAS (datos iniciales del programa).
2. Una funcion que calcule la suma total de horas semanales por recurso
   y clasifique la jornada laboral.
      -> analizar_recurso(), que se apoya en calcular_total_horas() y en
         clasificar_jornada().
3. Logica de negocio:
      - total de horas semanales MAYOR a 40   -> "Sobretiempo"
      - total que NO excede el umbral (<= 40) -> "Horario estandar"
      -> clasificar_jornada(). El umbral esta en la constante UMBRAL_SEMANAL,
         de modo que si la empresa cambia la politica se modifica en un solo
         lugar y no en todo el programa.
4. Salida: nombre de cada recurso, total de horas semanales trabajadas y la
   clasificacion de su jornada.
      -> mostrar_informe().

ESTRUCTURAS UTILIZADAS
----------------------
- Secuenciales : asignaciones, acumuladores y llamados ordenados a funciones.
- De control   : if / elif / else en clasificar_jornada(), en la validacion de
                 datos y en el menu principal.
- De repeticion: for anidado para recorrer la matriz (recursos) y, dentro de
                 cada recurso, los cinco dias de la semana; while para el menu
                 y para la validacion de los datos que escribe el usuario.
- Funciones    : nueve funciones con una sola responsabilidad cada una, de modo
                 que el programa principal solo coordina los llamados.

NOTA SOBRE EL CASO FRONTERA
---------------------------
El enunciado dice "si el total es MAYOR a 40" para Sobretiempo y "si no excede
el umbral" para Horario estandar. Por lo tanto un total de exactamente 40
horas NO es sobretiempo: se clasifica como "Horario estandar". El recurso
Carlos Andres Mejia (40 horas) se incluye en los datos iniciales justamente
para dejar ese caso frontera a la vista.
===============================================================================
"""

# ============================= CONSTANTES ====================================

# Nombres de los dias, en el mismo orden en que aparecen en la matriz.
DIAS = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

# Politica de la empresa: mas de 40 horas a la semana es sobretiempo.
UMBRAL_SEMANAL = 40

# Rango valido de horas que se pueden registrar en un dia.
HORAS_MIN_DIA = 0
HORAS_MAX_DIA = 24

# Etiquetas de la clasificacion.
JORNADA_SOBRETIEMPO = "Sobretiempo"
JORNADA_ESTANDAR = "Horario estandar"

# Posicion del nombre dentro de cada fila de la matriz.
COL_NOMBRE = 0

# Ancho de la tabla del informe, para que las lineas separadoras coincidan.
ANCHO_TABLA = 83

# Datos iniciales: 4 recursos con las horas trabajadas de lunes a viernes.
# Formato: [Nombre, Lunes, Martes, Miercoles, Jueves, Viernes]
MATRIZ_HORAS = [
    ["Ana Maria Castro",      9.0,  9.0,  8.0,  9.0, 10.0],
    ["Carlos Andres Mejia",   8.0,  8.0,  8.0,  8.0,  8.0],
    ["Diana Patricia Rojas",  7.5,  6.0,  8.0,  5.5,  6.0],
    ["Jorge Luis Benavides", 10.0,  9.0, 10.0,  9.0,  8.0],
]


# ============================ FUNCIONES DE CALCULO ===========================

def calcular_total_horas(registro):
    """Suma las horas de los cinco dias de un recurso y devuelve el total.

    Recibe una fila completa de la matriz ([nombre, lun, mar, mie, jue, vie]).
    El recorrido se hace con un ciclo for y un acumulador, empezando en la
    posicion 1 porque la posicion 0 guarda el nombre y no es un valor numerico.
    """
    total = 0.0
    for indice in range(1, len(registro)):
        total = total + registro[indice]
    return total


def clasificar_jornada(total_horas):
    """Clasifica la jornada laboral a partir del total de horas semanales.

    Regla de negocio:
        total > UMBRAL_SEMANAL  -> "Sobretiempo"
        en cualquier otro caso  -> "Horario estandar"
    """
    if total_horas > UMBRAL_SEMANAL:
        clasificacion = JORNADA_SOBRETIEMPO
    else:
        clasificacion = JORNADA_ESTANDAR
    return clasificacion


def analizar_recurso(registro):
    """Funcion principal que pide el enunciado.

    Para un recurso devuelve una tupla con los tres datos de la salida:
        (nombre, total de horas semanales, clasificacion de la jornada)

    Calcula la suma llamando a calcular_total_horas() y clasifica llamando a
    clasificar_jornada(). Al separar las dos tareas en funciones pequenas, cada
    una se puede probar y modificar por separado.
    """
    nombre = registro[COL_NOMBRE]
    total_horas = calcular_total_horas(registro)
    clasificacion = clasificar_jornada(total_horas)
    return nombre, total_horas, clasificacion


def formatear_horas(valor):
    """Devuelve las horas como texto corto: 40.0 -> 40 y 7.5 -> 7.5."""
    numero = float(valor)
    if numero == int(numero):
        return str(int(numero))
    return str(round(numero, 1))


# ============================ FUNCIONES DE SALIDA ============================

def mostrar_informe(matriz):
    """Imprime el informe solicitado: nombre, total de horas y clasificacion.

    Usa dos ciclos for anidados: el externo recorre los recursos de la matriz
    y el interno recorre los cinco dias para mostrar el detalle diario.
    """
    if len(matriz) == 0:
        print("\nNo hay recursos registrados todavia.")
        return

    print("\n" + "=" * ANCHO_TABLA)
    print("INFORME DE HORAS TRABAJADAS Y CLASIFICACION DE JORNADA")
    print("Umbral de la empresa: mas de", UMBRAL_SEMANAL,
          "horas semanales es sobretiempo")
    print("=" * ANCHO_TABLA)

    # Encabezado de la tabla.
    encabezado = "{:<22}".format("RECURSO")
    for dia in DIAS:
        encabezado = encabezado + "{:>7}".format(dia[:3])
    encabezado = encabezado + "{:>8}{:>18}".format("TOTAL", "CLASIFICACION")
    print(encabezado)
    print("-" * ANCHO_TABLA)

    # Ciclo externo: un recurso por vuelta.
    for registro in matriz:
        nombre, total_horas, clasificacion = analizar_recurso(registro)

        linea = "{:<22}".format(nombre[:21])

        # Ciclo interno: los cinco dias de ese recurso.
        for indice in range(1, len(registro)):
            linea = linea + "{:>7}".format(formatear_horas(registro[indice]))

        linea = linea + "{:>8}{:>18}".format(formatear_horas(total_horas),
                                             clasificacion)
        print(linea)

    print("=" * ANCHO_TABLA)


def mostrar_resumen(matriz):
    """Resumen del equipo: horas totales, promedio y recurso con mas horas.

    No lo exige el enunciado, pero aprovecha las mismas funciones de calculo
    para entregar informacion util al coordinador del equipo.
    """
    if len(matriz) == 0:
        print("\nNo hay recursos registrados todavia.")
        return

    horas_equipo = 0.0
    recursos_sobretiempo = 0
    nombre_mayor = ""
    horas_mayor = -1.0

    for registro in matriz:
        nombre, total_horas, clasificacion = analizar_recurso(registro)

        horas_equipo = horas_equipo + total_horas

        if clasificacion == JORNADA_SOBRETIEMPO:
            recursos_sobretiempo = recursos_sobretiempo + 1

        if total_horas > horas_mayor:
            horas_mayor = total_horas
            nombre_mayor = nombre

    promedio = horas_equipo / len(matriz)

    print("\n" + "-" * ANCHO_TABLA)
    print("RESUMEN DEL EQUIPO")
    print("-" * ANCHO_TABLA)
    print("Recursos registrados    :", len(matriz))
    print("Horas totales del equipo:", formatear_horas(horas_equipo))
    print("Promedio por recurso    :", formatear_horas(promedio))
    print("Recursos en sobretiempo :", recursos_sobretiempo, "de", len(matriz))
    print("Recurso con mas horas   :", nombre_mayor,
          "con", formatear_horas(horas_mayor), "horas")
    print("-" * ANCHO_TABLA)


# ======================= FUNCIONES DE ENTRADA DE DATOS =======================

def leer_horas(mensaje):
    """Pide un numero de horas y no avanza hasta que el dato sea valido.

    Valida con un ciclo while que el texto escrito sea un numero y que este
    dentro del rango permitido para un dia (0 a 24 horas).
    """
    while True:
        texto = input(mensaje).strip().replace(",", ".")

        try:
            horas = float(texto)
        except ValueError:
            print("   Dato invalido: escriba un numero, por ejemplo 8 o 7.5")
            continue

        if horas < HORAS_MIN_DIA or horas > HORAS_MAX_DIA:
            print("   Fuera de rango: las horas de un dia van de",
                  HORAS_MIN_DIA, "a", HORAS_MAX_DIA)
            continue

        return horas


def agregar_recurso(matriz):
    """Agrega un recurso nuevo a la matriz pidiendo su nombre y sus cinco dias.

    El nombre se valida con un while (no puede quedar vacio) y las horas se
    piden con un for que recorre la tupla DIAS, de manera que si la empresa
    agrega el sabado solo hay que modificar esa constante.
    """
    print("\n--- Registrar un recurso nuevo ---")

    while True:
        nombre = input("Nombre del recurso: ").strip()
        if nombre != "":
            break
        print("   El nombre no puede quedar vacio.")

    registro = [nombre]
    for dia in DIAS:
        horas = leer_horas("Horas del " + dia + ": ")
        registro.append(horas)

    matriz.append(registro)

    nombre, total_horas, clasificacion = analizar_recurso(registro)
    print("\nRecurso agregado:", nombre,
          "| Total:", formatear_horas(total_horas), "horas",
          "| Jornada:", clasificacion)


# ============================ PROGRAMA PRINCIPAL =============================

def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n" + "=" * 46)
    print("  CONTROL DE HORAS SEMANALES - FASE 5")
    print("=" * 46)
    print("  1. Ver informe de horas y clasificacion")
    print("  2. Ver resumen del equipo")
    print("  3. Registrar un recurso nuevo")
    print("  4. Salir")
    print("=" * 46)


def menu_principal():
    """Controla el flujo del programa con un ciclo while y un if / elif."""
    matriz = MATRIZ_HORAS

    print("\nBienvenido. El programa inicia con", len(matriz),
          "recursos cargados.")

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion == "1":
            mostrar_informe(matriz)
        elif opcion == "2":
            mostrar_resumen(matriz)
        elif opcion == "3":
            agregar_recurso(matriz)
        elif opcion == "4":
            print("\nPrograma finalizado. Gracias por usar el sistema.")
            continuar = False
        else:
            print("\nOpcion invalida: debe escribir un numero del 1 al 4.")


# Punto de entrada del programa.
if __name__ == "__main__":
    menu_principal()
