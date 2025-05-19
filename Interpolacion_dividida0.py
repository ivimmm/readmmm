import numpy as np
def diferencias_divididas(x_points, y_points):
    n = len(x_points)
    coef = np.zeros([n, n])
    coef[:, 0] = y_points
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x_points[i + j] - x_points[i])
    return coef[0, :]
# Ejemplo de uso
x_points = [1, 2, 4]
y_points = [2, 3, 5]
coefs = diferencias_divididas(x_points, y_points)
print("Coeficientes del polinomio:", coefs)