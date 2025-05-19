import numpy as np
def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points) # N ́umero de puntos
    P = 0 # Polinomio de interpolaci ́on
    # Itera sobre cada punto
    for i in range(n):
        # Calcula el t ́ermino de Lagrange L_i(x) para cada i
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x - x_points[j]) / (x_points[i] - x_points[j])
        # Suma el tèrmino al polinomio con el valor correspondiente de y_points[i]
        P += y_points[i] * Li
    return P


x_points = [1, 2, 3]
y_points = [2, 3, 5]
x = 2.5
result = lagrange_interpolation(x_points, y_points, x)
print("El valor del polinomio en x = 2.5 es:", result)
#print(f"El valor del polinomio en x ={x} es:: {result:.6f}")
print(f"El valor del polinomio en x ={x} es:: {result}")