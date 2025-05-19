def f(x):
    func=x**3 - x - 2
    return func

def biseccion(f, a, b, iteraciones):
    errores = []
    for i in range(iteraciones):
        c = (a + b) / 2
        error_relativo = abs((c - a) / c) if c != 0 else float('inf')
        errores.append(error_relativo)
        if f(c) == 0:
            print(f"Raíz encontrada: {c}")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        #print(f"Iteración {i+1}: a = {a}, b = {b}, c = {c}, Error Relativo = {error_relativo}")
        print(f"Iteración {i + 1}: [ {a} , {b} ] con el Error Relativo = {error_relativo}")
    return c, errores
# Parámetros iniciales [1,2] iteraciones=3
a = 1
b = 2
iteraciones = 3

# Ejecutar el metodo de bisección
raiz, errores = biseccion(f, a, b, iteraciones)

print(f"Raíz aproximada después de {iteraciones} iteraciones: {raiz}")

