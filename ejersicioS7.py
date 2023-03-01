# crea una lista que capture el nombre y dos calificaciones de asta 5 alumnos en un ciclo donde se cumpla 
# cierta condicion especifica

#lista = [] # lista vacia

#alumnos = 0
#while alumnos <= 5 :

#    opción = input('Agregar alumno (1) o terminar (2): ')
#    if opción == '1' : # el uno etre comillas por que es una cadena la opcion
#        nombre = input('Ingrese el nombre del alumno: ').capitalize() # capitalize se utiliza para q muestre
                                                                      #mayuscula cuando la ingrese minuscula        
#        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
#        calificacion2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
#        alumno = [nombre, calificacion1, calificacion2]
#        lista.append(alumno) # el append se utiliza para guardar lo nesesario en esa lista 
#        alumnos += 1
#    elif opción == '2' :
#        print(f'El programa ha terminado {alumnos} alumnos. ')
#        break # termina el programa
#    else :
#        print('Se a ingresado una opcion no valida')
#        continue

#print('La lista de alumnos es: ')
#print(lista)    
#############################################################################

lista = [] # lista vacia

alumnos = 0
while alumnos <= 11 :

    opción = input('Agregar alumno (1) o terminar (2): ')
    if opción == '1' : # el uno etre comillas por que es una cadena la opcion
        nombre = input('Ingrese el nombre del alumno: ').capitalize() # capitalize se utiliza para q muestre
                                                                      #mayuscula cuando la ingrese minuscula        
        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
        calificacion3 = int(input(f'Ingrese la tercera calificacion de {nombre}: '))
        calificacion4 = int(input(f'Ingrese la cuarta calificacion de {nombre}: '))
        calificacion5 = int(input(f'Ingrese la quinta calificacion de {nombre}: '))
        alumno = [nombre, calificacion1, calificacion2, calificacion3, calificacion4, calificacion5]
        lista.append(alumno) # el append se utiliza para guardar lo nesesario en esa lista 
        alumnos += 1
    elif opción == '2' :
        print(f'El programa ha terminado {alumnos} alumnos. ')
        break # termina el programa
    else :
        print('Se a ingresado una opcion no valida')
        continue

print('La lista de alumnos es: ')
print(lista)    