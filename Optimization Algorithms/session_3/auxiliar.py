import numpy as np
import matplotlib.pyplot as plt

def fitness(solucion, df):
    distancia = 0 

    N = len(solucion)
    for k in range(N-1):
        x1 = (df.iloc[solucion[k]])["x_km"]
        y1 = (df.iloc[solucion[k]])["y_km"]
        x2 = (df.iloc[solucion[k + 1]])["x_km"]
        y2 = (df.iloc[solucion[k + 1]])["y_km"]

        distancia += np.sqrt((x2-x1)**2 + (y2-y1)**2)

    return distancia

def seleccion_truncamiento(poblacion_ordenada, pct_truncamiento):
  # Selecciona el porcentaje de los mejores individuos como padres
  num_elegidos = max(2, int(len(poblacion_ordenada) * pct_truncamiento))
  padres = list(poblacion_ordenada.keys())[:num_elegidos]
  return padres


def cruce_ox(padre1, padre2):
  n = len(padre1)
  idx1, idx2 = sorted(np.random.choice(n, size=2, replace=False))

  print("\n=== INICIO CRUCE OX ===")
  print(f"Padre 1: {padre1}")
  print(f"Padre 2: {padre2}")
  print(f"Puntos de corte seleccionados: índice {idx1} hasta {idx2 - 1}")

  hijo = [None] * n
  hijo[idx1:idx2] = padre1[idx1:idx2]
  print(f"Hijo inicial (hereda segmento de Padre 1): {hijo}")

  pos = idx2
  secuencia_padre2 = list(padre2[idx2:]) + list(padre2[:idx2])
  print(f"Secuencia a revisar de Padre 2 (desde idx2): {secuencia_padre2}")

  for ciudad in secuencia_padre2:
    if ciudad not in hijo:
      if pos >= n:
        pos = 0
      hijo[pos] = ciudad
      print(f"  -> Insertada ciudad {ciudad} en pos {pos}: {hijo}")
      pos += 1
    else:
      print(f"  -> Ciudad {ciudad} omitida (ya está en el hijo)")

  resultado = tuple(hijo)
  print(f"Hijo final generado: {resultado}")
  print("=== FIN CRUCE OX ===\n")

  return resultado


def mutacion(cromosoma, prob_mutacion, n_swaps=1):
  # Intercambia posiciones aleatorias respetando la unicidad
  if np.random.rand() < prob_mutacion:
    cromosoma_lista = list(cromosoma)
    n = len(cromosoma_lista)
    for _ in range(n_swaps):
      i, j = np.random.choice(n, size=2, replace=False)
      cromosoma_lista[i], cromosoma_lista[j] = (
          cromosoma_lista[j],
          cromosoma_lista[i],
      )
    return tuple(cromosoma_lista)

  return cromosoma

def graficar_evolucion(
    df, mejor_recorrido, historial_distancia, generacion, mejor_distancia
):
  plt.clf()  # Limpiar la figura en cada frame

  # Subplot 1: Mapa del recorrido actual
  ax1 = plt.subplot(2, 1, 1)
  x = df.iloc[list(mejor_recorrido)]["x_km"].values
  y = df.iloc[list(mejor_recorrido)]["y_km"].values

  ax1.plot(x, y, "b-o", linewidth=0.8, markersize=5)

  for idx in mejor_recorrido:
    cx = df.iloc[idx]["x_km"]
    cy = df.iloc[idx]["y_km"]
    ax1.text(
        cx,
        cy,
        f" {idx}",
        fontsize=9,
        fontweight="bold",
        ha="left",
        va="bottom",
    )

  ax1.set_title(f"Problema del Vendedor Viajero - Generación {generacion}")
  ax1.set_xlabel("x [km]")
  ax1.set_ylabel("y [km]")
  ax1.grid(True, linestyle="--", alpha=0.5)

  # Subplot 2: Historial de la distancia
  ax2 = plt.subplot(2, 1, 2)
  ax2.plot(historial_distancia, "b-", linewidth=1.5)
  ax2.set_title(f"Distancia = {mejor_distancia:.2f} km")
  ax2.set_xlabel("Generaciones")
  ax2.set_ylabel("Distancia total [km]")
  ax2.grid(True, linestyle="--", alpha=0.5)

  plt.tight_layout()
  plt.pause(0.01)  # Refresco de la ventana interactiva

cruce_ox((0,1,2,3,4), (4,2,1,0,3))