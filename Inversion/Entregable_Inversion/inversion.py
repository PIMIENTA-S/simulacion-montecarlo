# Función que genera una observación de la distribución triangular
# triang(a,b,c) parámetros a: mín, c: moda, b: máx
# método usado: inversión

import random
import math
import numpy as np
import matplotlib.pyplot as plt

def triangular(ei,moda,ed):
  a=ei
  b=ed
  c=moda
  r=random.random()
  #para x entre a y c, r=(x-a)^2/(b-a)(c-a)
  #si x=a, r=0
  #si x=c, r=(c-a)/(b-a)
  r1=(c-a)/(b-a)
  #print(r)
  if r <=r1:
    obs=a+math.sqrt(r*(b-a)*(c-a))
  else :
    obs=b-math.sqrt((1-r)*(b-a)*(b-c))
  return(obs)

def calcularN(sigma, d):
    # Fórmula basada en la desviación estándar y un margen de error deseado
    n = ((1.96**2) * (sigma ** 2)) / d**2
    return n

# Función para calcular los intervalos de confianza
def intervalo_confianza(mean, sigma, n):
    # Calculamos los límites superior e inferior del intervalo
    limite_1 = mean + (1.96 * (sigma / np.sqrt(n)))
    limite_2 = mean - (1.96 * (sigma / np.sqrt(n)))
    return [int(limite_2), int(limite_1)]  # Retornamos los límites como enteros

# Lista global para guardar los resultados de VPN
vpn_copy = []

# Función principal para simular el cálculo del VPN
def simular(n, opcion):
    costo_fijo = 700000000  # Valor del costo fijo inicial
    vpn_lista = []  # Lista para guardar los resultados de cada simulación

    # Repetimos la simulación "n" veces
    for i in range(n):
        vpn = 0  # Inicializamos el VPN en 0 para cada iteración
        valor_1 = 50000  # Valor inicial para el rango bajo de ventas
        valor_2 = 75000  # Valor inicial para el rango medio
        valor_3 = 85000  # Valor inicial para el rango alto
        margen = 4000  # Margen inicial

        # Recorremos 5 años (periodo de análisis)
        for j in range(5):
            # Si usamos el costo triangular, lo calculamos
            if opcion == 1:
                costo_fijo = triangular(600, 650, 850) * 1000000
            
            # Si no es el primer año, aplicamos disminuciones en ventas y margen
            if j != 0:
                disminucion_ventas = triangular(0.05, 0.08, 0.10)  # Cambio en ventas
                valor_1 *= (1 - disminucion_ventas)
                valor_2 *= (1 - disminucion_ventas)
                valor_3 *= (1 - disminucion_ventas)
                margen *= 0.96  # Margen disminuye en un 4%

            # Calculamos las ventas anuales basadas en la distribución triangular
            ventas_anio = triangular(valor_1, valor_2, valor_3)

            # Calculamos las contribuciones y flujo de caja
            contribucion = margen * ventas_anio
            depreciacion = costo_fijo / 5  # La depreciación se reparte en 5 años
            utilidad_antes_impuestos = contribucion - depreciacion
            utilidad_despues_impuestos = utilidad_antes_impuestos * 0.60  # Aplicamos impuestos
            flujo_caja_final = utilidad_despues_impuestos + depreciacion
            # Actualizamos el VPN con el flujo de caja descontado
            vpn += flujo_caja_final / ((0.1 + 1) ** (j + 1))
        
        # Guardamos el resultado de esta simulación
        vpn_lista.append(vpn)
        vpn_copy.append(vpn)

    # Calculamos la media y desviación estándar de los VPN obtenidos
    return [np.mean(vpn_lista), np.std(vpn_lista)]

# Simulación para un costo fijo de 700M
resultado = simular(20000, 0)  # Simulamos con 20,000 iteraciones
N = calcularN(resultado[1], 1000000)  # Calculamos el tamaño de muestra óptimo
resultado_con_N = simular(int(N), 0)  # Re-simulamos con el tamaño óptimo
intervalos_700 = intervalo_confianza(resultado[0], resultado[1], N)
intervalos_700_N = intervalo_confianza(resultado_con_N[0], resultado_con_N[1], N)

# Mostramos los resultados
print()
print("Costo fijo de 700M")
print(f"El intervalor de confianza para 10000 simulaciones {intervalos_700}")
print(f"El intervalor de confianza con N({int(N)}) óptimos es {intervalos_700_N}")

# Simulación para un costo basado en distribución triangular
resultado_triangular = simular(20000, 1)
N_Tr = calcularN(resultado_triangular[1], 1000000)
resultado_con_N_Triangular = simular(int(N_Tr), 1)
intervalos_triangular = intervalo_confianza(resultado_triangular[0], resultado_triangular[1], N_Tr)
intervalos_triangular_N = intervalo_confianza(resultado_con_N_Triangular[0], resultado_con_N_Triangular[1], N_Tr)

# Mostramos los resultados
print()
print("Costo triangular de 600,650,850")
print(f"El intervalor de confianza para 10000 simulaciones {intervalos_triangular}")
print(f"El intervalor de confianza con N({int(N_Tr)}) óptimos es {intervalos_triangular_N}")
print()

# Visualización conjunta de los histogramas
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Histograma para costo fijo de 700M
axs[0].hist(vpn_copy, bins=30, color='skyblue', edgecolor='black')
axs[0].set_title("Histograma del VPN Simulado (700M)")
axs[0].set_xlabel("VPN")
axs[0].set_ylabel("Frecuencia")

# Limpiar vpn_copy antes de reutilizar
vpn_copy.clear()

# Simulación triangular
resultado_triangular = simular(20000, 1)

# Histograma para costo triangular
axs[1].hist(vpn_copy, bins=30, color='lightcoral', edgecolor='black')
axs[1].set_title("Histograma del VPN Simulado (Triangular)")
axs[1].set_xlabel("VPN")
axs[1].set_ylabel("Frecuencia")

# Ajustar diseño
plt.tight_layout()
plt.show()
