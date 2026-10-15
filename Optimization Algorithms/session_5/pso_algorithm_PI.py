import numpy as np
import pyswarms as ps
import control as con

s = con.tf('s')
G = 0.9373 / (77 * s + 1)
ts_expected = 150.5

def evaluar_particula(p):
    Kp, Ki = p
    C = Kp + Ki / s
    lazo_c = con.feedback(C * G, 1)
    
    ts_actual = con.step_info(lazo_c)["SettlingTime"]
    return (ts_expected - ts_actual) ** 2

def funcion_coste(x):
    return np.array([evaluar_particula(p) for p in x])


# PSO
bounds = (np.array([0.01, 0.001]), np.array([10.0, 2.0])) # Límites [min_Kp, min_Ki], [max_Kp, max_Ki]
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

optimizer = ps.single.GlobalBestPSO(n_particles=25, dimensions=2, options=options, bounds=bounds)
best_cost, best_pos = optimizer.optimize(funcion_coste, iters=50)

print(f"Mejor Kp: {best_pos[0]:.4f}")
print(f"Mejor Ki: {best_pos[1]:.4f}")
print(f"Valor de la función de coste (SSE): {best_cost:.6f}")