print('su palabra debera de tener un minimo de 4 letras y un maximo de 8 ')
N = input('Ingrese su palabra ')
if len (N) >= 4 and len (N) <= 8 :
    print('la palabra es correcta')
elif len (N) < 4 :
    print(f'Hacen falta letras, solo tiene {len(N)} siendo 4 el minimo de la palabra')
elif len (N) > 8 :
    print(f'Sobran letras, tiene {len(N)} siendo 8 el maximo de la palabra')
    
else :
    print('su palabra debera de tener un minimo de 4 letras y un maximo de 8 ')
