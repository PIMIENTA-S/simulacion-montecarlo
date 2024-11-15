# Diagrama de Flujo para Encontrar el Número Óptimo de Almanaques a Encargar

Este diagrama de flujo ilustra el proceso para determinar el número óptimo de almanaques a encargar, basándose en la simulación de demanda, cálculo de utilidad y ajuste de cantidad para maximizar el beneficio.

## Diagrama de Flujo

![Diagrama de Flujo](A_flowchart_diagram_to_find_the_optimal_number_of_.png)

## Pasos Detallados del Proceso

1. **Inicio**  
   El proceso comienza aquí.

2. **Generación de Demanda Simulada**  
   Se genera la demanda de almanaques vendida mediante una simulación basada en probabilidades establecidas.

3. **Calcular el Precio de Importación**  
   Se genera un precio de importación aleatorio dentro del rango de [1.5, 2.0].

4. **Comparar Demanda con Cantidad a Importar**  
   - **¿Demanda <= Cantidad Importada?**  
     - **Sí**: Se asigna la demanda simulada.
     - **No**: Se ajusta la demanda simulada al valor de la cantidad a importar.

5. **Calcular Utilidad Máxima**  
   La utilidad máxima se calcula considerando las ventas efectivas, el precio y la cantidad no vendida. La utilidad calculada se almacena en una lista.

6. **Calcular Desviación Estándar de las Utilidades**  
   Calcula la desviación estándar de la lista de utilidades simuladas.

7. **Calcular el Número Óptimo de Almanaques (N)**  
   Con la desviación estándar calculada, se obtiene el número óptimo de almanaques a encargar.

8. **Calcular Intervalo de Confianza**  
   Basándose en la media de las utilidades y la desviación estándar, se calcula y muestra el intervalo de confianza.

9. **Fin**  
   El proceso finaliza aquí.

---

Este flujo permite evaluar el mejor número de almanaques a encargar para maximizar las utilidades y minimizar los riesgos de sobrecarga.
