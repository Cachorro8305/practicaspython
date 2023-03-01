# le comentamos al usuario cuantas letras devera tener su palabra
print('su palabra debera de tener un minimo de 4 letras y un maximo de 8 ')
N = input('Ingrese su palabra ') # le pedimos al usuario su palabra
if len (N) >= 4 and len (N) <= 8 : #le desimos a N que si es mayor o igual a 4 y menor o igual a 8 y len cuenta cuantos caracteres tiene la palabra
    print('la palabra es correcta') # imprime el mensaje
elif len (N) < 4 : # nos dise que si len conto menos de 4 letras en la variable(N)
    print(f'Hacen falta letras, solo tiene {len(N)} siendo 4 el minimo de la palabra')#imprime el mensaje y el numero de letras que tiene la palabra
elif len (N) > 8 :# nos dise que si len conto mas de 8 letras en la variable(N)
    print(f'Sobran letras, tiene {len(N)} siendo 8 el maximo de la palabra')#imprime el mensaje y el numero de letras que tiene la palabra
    
else : # si no cumple ninguna de las condisiones 
    print('su palabra debera de tener un minimo de 4 letras y un maximo de 8 ')# imprime este mensaje
