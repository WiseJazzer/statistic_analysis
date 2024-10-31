import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Cargar los datos
file_path = '/Users/jorgeolayo/Documents/VS-Code/analisis_IE/resultados-para-analisis.csv'
data = pd.read_csv('resultados-para-analisis.csv')

# Crear el boxplot para representar la relación entre Puntaje global de IE y Situación laboral
plt.figure(figsize=(8, 6))
sns.boxplot(x='Situación laboral', y='Sociabilidad', data=data)

# Personalizar el gráfico
plt.title('Boxplot de Sociabilidad y la situación laboral')
plt.xlabel('Situación laboral (0: No trabaja, 1: Trabaja)')
plt.ylabel('Sociabilidad')

# Mostrar el gráfico
plt.show()
