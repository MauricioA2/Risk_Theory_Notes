import numpy as np

# Semilla para reproducibilidad
np.random.seed(42)

# Parámetros del modelo
promedio_reclamaciones = 3  # Número medio de reclamaciones por mes (frecuencia)
media_severidad = 5000      # Monto medio de cada reclamación (severidad)

# Simulación del número de reclamaciones (distribución de Poisson)
num_reclamaciones = np.random.poisson(promedio_reclamaciones)

# Simulación de montos de reclamaciones (distribución Exponencial)
montos_reclamaciones = np.random.exponential(media_severidad, num_reclamaciones)

# Cálculo del total de pagos
total_pagos = np.sum(montos_reclamaciones)

# Resultados
print(f"Numero de reclamaciones en el mes: {num_reclamaciones}")
print(f"Montos de cada reclamacion: {montos_reclamaciones}")
print(f"Total de pagos en el mes: {total_pagos:,.2f}")

