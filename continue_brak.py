# uso de la sentencia continue con el ciclo for
#for numero in range (1, 11 ):
#    if numero % 2 == 1 :
#        continue
#    print(f'{numero} es un numero par ')

# uso de la sentencia continue con el ciclo while

#numero = 0
#while numero < 11 :
#    numero += 1 
#    if numero % 2 == 0 :
#        continue
#>    print(f'{numero} es un numero impar')

######################################################

# uso de la sentencia break
#numero = int(input('Ingrese un digito: '))
#limite_inferior = 0
#limite_superior = 10
#buscado = 5
#intentos = 0

#while True:
#    intentos += 1
#    if numero == buscado :
#        print(f'El numero {numero} fue encontrado en {intentos} intentos ')
#        break
#    elif numero < buscado :
#        limite_superior = buscado
#        buscado = (buscado + limite_inferior) // 2
#    else:
#        limite_inferior = buscado
#        buscado = (buscado + limite_superior) // 2   
#print('FIN DEL PROGRAMA')
########################################################################################

# uso de la funcion exit

numero = int(input('Ingrese un digito: '))
limite_inferior = 0
limite_superior = 10
buscado = 5
intentos = 0

while True:
    intentos += 1
    if numero == buscado :
        print(f'El numero {numero} fue encontrado en {intentos} intentos ')
        exit()
    elif numero < buscado :
        limite_superior = buscado
        buscado = (buscado + limite_inferior) // 2
    else:
        limite_inferior = buscado
        buscado = (buscado + limite_superior) // 2   
print('FIN DEL PROGRAMA')
print('IMPRECIÓN DESPUES DEL USO DE LA FUNCIÓN BREAK')
print('IMPRECIÓN DESPUES DEL USO DE LA FUNCIÓN EXIT()')