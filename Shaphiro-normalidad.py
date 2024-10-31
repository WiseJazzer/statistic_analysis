from scipy import stats
import pandas as pd

# Cargar los datos
file_path = '/Users/jorgeolayo/Documents/VS-Code/analisis_IE/resultados-para-analisis.csv'
data = pd.read_csv(file_path)

# Seleccionar las columnas relevantes
items = data[['Puntuación global', 'Bienestar', 'Autocontrol', 'Emocionalidad', 'Sociabilidad']]

# Realizar la prueba de Shapiro-Wilk para cada ítem
shapiro_results = {}
for column in items.columns:
    stat, p_value = stats.shapiro(items[column])
    shapiro_results[column] = {"W-Statistic": stat, "p-value": p_value}

# Mostrar los resultados
shapiro_df = pd.DataFrame(shapiro_results).T
print(shapiro_df)
