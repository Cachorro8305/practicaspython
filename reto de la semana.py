actual = int(input("Introduce el año actual. "))
anterior = int(input("Introduce otro año para calcular. "))
if actual >= anterior:  
    print("Han pasado desde", actual - anterior," el año que as introducido")
actual = int(input("Introduce el año actual. "))
anterior = int(input("Introduce otro año para calcular. "))    
if actual <= anterior:
    print('Faltan',anterior - actual,'años para llegar al año que as introducido')
actual = int(input("Introduce el año actual. "))
anterior = int(input("Introduce otro año para calcular. "))    
if actual >= anterior:
    print('Desde el año',anterior, 'han pasado',actual - anterior,)
actual = int(input("Introduce el año actual. "))
anterior = int(input("Introduce otro año para calcular. "))    
if actual <= anterior:
    print('Para llegar a',anterior,'hace falta',anterior - actual,'años')
actual = int(input("Introduce el año actual. "))
anterior = int(input("Introduce otro año para calcular. "))    
if actual == anterior:
    print('Has introducido el mismo numero que el actual') 



 # print(f"Has introducido el mismo año que el actual")
