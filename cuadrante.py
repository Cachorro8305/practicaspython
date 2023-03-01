x = int(input('Ingrese cordenada de X '))
y = int(input('Ingrese cordenada de Y '))

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
