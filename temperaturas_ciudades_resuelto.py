# Importamos la biblioteca random para generar temperaturas de ejemplo
import random

# Definimos las dimensiones de la matriz
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
dias_semana = 7  # 7 días
semanas = 4      # 4 semanas

# 1. Crear una matriz 3D para almacenar temperaturas
# La estructura será [ciudades][semanas][dias]
matriz_temperaturas = [[[random.uniform(18, 28) for _ in range(dias_semana)] 
                        for _ in range(semanas)] 
                       for _ in range(len(ciudades))]

# 2. Iterar y calcular el promedio
# Usamos bucles anidados para recorrer la matriz y sumar las temperaturas de cada semana
for i, ciudad in enumerate(ciudades):
    print(f"\n--- Promedios de temperatura para {ciudad} ---")
    
    # Bucle para cada semana
    for j in range(semanas):
        # Seleccionamos el conjunto de temperaturas de la semana actual
        temperaturas_semana = matriz_temperaturas[i][j]
        
        # 3. y 4. Calcular el promedio y mostrarlo en la pantalla
        promedio = sum(temperaturas_semana) / len(temperaturas_semana)
        print(f"Semana {j + 1}: {promedio:.2f}°C")
