import numpy as np
import matplotlib.pyplot as plt

def interpolacion_cuadratica (x0 , y0 , x1 , y1 , x2 , y2 , x):

# Implemente aqui la formula de Lagrange
    term0 = y0 * ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    term1 = y1 * ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    term2 = y2 * ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    return term0 + term1 + term2

# Datos del problema 1
x0 , y0 = 1, 2
x1 , y1 = 3, 1
x2 , y2 = 4, 3

# Generar puntos para graficar
x_vals = np . linspace (0 , 5, 100)
y_vals = [ interpolacion_cuadratica (x0 , y0 , x1 , y1 , x2 , y2 , x) for x in x_vals ]

# Graficar
plt . figure ( figsize =(8 , 6) )
plt . scatter ([ x0 , x1 , x2 ], [y0 , y1 , y2 ], color ='red', label = 'Puntos dados')
plt . plot ( x_vals , y_vals , label ='Polinomio interpolante', linestyle ='--')
plt . xlabel ('x')
plt . ylabel ('y')
plt . legend ()
plt . grid ()
plt . title ('Interpolación Cuadrática')
plt . show ()