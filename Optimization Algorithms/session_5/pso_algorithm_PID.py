import numpy as np
import pyswarms as ps
import control as con
import matplotlib.pyplot as plt

s = con.tf('s')
G = 0.1562 / (116 * s + 1)
# ts_expected = 150.5

def evaluar_particula(p):
    Kp, Ki, Kd, tao_d = p
    C = Kp + Ki / s + s * Kd /( tao_d * s + 1 )
    lazo_c = con.feedback(C * G, 1)
    
    ts_actual = con.step_info(lazo_c)["SettlingTime"]
    return ts_actual

def funcion_coste(x):
    return np.array([evaluar_particula(p) for p in x])


# PSO
bounds = (np.array([0.01, 0.001, 0.001, 0.01]), np.array([10.0, 2.0, 2.0, 2.0])) # Límites [min_Kp, min_Ki, min_Kd, min_tao_d], [max_Kp, max_Ki, max_Kd, max_tao_d]
options = {'c1': 0.5, 'c2': 0.5, 'w': 0.9}
# c1: componente cognitivo, c2: componente social, w: punto inicial

optimizer = ps.single.GlobalBestPSO(n_particles=25, dimensions=4, options=options, bounds=bounds)
best_cost, best_pos = optimizer.optimize(funcion_coste, iters=50)

print(f"Mejor Kp: {best_pos[0]:.4f}")
print(f"Mejor Ki: {best_pos[1]:.4f}")
print(f"Mejor Kd: {best_pos[2]:.4f}")
print(f"Mejor tao_d: {best_pos[3]:.4f}")
print(f"Valor de la función de coste (t_s): {best_cost:.6f}")

# PID con menor función de coste
control_step = con.feedback((best_pos[0] + best_pos[1] / s + s * best_pos[2] / (best_pos[3] * s + 1)) * G, 1)
t, y = con.step_response(control_step)

# Gráfico
plt.plot(t, y)
plt.title('Respuesta al Escalón del Sistema Controlado con PID Optimizado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida') 
plt.axhline(1.01, color='r', linestyle='--')
plt.axhline(0.99, color='r', linestyle='--')
plt.grid()
plt.show()