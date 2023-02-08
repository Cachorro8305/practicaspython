entrada = input("Hola introduce tu edad: ")

edad = 0

if entrada.isnumeric() :
    edad = int(entrada)
else :
  print("Dato incorrecto. Debes introducir un numero")
  exit()

if edad <= 0 :
    print("Woooowww!! que joven eres. Pero lo siento eso no es posible ")
elif edad > 115 :
    print("VAYA !!! ¿Como le ases para vivir tanto? No te creo mejor intenta de nuevo")
elif edad < 18 :
    print("Eres menor de edad asi que no puedes comprar tus cigarros")
else :
    print("Eres mayor de edad. Aqui tienes tus cigarros ")    

