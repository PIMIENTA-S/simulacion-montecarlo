import numpy as np

# Parámetros del problema
costos = [1.5, 2.0]  # Rango de costos posibles por almanaque
precio_venta = 4.5
reembolso = 0.75
probabilidades = [0.3, 0.2, 0.3, 0.15, 0.05]
demandas = [100, 150, 200, 250, 300]
m = 10000  # Número de simulaciones para cada nivel de pedido

def calcular_ganancias(encargo, costo):
    ganancias = []
    for _ in range(m):
        # Simulamos la demanda de acuerdo con la distribución de probabilidades
        demanda = np.random.choice(demandas, p=probabilidades)
        
        # Calcular ganancia según la demanda y el pedido
        if demanda <= encargo:
            # Sobrante, entonces venderemos solo la demanda y devolveremos el sobrante
            ingreso_ventas = demanda * precio_venta
            costo_total = encargo * costo
            reembolso_total = (encargo - demanda) * reembolso
            ganancia = ingreso_ventas - costo_total + reembolso_total
        else:
            # Vendemos todo lo que encargamos
            ingreso_ventas = encargo * precio_venta
            costo_total = encargo * costo
            ganancia = ingreso_ventas - costo_total

        ganancias.append(ganancia)
    
    return np.mean(ganancias)  # Ganancia promedio para este nivel de encargo

# Probar diferentes niveles de encargo y costos
resultados = {}
for encargo in range(100, 350, 50):  # Niveles de encargo de 100 a 300
    for costo in costos:
        ganancia_promedio = calcular_ganancias(encargo, costo)
        resultados[(encargo, costo)] = ganancia_promedio

# Encontrar el mejor pedido en términos de ganancia promedio
mejor_encargo = max(resultados, key=resultados.get)
mejor_ganancia = resultados[mejor_encargo]

print(f"Mejor encargo: {mejor_encargo[0]} almanaques a un costo de ${mejor_encargo[1]} por unidad")
print(f"Ganancia promedio esperada: ${mejor_ganancia:.2f}")
