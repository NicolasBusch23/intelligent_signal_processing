##################################
# Referencias:
# - 
# - https://www.youtube.com/watch?v=CBTEVFphv-E
##################################

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#-- Funciones auxiliares
def graf_funciones_pertenencia(x1, servicio_sets, x2, comida_sets, y, propina_sets, figsize=(10, 8)):
    """
    Visualiza las funciones de pertenencia para las variables de entrada y salida
    recibiendo los conjuntos difusos agrupados en tuplas o listas.

    Parámetros:
    - x1: Vector del universo de discurso para la primera variable (ej. servicio)
    - servicio_sets: Lista de tuplas con formato [('Etiqueta', conjunto_array, 'color')]
    - x2: Vector del universo de discurso para la segunda variable (ej. comida)
    - comida_sets: Lista de tuplas con formato [('Etiqueta', conjunto_array, 'color')]
    - y: Vector del universo de discurso para la salida (ej. propina)
    - propina_sets: Lista de tuplas con formato [('Etiqueta', conjunto_array, 'color')]
    - figsize: Tupla opcional con las dimensiones de la figura (ancho, alto)

    Retorna:
    - fig: Objeto Figure de Matplotlib
    - axes: Arreglo de ejes (Axes) de los subplots
    """
    # Estructura que agrupa vectores, nombres de eje y conjuntos
    configuracion = [
        (x1, 'Calidad del Servicio', servicio_sets),
        (x2, 'Calidad de la Comida', comida_sets),
        (y, 'Propina (%)', propina_sets)
    ]

    # Crear cuadrícula 2x2 de subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=figsize)
    axes_flat = axes.flatten()

    # Graficar cada variable en su respectivo cuadrante
    for ax, (x_vec, xlabel, curvas) in zip(axes_flat[:3], configuracion):
        for etiqueta, conjunto, color in curvas:
            ax.plot(x_vec, conjunto, color=color, linewidth=1.5, label=etiqueta)
        
        ax.set_ylabel('Grado de Pertenencia')
        ax.set_xlabel(xlabel)
        ax.legend(loc='upper right')
        ax.grid(True)

    # Eliminar el cuarto cuadrante (vacío)
    fig.delaxes(axes_flat[3])

    plt.suptitle('Funciones de Pertenencia del Sistema Difuso', fontsize=13)
    plt.tight_layout()
    plt.show()

    return fig, axes

def graficar_union_conjuntos(y_propina, pertenencias, conjuntos_base, graficar = False):
    """
    Calcula los recortes de pertenencia y la unión final de conjuntos difusos.
    
    Parámetros:
    - y_propina: Vector del universo de discurso (0 a 25)
    - pertenencias: Lista o tupla [pertenencia_propina_baja, pertenencia_propina_media, pertenencia_propina_alta]
    - conjuntos_base: Lista o tupla [propina_baja, propina_media, propina_alta]
    """
    pertenencia_propina_baja, pertenencia_propina_media, pertenencia_propina_alta = pertenencias
    conjunto_propina_baja, conjunto_propina_media, conjunto_propina_alta = conjuntos_base

    # Recorte de cada conjunto según su grado de pertenencia
    conjunto_1 = np.fmin(pertenencia_propina_baja, conjunto_propina_baja)
    conjunto_2 = np.fmin(pertenencia_propina_media, conjunto_propina_media)
    conjunto_3 = np.fmin(pertenencia_propina_alta, conjunto_propina_alta)

    # Unión de los conjuntos (equivalente a np.fmax de los tres)
    union_conjuntos = np.maximum.reduce([conjunto_1, conjunto_2, conjunto_3])

    if graficar:
        # Visualización
        fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(10, 9), sharex=True)

        # Subplot 1: conjunto_1
        ax0.plot(y_propina, conjunto_propina_baja, 'b--', linewidth=1, label='propina_baja')
        ax0.axhline(y=pertenencia_propina_baja, color='b', linestyle='-', label=f'pertenencia ({pertenencia_propina_baja:.2f})')
        ax0.fill_between(y_propina, 0, conjunto_1, facecolor='blue', alpha=0.4, label='conjunto_1')
        ax0.set_title('conjunto_1 = np.fmin(pertenencia_propina_baja, conjunto_propina_baja)')
        ax0.set_ylabel('Pertenencia')
        ax0.legend(loc='upper right')
        ax0.grid(True)

        # Subplot 2: conjunto_2
        ax1.plot(y_propina, conjunto_propina_media, 'g--', linewidth=1, label='propina_media')
        ax1.axhline(y=pertenencia_propina_media, color='g', linestyle='-', label=f'pertenencia ({pertenencia_propina_media:.2f})')
        ax1.fill_between(y_propina, 0, conjunto_2, facecolor='green', alpha=0.4, label='conjunto_2')
        ax1.set_title('conjunto_2 = np.fmin(pertenencia_propina_media, conjunto_propina_media)')
        ax1.set_ylabel('Pertenencia')
        ax1.legend(loc='upper right')
        ax1.grid(True)

        # Subplot 3: conjunto_3
        ax2.plot(y_propina, conjunto_propina_alta, 'r--', linewidth=1, label='propina_alta')
        ax2.axhline(y=pertenencia_propina_alta, color='r', linestyle='-', label=f'pertenencia ({pertenencia_propina_alta:.2f})')
        ax2.fill_between(y_propina, 0, conjunto_3, facecolor='red', alpha=0.4, label='conjunto_3')
        ax2.set_title('conjunto_3 = np.fmin(pertenencia_propina_alta, conjunto_propina_alta)')
        ax2.set_ylabel('Pertenencia')
        ax2.legend(loc='upper right')
        ax2.grid(True)

        # Subplot 4: union_conjuntos
        ax3.plot(y_propina, conjunto_1, 'b--', alpha=0.6, label='conjunto_1')
        ax3.plot(y_propina, conjunto_2, 'g--', alpha=0.6, label='conjunto_2')
        ax3.plot(y_propina, conjunto_3, 'r--', alpha=0.6, label='conjunto_3')
        ax3.fill_between(y_propina, 0, union_conjuntos, facecolor='orange', alpha=0.6, edgecolor='darkorange', linewidth=2, label='union_conjuntos')
        ax3.set_title('union_conjuntos = np.fmax(conjunto_1, conjunto_2, conjunto_3)')
        ax3.set_xlabel('Propina (%)')
        ax3.set_ylabel('Pertenencia')
        ax3.legend(loc='upper right')
        ax3.grid(True)

        plt.tight_layout()
        plt.show()

    return union_conjuntos

def calculo_propina(val_servicio, val_comida, caso_prueba = False):
    """
    Calcula la propina sugerida basada en la calidad del servicio y la comida usando lógica difusa.

    Parámetros:
    - val_servicio: Calidad del servicio (0 a 10)
    - val_comida: Calidad de la comida (0 a 10)
    - caso_prueba: Booleano que indica si se deben graficar los resultados de la inferencia difusa (ideal para visualizar el proceso paso a paso)

    Retorna:
    - propina: Propina sugerida en porcentaje (0% a 25%)
    """

    #---- 1. Definición de variables y funciones de pertenencia

    #-- Dominio de variables de entrada (servicio y comida) y salida (propina)
    x1_servicio = np.linspace(0, 10, 1000) # Calidad de atención del servicio (0 a 10)
    x2_comida = np.linspace(0, 10, 1000) # Calidad de la comida (0 a 10)
    y_propina = np.linspace(0, 25, 1000) # Propina (0% a 25%)

    #-- Funciones de pertenencia

    # Servicio: Pobre, Aceptable, Alto
    conjunto_servicio_pobre = fuzz.zmf(x1_servicio, 0, 5)
    conjunto_servicio_aceptable = fuzz.trimf(x1_servicio, [0, 5, 10])
    conjunto_servicio_alto = fuzz.smf(x1_servicio, 5, 10)

    # Comida: Mala, Regular, Muy Buena
    conjunto_comida_mala = fuzz.zmf(x2_comida, 0, 5)
    conjunto_comida_regular = fuzz.gaussmf(x2_comida, 5, 1)
    conjunto_comida_muy_buena = fuzz.smf(x2_comida, 5, 10)

    # Propina: Baja, Media, Alta
    conjunto_propina_baja = fuzz.trapmf(y_propina, [0, 0, 2.5, 8])
    conjunto_propina_media = fuzz.trimf(y_propina, [5, 10, 15])
    conjunto_propina_alta = fuzz.trapmf(y_propina, [12, 20, 25, 25])

    if caso_prueba:
        graf_funciones_pertenencia(
            x1 = x1_servicio,
            servicio_sets = [
                ('Pobre', conjunto_servicio_pobre, 'b'),
                ('Aceptable', conjunto_servicio_aceptable, 'g'),
                ('Alto', conjunto_servicio_alto, 'r')
            ],
            x2 = x2_comida,
            comida_sets = [
                ('Mala', conjunto_comida_mala, 'b'),
                ('Regular', conjunto_comida_regular, 'g'),
                ('Muy Buena', conjunto_comida_muy_buena, 'r')
            ],
            y = y_propina,
            propina_sets = [
                ('Baja', conjunto_propina_baja, 'b'),
                ('Media', conjunto_propina_media, 'g'),
                ('Alta', conjunto_propina_alta, 'r')
            ]
        )

    #---- 2. Fuzzificación de los valores de entrada
    s_pobre = fuzz.interp_membership(x1_servicio, conjunto_servicio_pobre, val_servicio)
    s_aceptable = fuzz.interp_membership(x1_servicio, conjunto_servicio_aceptable, val_servicio)
    s_alto = fuzz.interp_membership(x1_servicio, conjunto_servicio_alto, val_servicio)

    c_mala = fuzz.interp_membership(x2_comida, conjunto_comida_mala, val_comida)
    c_regular = fuzz.interp_membership(x2_comida, conjunto_comida_regular, val_comida)
    c_muy_buena = fuzz.interp_membership(x2_comida, conjunto_comida_muy_buena, val_comida)

    #---- 3.1. Inferencia y aplicación de reglas difusas
    # Regla 1: Si s_pobre V (s_aceptable Λ c_mala) entonces propina_baja
    pertenencia_propina_baja = np.fmax(s_pobre, np.fmin(s_aceptable, c_mala))
    if caso_prueba:
        print(f"Grado de pertenencia a Propina Baja: {pertenencia_propina_baja}")

    # Regla 2: Si s_aceptable V ((s_alto Λ c_regular) V (s_alto Λ c_mala)) entonces propina_media
    pertenencia_propina_media = np.fmax(s_aceptable, np.fmax(np.fmin(s_alto, c_regular), np.fmin(s_alto, c_mala)))
    if caso_prueba:
        print(f"Grado de pertenencia a Propina Media: {pertenencia_propina_media}")

    # Regla 3: Si s_alto Λ c_muy_buena entonces propina_alta
    pertenencia_propina_alta = np.fmin(s_alto, c_muy_buena)
    if caso_prueba:
        print(f"Grado de pertenencia a Propina Alta: {pertenencia_propina_alta}")

    # --- 3.2. 
    union_conjuntos = graficar_union_conjuntos(
        y_propina = y_propina,
        pertenencias = [pertenencia_propina_baja, pertenencia_propina_media, pertenencia_propina_alta],
        conjuntos_base = [conjunto_propina_baja, conjunto_propina_media, conjunto_propina_alta],
        graficar = caso_prueba
    )

    # --- 4. Defuzzificación
    propina = fuzz.defuzz(y_propina, union_conjuntos, 'centroid')
    return propina

# Caso de prueba+
print("\n--- Caso de prueba: Cálculo de propina sugerida ---")
val_servicio = float(input("Ingrese la calidad del servicio (0 a 10): "))
val_comida = float(input("Ingrese la calidad de la comida (0 a 10): "))
propina = calculo_propina(val_servicio, val_comida, caso_prueba = True)
print(f"Propina sugerida: {propina:.2f}%")

# Gráfico de superficie de control difusa
print("\n--- Superficie de Control Difusa ---")
graficar_superficie = input("Graficar la superficie de control difusa? (s/n): ").strip().lower()
if graficar_superficie == 's':
    x1_servicio = np.linspace(0, 10, 1000) # Calidad de atención del servicio (0 a 10)
    x2_comida = np.linspace(0, 10, 1000) # Calidad de la comida (0 a 10)
    y_propina = np.linspace(0, 25, 1000) # Propina (0% a 25%)

    x1_valores = np.linspace(0, 10, 40)
    x2_valores = np.linspace(0, 10, 40)
    x1_servicio, x2_comida = np.meshgrid(x1_valores, x2_valores)
    Z = np.empty_like(x1_servicio)
    for fila in range(x1_servicio.shape[0]):
        for columna in range(x1_servicio.shape[1]):
            Z[fila, columna] = calculo_propina(
                x1_servicio[fila, columna], x2_comida[fila, columna],
                caso_prueba = False
            )

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x1_servicio, x2_comida, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('X1: Calidad del Servicio')
    ax.set_ylabel('X2: Calidad de la Comida')
    ax.set_zlabel('Z: Propina (%)')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title('Superficie 3D de propina = f(calidad del servicio, calidad de la comida)')
    plt.show()

