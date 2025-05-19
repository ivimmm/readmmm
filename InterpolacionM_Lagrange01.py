#Codigo BASE
#función lagrange(x, puntos)
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

#Ejercicio 1: Temperatura en Reactor Químico
'''
Hora (x) | Temperatura (°C) (y)
 1       |    68
 3       |    72
 5       |    80

Tareas:
1. Encontrar el polinomio interpolante de Lagrange manualmente.
2. Implementar en Python la función lagrange(x, puntos).
3. Estimar la temperatura a las 4:00 (usar el código).
'''

# Puntos dados
puntos = [(1, 68), (3, 72), (5, 80)]

# Estimar la temperatura a las 4:00
x = 4
temperatura_4 = lagrange(x, puntos)
print("Temperatura a las 4:00: es=", temperatura_4)
#----------------------------------------------------------------------------------
#Ejercicio 2: Producción de Cultivos
'''
Producción de trigo (ton) vs agua aplicada (cm):
Agua (cm) (x) Producción (ton) (y)
    10           5
    20           7
    30           6

Tareas:
1. Generalizar el código para n puntos usando bucles.
    -El código de la función lagrange ya está generalizado para n puntos.
2. Calcular la producción con 25 cm de agua.
'''
# Puntos dados
puntosE2 = [(10, 5), (20, 7), (30, 6)]

# Calcular la producción con 25 cm de agua
x = 25
produccion_25 = lagrange(x, puntosE2)
print("Producción con 25 cm de agua:", produccion_25)
