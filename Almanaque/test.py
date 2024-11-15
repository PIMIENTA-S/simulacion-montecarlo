import numpy as np

# Configuración de valores de venta y probabilidades de demanda
almanaqueVendido = [100, 150, 200, 250, 300]
probabilidadVenta = [0.3, 0.2, 0.3, 0.15, 0.05]

def demanda():
    # Elegimos un valor de ventas basado en las probabilidades acumulativas
    return np.random.choice(almanaqueVendido, p=probabilidadVenta)

def calcularN(sigma):
    return ((1.96**2) * (sigma ** 2)) / 100

def main(n):
    # Generar precio y calcular demanda
    simulado = demanda()
    precio_simulado = 1.5 + (0.5 * np.random.random())
    
    # Ajustar la cantidad de demanda simulada si excede la cantidad importada
    simulado = min(simulado, n)
    no_vendidos = n - simulado

    # Calcular la utilidad máxima
    utilidad_maxima = (4.5 * simulado + no_vendidos * 0.75) - precio_simulado * n
    return utilidad_maxima

def main_section(n):
    # Simulación de utilidades
    utilidades = [main(n) for _ in range(10000)]
    desviacion_muestral = np.std(utilidades)
    n_optimo = calcularN(desviacion_muestral)
    print(f"Desviación estándar con un importe de {n} en muestra de 10000: {desviacion_muestral}")
    print(f"Con dicha desviación se calcula la cantidad óptima (N): {int(n_optimo)}")
    return int(n_optimo)

def intervalo_confianza(mean, sigma, n):
    margen_error = 1.96 * (sigma / np.sqrt(n))
    return [int(mean - margen_error), int(mean + margen_error)]

def master():
    for n in almanaqueVendido:
        n_ideal = main_section(n)
        
        # Calcular utilidad ideal y sus estadísticas
        utilidades_ideales = [main(n) for _ in range(n_ideal)]
        desviacion_ideal = np.std(utilidades_ideales)
        media_ideal_ganancias = np.mean(utilidades_ideales)
        confianza = intervalo_confianza(media_ideal_ganancias, desviacion_ideal, n_ideal)
        
        print(f"Desviación ideal: {desviacion_ideal}")
        print(f"Media ideal (X): {media_ideal_ganancias}")
        print(f"Con un intervalo de confianza de {confianza}\n")

master()
