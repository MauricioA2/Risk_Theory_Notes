# Definir los parámetros básicos
ingresos = 1000000  # Ingresos totales de la empresa
gastos_fijos = 300000  # Gastos fijos anuales
gastos_variables = 200000  # Gastos variables anuales
tasa_impuesto = 0.30  # Tasa de impuesto sobre la renta (30%)
porcentaje_dividendos = 0.40  # Porcentaje de las ganancias a distribuir como dividendos

# Cálculo de beneficios antes de impuestos
beneficios_antes_impuestos = ingresos - (gastos_fijos + gastos_variables)

# Cálculo de impuestos
impuestos = beneficios_antes_impuestos * tasa_impuesto

# Beneficio neto después de impuestos
beneficio_neto = beneficios_antes_impuestos - impuestos

# Cálculo de los dividendos
dividendos = beneficio_neto * porcentaje_dividendos

# Resultados
print(f"Beneficios antes de impuestos: ${beneficios_antes_impuestos:.2f}")
print(f"Impuestos a pagar: ${impuestos:.2f}")
print(f"Beneficio neto después de impuestos: ${beneficio_neto:.2f}")
print(f"Dividendos a distribuir: ${dividendos:.2f}")