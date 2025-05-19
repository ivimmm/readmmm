import math

# Función f(x) para la secante
def f(x):
    return math.log(x) + x

# Función g(x) para el punto fijo
def g(x):
    return -math.log(x)

# Metodo del punto fijo
def punto_fijo(g, x0, iteraciones):
    x = x0
    for i in range(iteraciones):
        x_new = g(x)
        print(f"Punto Fijo - Iteración {i+1}: x = {x_new}")
        x = x_new
    return x

# Metodo de la secante
def secante(f, x0, x1, iteraciones):
    for i in range(iteraciones):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("División por cero en la fórmula de la secante.")
            break
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        print(f"Secante - Iteración {i+1}: x = {x_new}")
        x0 = x1
        x1 = x_new
    return x_new

# Parámetros iniciales
x0_punto_fijo = 0.5  #La elección de 0.5 fue arbitraria y podría cambiarse a 0.1 si se desea.
x0_secante = 0.1
x1_secante = 0.5
iteraciones = 1

# Ejecutar el metodo del punto fijo
print("Método del Punto Fijo:")
solucion_punto_fijo = punto_fijo(g, x0_punto_fijo, iteraciones)
print(f"Solución en {iteraciones} iteración (Punto Fijo): {solucion_punto_fijo}\n")

# Ejecutar el metodo de la secante
print("Método de la Secante:")
solucion_secante = secante(f, x0_secante, x1_secante, iteraciones)
print(f"Solución en {iteraciones} iteración (Secante): {solucion_secante}")
