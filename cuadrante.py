x = int(input('Ingrese cordenada de X '))# pedimos datos a usuario
y = int(input('Ingrese cordenada de Y '))

#se calcula cuadrante mediante la condicion and
if x > 0 and y > 0 :
    print('Punto en el primer cuadrante')
elif x < 0 and y > 0 :
    print('Punto en el segundo cuadrante')
elif x < 0 and y < 0 :
    print('Punto en el tercer cuadrante')
elif x > 0 and y < 0 :
    print('Punto en el cuarto cuadrante')
else :
    print('Punto de Origen')
