a = int(input("Introduce el año actual. "))
b = int(input("Introduce otro año para calcular. "))
if a > b:  
    print("Han pasado", a - b,"desde el año que as introducido")

elif a < b:
    print('Faltan',a - b,'años para llegar al año que as introducido')

c = int(input("Introduce el año actual. "))
d = int(input("Introduce otro año para calcular. "))    
    
if c > d:
    print('Desde el año',d, 'han pasado',c - d,)
     
elif c > d:
    print('Para llegar a',d,'hace falta',d - c,'años')
   
elif c == d:
    print('Has introducido el mismo numero que el actual') 