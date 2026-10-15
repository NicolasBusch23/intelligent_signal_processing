import numpy as np

# Diccionario de id de productos con sus valores de utilidad y pesos
dict_productos = {
    1: {"elemento": "Kit de Primeros Auxilios Avanzado", "valor": 91, "peso": 39},
    2: {"elemento": "Desfibrilador Portátil", "valor": 24, "peso": 12},
    3: {"elemento": "Manta Térmica de Emergencia (Pack x50)", "valor": 13, "peso": 29},
    4: {"elemento": "Pastillas Purificadoras de Agua (Caja)", "valor": 45, "peso": 10},
    5: {"elemento": "Raciones de Comida MRE (Pack x20)", "valor": 41, "peso": 40},
    6: {"elemento": "Generador Eléctrico Pequeño", "valor": 38, "peso": 23},
    7: {"elemento": "Kit de Herramientas de Rescate", "valor": 27, "peso": 45},
    8: {"elemento": "Tienda de Campaña Familiar", "valor": 23, "peso": 44},
    9: {"elemento": "Linternas Recargables (Pack x15)", "valor": 96, "peso": 28},
    10: {"elemento": "Antibióticos de Amplio Espectro (Caja)", "valor": 79, "peso": 41},
    11: {"elemento": "Radio de Comunicación Satelital", "valor": 21, "peso": 17},
    12: {"elemento": "Suero Fisiológico Flujo Alto (Caja)", "valor": 85, "peso": 50},
    13: {"elemento": "Kit de Costura y Sutura Médica", "valor": 64, "peso": 9},
    14: {"elemento": "Oxímetro y Tensiómetro Digital", "valor": 14, "peso": 7},
    15: {"elemento": "Analgésicos Fuertes (Caja)", "valor": 13, "peso": 47},
    16: {"elemento": "Camilla Plegable de Lona", "valor": 21, "peso": 19},
    17: {"elemento": "Botellas de Agua Mineral (Pack x24)", "valor": 37, "peso": 23},
    18: {"elemento": "Kit de Higiene Femenina (Caja)", "valor": 39, "peso": 10},
    19: {"elemento": "Leche en Polvo Infantil (Caja)", "valor": 74, "peso": 19},
    20: {"elemento": "Repelente de Insectos Concentrado", "valor": 87, "peso": 11},
    21: {"elemento": "Jabón Antiséptico Líquido (Bidón)", "valor": 13, "peso": 29},
    22: {"elemento": "Pañales para Bebé (Caja Grande)", "valor": 81, "peso": 22},
    23: {"elemento": "Combustible para Generador (Bidón)", "valor": 35, "peso": 34},
    24: {"elemento": "Ropa de Abrigo Surtida (Caja)", "valor": 93, "peso": 45},
    25: {"elemento": "Vacunas Críticas contra Hepatitis", "valor": 99, "peso": 28},
    26: {"elemento": "Impermeables para Lluvia (Pack x30)", "valor": 79, "peso": 15},
    27: {"elemento": "Bengalas y Señales de Humo", "valor": 63, "peso": 28},
    28: {"elemento": "Guantes Quirúrgicos (Caja x500)", "valor": 38, "peso": 27},
    29: {"elemento": "Linternas de Cabeza para Rescatistas", "valor": 67, "peso": 18},
    30: {"elemento": "Kit de Intubación Pediátrica", "valor": 85, "peso": 47},
    31: {"elemento": "Kit Quirúrgico Menor", "valor": 45, "peso": 22},
    32: {"elemento": "Camillas de Inmovilización Espinal", "valor": 10, "peso": 49},
    33: {"elemento": "Desinfectante de Superficies Médicas", "valor": 30, "peso": 48},
    34: {"elemento": "Equipos de Protección EPP (Caja)", "valor": 99, "peso": 46},
    35: {"elemento": "Insulina y Nevera de Transporte", "valor": 64, "peso": 9},
    36: {"elemento": "Baterías Externas Powerbank (Pack)", "valor": 53, "peso": 43},
    37: {"elemento": "Kit de Ferulización de Miembros", "valor": 45, "peso": 45},
    38: {"elemento": "Megáfono a Baterías", "valor": 29, "peso": 15},
    39: {"elemento": "Kit de Herramientas Multiusos", "valor": 37, "peso": 39},
    40: {"elemento": "Antivenenos para Mordedura de Serpiente", "valor": 53, "peso": 20},
    41: {"elemento": "Apósitos y Gasas Estériles (Caja)", "valor": 23, "peso": 15},
    42: {"elemento": "Máscaras de Oxígeno con Reservorio", "valor": 21, "peso": 34},
    43: {"elemento": "Alcohol Isopropílico (Bidón)", "valor": 58, "peso": 29},
    44: {"elemento": "Suero Oral en Polvo (Caja x100)", "valor": 22, "peso": 22},
    45: {"elemento": "Sacos de Dormir Térmicos", "valor": 55, "peso": 45},
    46: {"elemento": "Kit Tratamiento de Quemaduras", "valor": 54, "peso": 49},
    47: {"elemento": "Unidad de Purificación Filtración Portátil", "valor": 87, "peso": 40},
    48: {"elemento": "Alimentos Deshidratados Energéticos", "valor": 43, "peso": 19},
    49: {"elemento": "Estufas Portátiles de Gas", "valor": 15, "peso": 48},
    50: {"elemento": "Kit de Iluminación Perimetral LED", "valor": 68, "peso": 25}
}

def calcular_peso(muestra):
    indices_productos = [i for i in range(1,51) if muestra[i-1] == 1]  # Lista de indices asociados a productos seleccionados
    # print(indices_productos)
    peso_total = 0
    for producto in indices_productos:
        peso_total += dict_productos[producto]["peso"]

    return peso_total

def calcular_utilidad(muestra):
    indices_productos = [i for i in range(1,51) if muestra[i-1] == 1]  # Lista de indices asociados a productos seleccionados
    # print(indices_productos)
    utilidad_total = 0
    for producto in indices_productos:
        utilidad_total += dict_productos[producto]["valor"]

    return utilidad_total


#---- S: Candidato inicial
def candidato_inicial():
    while True:
        muestra = np.random.randint(0, 2, size = 50)  # Vector de 0s y 1s
        # 0: No se selecciona el producto
        # 1: Se selecciona el producto

        if calcular_peso(muestra) <= 591:
            S = muestra # Candidato inicial
            break

    print("----- Candidato inicial (S) -----")
    indices_productos = [i for i in range(1,51) if S[i-1] == 1]
    print(f"Productos seleccionados: {indices_productos}")
    print(f"Peso total: {calcular_peso(S)} kg")
    print(f"Utilidad total: {calcular_utilidad(S)}")

    return S