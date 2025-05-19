def jacobi(iter_max, tol):
    x0, y0 = 0, 0
    print("Método de Jacobi:")
    for i in range(1, iter_max + 1):
        x1 = (7 + y0) / 4
        y1 = (9 - x0) / 5
        error = max(abs(x1 - x0), abs(y1 - y0))
        print(f"Iteración {i}: x = {x1:.6f}, y = {y1:.6f}")
        if error < tol:
            break
        x0, y0 = x1, y1

def gauss_seidel(iter_max, tol):
    x, y = 0, 0
    print("\nMétodo de Gauss-Seidel:")
    for i in range(1, iter_max + 1):
        x_new = (7 + y) / 4
        y_new = (9 - x_new) / 5
        error = max(abs(x_new - x), abs(y_new - y))
        print(f"Iteración {i}: x = {x_new:.6f}, y = {y_new:.6f}")
        if error < tol:
            break
        x, y = x_new, y_new
#Pregunta4-Jacobi-y-GaussSeidel
# Parámetros
iteraciones = 2
tolerancia = 1e-2

jacobi(iteraciones, tolerancia)
gauss_seidel(iteraciones, tolerancia)
