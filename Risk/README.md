
# Simulador de Combate de Risk

## Descripción
El juego de mesa **Risk** tiene como objetivo dominar el mundo mediante la conquista de territorios. Los jugadores pueden atacar territorios adyacentes con su ejército, mientras el jugador defensor intenta proteger sus posiciones. Este simulador permite calcular la probabilidad de éxito de un ataque basado en las reglas de combate de Risk.

## Reglas del Combate

Durante un combate en Risk:
- El **atacante** puede lanzar hasta **3 dados**.
- El **defensor** puede lanzar hasta **2 dados**.
- Los resultados de los dados de ambos jugadores se ordenan de **mayor a menor**.
- Los valores de cada dado del atacante se comparan con los valores correspondientes de los dados del defensor en orden:
  - Si el dado del defensor es **mayor o igual** al del atacante, el **atacante pierde un soldado**.
  - Si el dado del atacante es mayor, el **defensor pierde un soldado**.

### Ejemplo de Combate
Imaginemos que el atacante lanza tres dados y el defensor lanza dos. Los resultados son los siguientes:

| Atacante (dados) | Defensor (dados) | Resultado  | Soldado Perdido |
|------------------|------------------|------------|-----------------|
| 5                | 6                | Defensor   | Atacante        |
| 3                | 4                | Defensor   | Atacante        |
| 1                | No se compara    | -          | -               |

En este caso, el atacante perdería **dos soldados**.

## Ejercicio de Probabilidad

Si el atacante cuenta con 4 soldados y el defensor con 3, este programa permite calcular la **probabilidad de que el atacante gane el combate** bajo estas condiciones iniciales.

---

## Instalación

Para ejecutar este simulador, asegúrate de tener Python instalado y sigue estos pasos:

```bash
# Clona este repositorio
git clone https://github.com/PIMIENTA-S/simulacion-montecarlo.git

# Entra al directorio del proyecto
cd simulacion-montecarlo

# Instala los requerimientos
pip install -r requirements.txt
