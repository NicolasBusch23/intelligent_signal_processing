# Repositorio - Procesamiento Inteligente de Señales
**Universidad Nacional de Colombia - Sede Medellín**  
**Facultad de Minas**  
**Profesor:** Freddy Bolanos Martínez

**Autor:** Nicolás Buenaventura Schlesinger  

## *Estructura del Proyecto*

```text
.
├── session_1/
│   ├── rastrigin_exploitation.py
│   └── rosenbrock_exploitation.py
├── session_2/
│   ├── auxiliar.py
│   └── simulated_annealing.py
├── .gitignore
├── LICENSE
└── requirements.txt

```

## *Descripción del Proyecto*
## Sesión 1: Algoritmos de Hill Climbing (Explotación)

Desarrollo de un algoritmo de **Hill Climbing** centrado en la fase de **explotación** sobre las funciones de costo clásicas **Rosenbrock** y **Rastrigin**, con el objetivo de hallar la mejor solución alrededor de un punto de inicio aleatorio en el espacio de soluciones.

### Observaciones
* **Tamaño de paso:** Si bien es aleatorio, se restringe a valores pequeños para no incurrir en la fase de *Exploración*, la cual no es objeto de interés para este primer ejercicio.
* **Función Rosenbrock:** El algoritmo logra hallar el mínimo global dada la geometría continua de su superficie.
* **Función Rastrigin:** El algoritmo no logra hallar el mínimo global debido a la gran cantidad de mínimos locales en los que queda atrapado.

---

## Sesión 2: Simulated Annealing — Problema de la Mochila (Knapsack Problem)

Desarrollo de un algoritmo de **Simulated Annealing** (Recocido Simulado) enfocado en resolver el problema clásico de la mochila enunciado a continuación.

> ### Enunciado del Problema
> Una empresa de logística humanitaria está preparando un contenedor de rescate aéreo para enviarlo
a una zona afectada por una inundación masiva. El contenedor tiene una capacidad de peso
estrictamente limitada a 591 kg. Hay 50 suministros críticos listos para ser cargados. Cada uno tiene un peso diferente (en kg) y un nivel de beneficio/utilidad asignado por los médicos y rescatistas (en
una escala de 10 a 100 puntos). El objetivo es maximizar el beneficio total de los suministros
enviados sin exceder el peso máximo del contenedor.
> ### Inventario de Suministros
> | ID | Suministro / Elemento | Valor (Utilidad) | Peso (kg) |
> | :-: | :-- | :-: | :-: |
> | **1** | Kit de Primeros Auxilios Avanzado | 91 | 39 |
> | **2** | Desfibrilador Portátil | 24 | 12 |
> | **3** | Manta Térmica de Emergencia (Pack x50) | 13 | 29 |
> | **4** | Pastillas Purificadoras de Agua (Caja) | 45 | 10 |
> | **5** | Raciones de Comida MRE (Pack x20) | 41 | 40 |
> | **6** | Generador Eléctrico Pequeño | 38 | 23 |
> | **7** | Kit de Herramientas de Rescate | 27 | 45 |
> | **8** | Tienda de Campaña Familiar | 23 | 44 |
> | **9** | Linternas Recargables (Pack x15) | 96 | 28 |
> | **10** | Antibióticos de Amplio Espectro (Caja) | 79 | 41 |
> | **11** | Radio de Comunicación Satelital | 21 | 17 |
> | **12** | Suero Fisiológico Flujo Alto (Caja) | 85 | 50 |
> | **13** | Kit de Costura y Sutura Médica | 64 | 9 |
> | **14** | Oxímetro y Tensiómetro Digital | 14 | 7 |
> | **15** | Analgésicos Fuertes (Caja) | 13 | 47 |
> | **16** | Camilla Plegable de Lona | 21 | 19 |
> | **17** | Botellas de Agua Mineral (Pack x24) | 37 | 23 |
> | **18** | Kit de Higiene Femenina (Caja) | 39 | 10 |
> | **19** | Leche en Polvo Infantil (Caja) | 74 | 19 |
> | **20** | Repelente de Insectos Concentrado | 87 | 11 |
> | **21** | Jabón Antiséptico Líquido (Bidón) | 13 | 29 |
> | **22** | Pañales para Bebé (Caja Grande) | 81 | 22 |
> | **23** | Combustible para Generador (Bidón) | 35 | 34 |
> | **24** | Ropa de Abrigo Surtida (Caja) | 93 | 45 |
> | **25** | Vacunas Críticas contra Hepatitis | 99 | 28 |
> | **26** | Impermeables para Lluvia (Pack x30) | 79 | 15 |
> | **27** | Bengalas y Señales de Humo | 63 | 28 |
> | **28** | Guantes Quirúrgicos (Caja x500) | 38 | 27 |
> | **29** | Linternas de Cabeza para Rescatistas | 67 | 18 |
> | **30** | Kit de Intubación Pediátrica | 85 | 47 |
> | **31** | Kit Quirúrgico Menor | 45 | 22 |
> | **32** | Camillas de Inmovilización Espinal | 10 | 49 |
> | **33** | Desinfectante de Superficies Médicas | 30 | 48 |
> | **34** | Equipos de Protección EPP (Caja) | 99 | 46 |
> | **35** | Insulina y Nevera de Transporte | 64 | 9 |
> | **36** | Baterías Externas Powerbank (Pack) | 53 | 43 |
> | **37** | Kit de Ferulización de Miembros | 45 | 45 |
> | **38** | Megáfono a Baterías | 29 | 15 |
> | **39** | Kit de Herramientas Multiusos | 37 | 39 |
> | **40** | Antivenenos para Mordedura de Serpiente | 53 | 20 |
> | **41** | Apósitos y Gasas Estériles (Caja) | 23 | 15 |
> | **42** | Máscaras de Oxígeno con Reservorio | 21 | 34 |
> | **43** | Alcohol Isopropílico (Bidón) | 58 | 29 |
> | **44** | Suero Oral en Polvo (Caja x100) | 22 | 22 |
> | **45** | Sacos de Dormir Térmicos | 55 | 45 |
> | **46** | Kit Tratamiento de Quemaduras | 54 | 49 |
> | **47** | Unidad de Purificación Filtración Portátil | 87 | 40 |
> | **48** | Alimentos Deshidratados Energéticos | 43 | 19 |
> | **49** | Estufas Portátiles de Gas | 15 | 48 |
> | **50** | Kit de Iluminación Perimetral LED | 68 | 25 |


### Observaciones y Resultados

* **Análisis de Métricas:** Se realiza una comparación visual del desempeño mediante un gráfico de **Utilidad vs. Iteraciones**.
* **Reglas de Convergencia:** Se implementaron dos funciones de temperatura/enfriamiento (**exponencial** y **lineal**). Los comportamientos y resultados de cada una se pueden evaluar modificando el parámetro `type` dentro de la función `temperatura`.
* **Mecanismo de Modificación (*Tweak*):** Para evaluar la solución temporal frente a una solución modificada, se utiliza el parámetro `size` dentro de `np.random.randint()`, permitiendo variar de forma aleatoria la cantidad de elementos alterados en cada paso.
