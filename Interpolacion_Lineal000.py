def interpolar_lineal (x0 , y0 , x1 , y1 , x):
    '''
    Interpola el valor y correspondiente a x usando los puntos (x0 ,y0) y (x1 ,y1).
    Parametros :
    x0 , y0: Coordenadas del primer punto conocido
    x1 , y1: Coordenadas del segundo punto conocido
    x: Valor donde se desea interpolar
    Retorna :
    Valor y interpolado
    '''
# Validacion de datos de entrada
    if x0 == x1:
        raise ValueError ("Los valores x0 y x1 no pueden ser iguales ( division por cero )")
# Calculo de la pendiente (m)
    pendiente = ( y1 - y0 ) / ( x1 - x0 )
# Aplicacion de la formula de interpolacion
    y = y0 + pendiente * (x - x0 )
    return y

# Puntos conocidos
punto1 = (2 , 4) # (x0 , y0)
punto2 = (5 , 10) # (x1 , y1)

# Valor a interpolar
x_interpolar = 3.5

# Llamada a la funcion
y_interpolado = interpolar_lineal (* punto1 , * punto2 , x_interpolar )

print (f" Para x = { x_interpolar }, y { y_interpolado :.2f}")