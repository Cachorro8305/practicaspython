#se piden los datos de la persona a revisar el IMC
nombre = input("Diguite su nombre: ")
apellido1 = input("Su apellido paterno:")
apellido2 = input("Su apellido materno: ")
edad = int(input("Diguite su edad: "))
peso = float(input("Diguite su peso: "))
estatura = float(input("Diguite su estatura: " ))
#se agrega la formula para validar el IMC
IMC = peso / estatura**2
# imprimo el IMC de la persona o datos ingresados
print(IMC)
#calculo del IMC segun la documentación del issste y valida en que seccion esta segun su validación
if IMC >= 0 and IMC <= 18.9 :
    print("Peso bajo. ")
elif IMC >= 18.50 and IMC <= 24.99 :
    print("Peso normal. ")
elif IMC >=25.00 and IMC <= 29.99 :
    print("Sobre peso. ")
elif IMC >= 30.00 and IMC <=34.99 :
    print("Obecidad leve. ")
elif IMC >= 35.00 and IMC <= 39.99 :
    print("Obecidad media.")
elif IMC > 40.00 :
    print("Obecidad morbida. ")
