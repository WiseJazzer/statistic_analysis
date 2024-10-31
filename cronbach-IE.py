import pandas as pd
import numpy as np

# Cargar los datos
file_path = 'resultados-para-analisis.csv'
data = pd.read_csv(file_path)

# Seleccionar las columnas relevantes
items = data[['Puntuación global', 'Bienestar', 'Autocontrol', 'Emocionalidad', 'Sociabilidad']]

# Calcular el alfa de Cronbach
def cronbach_alpha(df):
    n_items = df.shape[1]
    item_variances = df.var(axis=0, ddof=1).sum()
    total_variance = df.sum(axis=1).var(ddof=1)
    alpha = (n_items / (n_items - 1)) * (1 - item_variances / total_variance)
    return alpha

alpha = cronbach_alpha(items)
print(f'Alfa de Cronbach: {alpha}')
