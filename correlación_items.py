import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos
file_path = 'resultados-para-analisis.csv'
data = pd.read_csv(file_path)

# Seleccionar las columnas relevantes
items = data[['Puntuación global', 'Bienestar', 'Autocontrol', 'Emocionalidad', 'Sociabilidad']]

# Calcular la matriz de correlación
corr_matrix = items.corr()

# Visualizar la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación de Ítems')
plt.show()
