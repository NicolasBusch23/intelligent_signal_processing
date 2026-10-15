import matplotlib.pyplot as plt
import numpy as np
import auxiliar as aux

def temperatura(x, type, T0, cooling):
    """
    x: variable independiente 
    type: tipo de distribución de temperatura ("exponencial" o "lineal")
    T0: temperatura inicial
    cooling: velocidad de enfriamiento
    """
    if type == "exponencial":
        return T0 * np.exp(-cooling * x)
    elif type == "lineal":
        return T0 - cooling * x

# Inicialización de parámetros
iteraciones = 10000
tipo = "exponencial"
T0 = iteraciones
cooling = 0.001

# Gráfico de función de temperatura
plt.figure()
k = np.arange(0, iteraciones, 1)
t = temperatura(k, tipo, T0, cooling)
plt.plot(k, t)
plt.title("Temperatura vs número de iteraciones")
plt.xlabel("Número de iteraciones")
plt.ylabel("Temperatura")
plt.grid()
plt.show()

# Algoritmo de Simulated Annealing
S = aux.candidato_inicial()
candidatos = []

for i in range(10000):
    t = temperatura(i, tipo, T0, cooling)
    candidatos.append(aux.calcular_utilidad(S.copy()))

    #---- R: Modificación del candidato inicial S
    while True:
        S_mod = S.copy()

        # Tweak
        posicion = np.random.randint(0, len(S_mod), size = 3) # Seleccionar una posición aleatoria
        for k in posicion:
           S_mod[k] = 1 - S[k]  # Cambiar el valor del elemento en la posición seleccionada

        if aux.calcular_peso(S_mod) <= 591:
            R = S_mod # Modificación del candidato inicial S
            break  # Si el peso total es menor o igual a 591 kg, se rompe el bucle

    if aux.calcular_utilidad(R) > aux.calcular_utilidad(S) or np.random.rand() < np.exp((aux.calcular_utilidad(R) - aux.calcular_utilidad(S)) / t):
        S = R
    elif aux.calcular_utilidad(S) >= aux.calcular_utilidad(R):
        S = S

# Mejor candidato encontrado
print("----- Candidato optimo (Best) -----")
indices_productos = [i for i in range(1,51) if S[i-1] == 1]
print(f"Productos seleccionados: {indices_productos}")
print(f"Peso total: {aux.calcular_peso(S)} kg")
print(f"Utilidad total: {aux.calcular_utilidad(S)}")

# Gráfico de utilidad de los candidatos a lo largo de las iteraciones
plt.figure()
plt.plot(range(len(candidatos)), candidatos)
plt.title("Utilidad de los candidatos a lo largo de las iteraciones")
plt.xlabel("Número de iteraciones")
plt.ylabel("Utilidad")
plt.grid()
plt.show()