# Definir los parámetros del seguro
valor_asegurado = 20000  # Valor asegurado del vehículo en USD
frecuencia_siniestros = 0.1  # Frecuencia de siniestros por año
severidad_siniestros = 5000  # Costo promedio por siniestro en USD
gastos_administrativos = 200  # Gastos administrativos y comisiones en USD
margen_beneficio = 0.10  # Margen de beneficio (10%)

# 1. Calcular el costo esperado de los siniestros
costo_esperado_siniestros = frecuencia_siniestros * severidad_siniestros

# 2. Calcular el total de costos (siniestros + administrativos)
total_costos = costo_esperado_siniestros + gastos_administrativos

# 3. Calcular la prima total incluyendo el margen de beneficio
prima_total = total_costos * (1 + margen_beneficio)

# Imprimir los resultados
print(f"Frecuencia de siniestros: {frecuencia_siniestros} siniestros/año")
print(f"Severidad del siniestro: ${severidad_siniestros} por siniestro")
print(f"Gastos administrativos: ${gastos_administrativos}")
print(f"Margen de beneficio: {margen_beneficio * 100}%")
print(f"\nCosto esperado de siniestros: ${costo_esperado_siniestros}")
print(f"Total de costos (siniestros + administrativos): ${total_costos}")
print(f"Prima total (con margen de beneficio): ${prima_total}")
