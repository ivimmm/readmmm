def interpolacion_lineal (x0 , y0 , x1 , y1 , x):
# Interpola el valor de y en x usando los puntos (x0 ,y0) y (x1 ,y1). "
    return y0 + ( y1 - y0 ) * ( x - x0 ) / ( x1 - x0 )
 # Ejemplo :
x0 , y0 = 2, 4
x1 , y1 = 3, 9
x_interp = 2.5
y_interp = interpolacion_lineal (x0 , y0 , x1 , y1 , x_interp )
print (f" Valor interpolado en x= { x_interp } : { y_interp }")