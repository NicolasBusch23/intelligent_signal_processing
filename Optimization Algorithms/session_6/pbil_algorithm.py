##################################
# Referencias:
# - Llamar Matlab desde Python: https://la.mathworks.com/help/matlab/matlab-engine-for-python.html?s_tid=CRUX_lftnav
##################################

import numpy as np
import auxiliar as aux
import matplotlib.pyplot as plt
# import matlab
# import matlab.engine
# import os

N = 20 # Tamaño población
T = 1000 # Tamaño de semiciclo
P = [0.5] * T # Arreglo de probabilidades neutro
LR = 0.01 # Tasa de aprendizaje

# Historial
historial_thd = []
stall_counter = 0
MAX_STALL = 1000
contador = 0

while True:
    contador += 1
    poblacion = ((np.random.rand(N, T)) < P).astype(float) # Genera una matriz 'N x 1000'
    # print(poblacion)

    l_THD = []

    for i in range(len(poblacion)):
        THD = aux.pwm_sin(list(poblacion[i]))

        if i == 0:
            min_THD = THD
            continue

        if THD < min_THD:
            # El mejor individuo de una población de tamaño N será aquel con menor THD
            min_THD = THD
            mejor_individuo = poblacion[i] 

    # print(mejor_individuo)

    historial_thd.append(min_THD)

    if contador == 1:
        global_min_THD = min_THD
        global_mejor_individuo = mejor_individuo.copy()
        continue

    if min_THD < global_min_THD:
        global_min_THD = min_THD
        global_mejor_individuo = mejor_individuo.copy()
        stall_counter = 0 
    else:
        stall_counter += 1  # Permanece sobre el mismo mínimo o empeora

    # Condición de parada
    if stall_counter >= MAX_STALL:
        print(f"Algoritmo finalizado en la iteración {contador}.")
        print(f"Permaneció {MAX_STALL} iteraciones consecutivas sin mejorar el mínimo THD ({global_min_THD:.6f}).")
        break

    # entropia_norm = aux.calc_entropia_norm(P)
    # LR = aux.LR(entropia_norm, "lineal")

    for k in range(len(P)):
        if mejor_individuo[k] == 1:
            P[k] = P[k] * (1 + LR)
        elif mejor_individuo[k] == 0:
            P[k] = P[k] * (1 - LR)

        # Para evitar probabilidades no válidas:
        if P[k] > 1:
            P[k] = 1
        elif P[k] < 0:
            P[k] = 0

    # print(P)


# Resultados Finales
print("--- RESULTADO FINAL DEL ALGORITMO ---")
print(f"Mínimo THD conseguido : {global_min_THD:.6f}")
print(f"Mejor Solución : \n{global_mejor_individuo}")


# Gráfica de Evolución
plt.figure(figsize=(9, 5))
plt.plot(historial_thd, color='#1f77b4', linewidth=1.5, label='Mínimo THD del ciclo')
plt.axhline(y=global_min_THD, color='red', linestyle='--', linewidth=1, label=f'THD Mínimo Final ({global_min_THD:.6f})')

plt.title('Evolución de la Distorsión Armónica (THD)')
plt.xlabel('Iteraciones / Generaciones')
plt.ylabel('THD')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# m = matlab.engine.start_matlab()
# script_dir = os.path.dirname(os.path.abspath(__file__))
# m.addpath(script_dir, nargout = 0)
# m.pwm_sin(global_mejor_individuo)

# m.quit()