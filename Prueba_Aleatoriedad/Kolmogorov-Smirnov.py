import matplotlib.pyplot as plt
import numpy as np

# Datos del eje x e y
x = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
y = [0.03511875, 0.116855014, 0.172365059, 0.216388249, 0.233306103, 0.251069834, 0.254510373, 0.325343459, 
     0.409268512, 0.443394229, 0.451620119, 0.459412295, 0.619970667, 0.643638071, 0.655169592, 0.668354483, 
     0.720147965, 0.738267605, 0.788723548, 0.856315562]

# Crear los valores teóricos de la distribución uniforme
x_uniform = np.linspace(0, 1, 100)  # Más puntos para suavidad
y_uniform = x_uniform  # F(x) = x para uniforme [0, 1]

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Datos observados (escalonados)
plt.step(x, y, where='post', color='b', label='Datos observados')

# Función acumulada teórica (uniforme)
plt.plot(x_uniform, y_uniform, color='r', linestyle='--', label='Función acumulada teórica (Uniforme)')

# Añadir etiquetas y título
plt.title('Datos Observados vs. Función Acumulada Teórica (Uniforme)')
plt.xlabel('Rf')
plt.ylabel('Probabilidad acumulada')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
