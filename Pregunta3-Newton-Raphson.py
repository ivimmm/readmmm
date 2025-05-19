import math
# Función f(x)
def f(x):
    return math.exp(-x) - x
# Derivada de f(x)
def df(x):
    return -math.exp(-x) - 1
# Metodo de Newton-Raphson
def newton_raphson(f, df, x0, iteraciones):
    x = x0
    for i in range(iteraciones):
        x_new = x - f(x) / df(x)
        print(f"Iteración {i+1}: y Aproximacion: {x_new}")
        x = x_new
    return x
# Parámetros iniciales
x0 = 0
iteraciones = 1  # Se Puede cambiar el numero de iteraciones aquí
# Aplicar el metodo de Newton-Raphson
x_final = newton_raphson(f, df, x0, iteraciones)

print(f"De {iteraciones} iteracion de Newton-Raphson con x0 = {x0}, x es aproximadamente: {x_final}")
