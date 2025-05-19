def interpolacion_cuadratica (x0 , y0 , x1 , y1 , x2 , y2 , x):
    """
    Interpolacion cuadratica usando el metodo de Lagrange .

    Parametros:
        x0 , y0 , x1 , y1 , x2 , y2: Tres puntos de datos .
        x: Punto a interpolar .

    Retorna :
        Valor interpolado y = P(x).
    """
    term0 = y0 * (( x - x1 ) * ( x - x2 ) ) / (( x0 - x1 ) * ( x0 - x2 ) )
    term1 = y1 * (( x - x0 ) * ( x - x2 ) ) / (( x1 - x0 ) * ( x1 - x2 ) )
    term2 = y2 * (( x - x0 ) * ( x - x1 ) ) / (( x2 - x0 ) * ( x2 - x1 ) )
    return term0 + term1 + term2

# Ejemplo de uso
x0 , y0 = 1, 2
x1 , y1 = 3, 4
x2 , y2 = 5, 3
x_interpolar = 2

resultado = interpolacion_cuadratica (x0 , y0 , x1 , y1 , x2 , y2 ,x_interpolar )
print (f"El valor interpolado en x= { x_interpolar } es y= { resultado :.4f}")