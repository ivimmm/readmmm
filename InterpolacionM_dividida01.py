#Codigo BASE
#2. función diferencias_divididas (puntos)
def diferencias_divididas(puntos):
    n = len(puntos)
    tabla = [ [0]*n for _ in range(n) ]
    for i in range(n):
        tabla[i][0] = puntos[i][1]
    for j in range(1, n):
        for i in range(n - j):
            tabla[i][j] = (tabla[i + 1][j - 1] - tabla[i][j - 1])/ (puntos[i + j][0] - puntos[i][0])

    return tabla[0]  # Coeficientes

#lagrange(x, puntos)
def lagrange(x, puntos):
    resultado = 0.0
    n = len(puntos)
    for i in range(n):
        xi, yi = puntos[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, yj = puntos[j]
                term *= (x - xj) / (xi - xj)
        resultado += term
    return resultado
#lagrange(x, puntos)


#2. Ejercicios de Diferencias Divididas
#Ejercicio 3: Velocidad de un Cohete
'''
Datos de velocidad (km/s) vs tiempo (s):

Tiempo (s) (x) Velocidad (km/s) (y)
      2             5
      4            17
      6            37

Tareas:
1. Construir la tabla de diferencias divididas manualmente.
2. Programar la función diferencias divididas(puntos).
    -El código de la función diferencias_divididas (puntos) ya esta (codigo base) 
3. Estimar la velocidad en t = 5 s.
'''
# Puntos dados
puntos = [(2, 5), (4, 17), (6, 37)]

# Obtener los coeficientes
coeficientes = diferencias_divididas(puntos)
print("Coeficientes del polinomio:", coeficientes)

#3 Estimar la velocidad en t=5 s
# Estimar la velocidad en t = 5 s
x = 5
velocidad_5 = lagrange(x, puntos)
print("Velocidad en t = 5 s:", velocidad_5)



#Ejercicio 4: Costo de Energía Solar
'''
Capacidad (MW)(x)  Costo ($M)(y)
        1            10
        3            25
        5            55
Tareas:
1. Encontrar el polinomio interpolante y evaluar para 4 MW.
2. Optimizar el codigo para reutilizar la tabla de diferencias.
'''
# Puntos dados
puntos = [(1, 10), (3, 25), (5, 55)]

# Obtener los coeficientes
coeficientes = diferencias_divididas(puntos)
print("Coeficientes del polinomioAAA:", coeficientes)

# Evaluar para 4 MW
x = 4
costo_4 = lagrange(x, puntos)
print("Costo para 4 MW:", costo_4)
