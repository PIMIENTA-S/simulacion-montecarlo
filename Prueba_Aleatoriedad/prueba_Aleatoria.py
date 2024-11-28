import pandas as pd

archivo = '/content/drive/MyDrive/Simulacion/loteriaBOG.csv'

df = pd.read_csv(archivo, header=None)

df = df.rename(columns={0: 'Datos'})

impar = []
par = []
for i in df['Datos']:
  if i % 2 != 0:
    impar.append(i)
  else:
    par.append(i)

print(f'Numero Impar: {len(impar)}, Numero par: {len(par)}')
