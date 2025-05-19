# Método de Diferencias Divididas de Newton para interpolación

def diferencias_divididas(x, y):
    n = len(x)
    coef = [yi for yi in y]  # Copiar los valores iniciales de y
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def evaluar_polinomio(coef, x_data, t):
    n = len(coef)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (t - x_data[i]) + coef[i]
    return result
#Ejercicio 3
# Datos del problema
x = [2, 4, 6]      # Tiempo (s)
y = [5, 17, 37]    # Velocidad (km/s)

# Calcular los coeficientes de diferencias divididas
coeficientes = diferencias_divididas(x, y)

# Estimar la velocidad en t = 5
t_estimado = 5
velocidad_estimada = evaluar_polinomio(coeficientes, x, t_estimado)

# Imprimir resultados
print("Coeficientes de diferencias divididas:", coeficientes)
print(f"Velocidad estimada en t = {t_estimado} s: {velocidad_estimada} km/s")


#Ejercicio 4: Costo de Energ ́ıa Solar
# Datos del problema
x = [1, 3, 5]      #Capacidad (MW)(x)
y = [10, 25, 55]    # Costo ($M) (y)

# Calcular los coeficientes de diferencias divididas
coeficientes = diferencias_divididas(x, y)

# Estimar la velocidad en t = 5
t_estimado = 4
velocidad_estimada = evaluar_polinomio(coeficientes, x, t_estimado)

# Imprimir resultados
print("Coeficientes de diferencias divididas:", coeficientes)
print(f"Costo para  = {t_estimado} MW es: {velocidad_estimada} ")