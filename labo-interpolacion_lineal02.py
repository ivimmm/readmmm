# Ejercicio 2: Finanzas
import matplotlib.pyplot as plt

def interpolacion_lineal(x0, y0, x1, y1, x):
    y = y0 + (y1 - y0) / (x1 - x0) * (x - x0)
    return y

# Datos
dia0 = 5
precio0 = 28.50
dia1 = 15
precio1 = 31.20

# Calcular el precio en el día 10
dia_interp = 10
precio_interp = interpolacion_lineal(dia0, precio0, dia1, precio1, dia_interp)
print(f"Precio en el día 10: El precio interpolado es : ${precio_interp:.2f}")

# Graficar
plt.plot([dia0, dia1], [precio0, precio1], 'bo-', label='Puntos conocidos')
plt.plot(dia_interp, precio_interp, 'ro', label='Precio interpolado')
plt.xlabel('Día')
plt.ylabel('Precio (USD)')
plt.legend()
plt.title('Interpolación Lineal de Precios')
plt.grid(True)
plt.show()

# Calcular el error
precio_real = 29.80
error = abs(precio_interp - precio_real)
print(f"El error entre el precio interpolado y el precio real: ${error:.2f}")
