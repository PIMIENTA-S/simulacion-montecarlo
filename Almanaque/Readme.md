# Simulación para Decisión Óptima de Almanaques a Encargar

Este proyecto utiliza simulación para ayudar a una librería a determinar el número óptimo de almanaques que debería encargar a su proveedor, con base en costos, ingresos por ventas y posibles reembolsos por devoluciones. La simulación evalúa diferentes cantidades de almanaques encargados (100, 150, 200, 250 y 300) para identificar la decisión más rentable.

## Contexto del Problema

La librería tiene la siguiente información:

- **Costo por almanaque**: Entre $1.50 y $2.00 (generado aleatoriamente usando el método de la transformada inversa).
- **Precio de venta**: $4.50 por almanaque.
- **Reembolso por almanaques no vendidos**: $0.75 por unidad.
- **Distribución de la demanda**:
    
  | Almanaques vendidos | Probabilidad |
  |---------------------|--------------|
  | 100                 | 0.3          |
  | 150                 | 0.2          |
  | 200                 | 0.3          |
  | 250                 | 0.15         |
  | 300                 | 0.05         |

El objetivo es determinar cuántos almanaques debería encargar la librería para maximizar sus ganancias, considerando las restricciones anteriores.

## Implementación del Proyecto

El código realiza simulaciones para cada cantidad de almanaques encargados (100, 150, 200, 250 y 300) y calcula:

1. **Desviación estándar** en una muestra de 10,000 simulaciones para estimar la variabilidad.
2. **Número óptimo de simulaciones necesarias** para un nivel de confianza del 95%.
3. **Estadísticas clave**:
   - Media de ganancias.
   - Desviación estándar de las ganancias.
   - Ganancia mínima y máxima observadas.
   - Intervalo de confianza del 95% para la media.

### Archivos Principales

- **`main.py`**: Contiene todo el código del proyecto, incluyendo la simulación y el cálculo de estadísticas.
- **`README.md`**: Este archivo, que explica el proyecto.

## Ejecución del Código

### Requisitos

- Python 3.8 o superior.
- Librerías necesarias: `math`, `random`, `numpy`.