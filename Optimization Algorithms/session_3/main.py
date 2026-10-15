import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import auxiliar as aux

df = pd.read_csv(f"session_3\\problem.csv")
indice_ciudades = list(df.index)

poblacion = {}
tamaño_poblacion = 100
pct_truncamiento = 0.20  # 20% de mejores soluciones como padres
prob_mutacion = 0.15  # Probabilidad de mutar
n_swaps = 2  # Cantidad de intercambios al mutar
max_estancamiento = 50  # Stall condition

for k in range(tamaño_poblacion):
    cromosoma = indice_ciudades.copy()
    np.random.shuffle(cromosoma) # Baraje aleatorio de 'indice_ciudades'
    distancia = aux.fitness(cromosoma, df)

    poblacion[tuple(cromosoma)] = distancia

# Para ordenar la poblacion de menor distancia a mayor distancia
poblacion_ordenada = dict(sorted(poblacion.items(), key = lambda item: item[1]))

# Gráfica interactiva
plt.ion()  # Modo interactivo de matplotlib
fig = plt.figure(figsize=(7, 7))

# Bucle principal
mejor_distancia_global = list(poblacion_ordenada.values())[0]
contador_estancamiento = 0
generacion = 0
historial_distancia = []

while contador_estancamiento < max_estancamiento:
  generacion += 1

  # Seleccionar padres mediante truncamiento
  padres = aux.seleccion_truncamiento(poblacion_ordenada, pct_truncamiento)

  # Generar nueva población
  nueva_poblacion = {}
  while len(nueva_poblacion) < tamaño_poblacion:
    idx1, idx2 = np.random.choice(len(padres), size=2, replace=False)
    hijo = aux.cruce_ox(padres[idx1], padres[idx2])
    hijo_mutado = aux.mutacion(hijo, prob_mutacion, n_swaps)

    distancia = aux.fitness(hijo_mutado, df)
    nueva_poblacion[hijo_mutado] = distancia

  # Ordenar la nueva población
  poblacion_ordenada = dict(
      sorted(nueva_poblacion.items(), key=lambda item: item[1])
  )

  mejor_recorrido_actual = list(poblacion_ordenada.keys())[0]
  mejor_distancia_actual = list(poblacion_ordenada.values())[0]
  historial_distancia.append(mejor_distancia_actual)

  # Dibujar frame actual
  aux.graficar_evolucion(
      df,
      mejor_recorrido_actual,
      historial_distancia,
      generacion,
      mejor_distancia_actual,
  )

  # Evaluación de mejora para el contador
  if mejor_distancia_actual < mejor_distancia_global:
    mejor_distancia_global = mejor_distancia_actual
    contador_estancamiento = 0  # Reiniciar contador si hay mejora
  else:
    contador_estancamiento += 1  # Sumar si se estanca

plt.ioff()  # Desactivar modo interactivo al terminar
print(f"Algoritmo finalizado en la generación: {generacion}")
print(f"Mejor distancia encontrada: {mejor_distancia_global:.2f} km")
print(f"Mejor ruta: {list(poblacion_ordenada.keys())[0]}")
plt.show()