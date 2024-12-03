import numpy as np

# Parámetros del modelo
lambda_param = 0.01  # Parámetro de la distribución exponencial (λ = 0.01, pérdidas promedio 1/λ = 100)
limite_retencion = 200  # Límite de retención inicial
costo_reaseguro_porcentaje = 0.05  # 5% del exceso
num_reclamaciones = 10  # Número de reclamaciones a simular

# Simulación de montos de reclamaciones (Exponencial)
montos_reclamaciones = np.random.exponential(1 / lambda_param, num_reclamaciones)

# Calcular el exceso sobre el límite de retención
excesos = np.maximum(montos_reclamaciones - limite_retencion, 0)  # Solo las reclamaciones que exceden el límite

# Calcular el costo del reaseguro (5% del exceso)
costos_reaseguro = excesos * costo_reaseguro_porcentaje  # 5% del monto que excede el límite
costo_total_reaseguro = np.sum(costos_reaseguro)  # Suma total del costo del reaseguro

# Calcular el costo esperado de pérdidas retenidas (Cp)
retenciones = np.minimum(montos_reclamaciones, limite_retencion)  # Reclamaciones dentro del límite
costo_perdidas_retenidas = np.sum(retenciones)  # Suma de todas las pérdidas retenidas

# Calcular el costo total
costo_total = costo_perdidas_retenidas + costo_total_reaseguro

# Mostrar resultados
print(f"Montos de las reclamaciones: {montos_reclamaciones}")
print(f"Excesos sobre el limite de retencion: {excesos}")
print(f"Costos del reaseguro: {costos_reaseguro}")
print(f"Costo total del reaseguro: {costo_total_reaseguro:.2f}")
print(f"Costo esperado de perdidas retenidas (Cp): {costo_perdidas_retenidas:.2f}")
print(f"Costo total: {costo_total:.2f}")