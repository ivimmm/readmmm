# Ejercicio 1: Termodinámica
def interpolacion_lineal(x0, y0, x1, y1, x):
    y = y0 + (y1 - y0) / (x1 - x0) * (x - x0)
    return y

# Datos
T0 = 20
mu0 = 0.0157
T1 = 50
mu1 = 0.0083

# Calcular la viscosidad a 35°C
T_interp = 35
mu_interp = interpolacion_lineal(T0, mu0, T1, mu1, T_interp)
print(f"Viscosidad a 35°C: La viscosidad interpolada es : {mu_interp:.4f} Pa·s")

# Calcular la temperatura para mu = 0.0100 Pa·s
mu_target = 0.0100
T_target = interpolacion_lineal(mu0, T0, mu1, T1, mu_target)
print(f"Temperatura para μ = 0.0100 Pa·s: La temperatura interpolada es : {T_target:.4f} °C")
