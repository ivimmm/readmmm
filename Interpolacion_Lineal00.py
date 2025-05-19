# Funcion de interpolacion lineal
def interpolacion_lineal ( x0 , y0 , x1 , y1 , x ) :
# Calcular la pendiente
    pendiente = ( y1 - y0 ) / ( x1 - x0 )
# Usar la formula de interpolacion
    y = y0 + pendiente * ( x - x0 )
    return y
# Ejemplo de uso
x0 , y0 = 1 , 2 # Punto ( x0 , y0 )
x1 , y1 = 3 , 3 # Punto ( x1 , y1 )
x = 2 # Valor de x para interpolar
resultado = interpolacion_lineal ( x0 , y0 , x1 , y1 , x )
print ( f" El valor interpolado es: { resultado } ")