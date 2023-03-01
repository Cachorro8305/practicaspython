from operator import xor
import tkinter

#-----------------------Ventana-----------------------------------------
ventana = tkinter.Tk()
ventana.title('Test TB')
ventana.geometry('500x500')

#---------------------Etiqueta------------------------------------------
cabezera = tkinter.Label(ventana, text = '            Pedido de tacos         '). pack()

#-------------------Botones---------------------------------------------

def salir():
    ventana.destroy()


boton = tkinter.Button(ventana , text = '1', command = 1, fg = 'blue')
boton.pack()
boton.place(x = 380, y = 380, height = 100,width = 100)

boton2 = tkinter.Button(ventana, text = '2', command = 2, fg = 'blue')
boton2.pack()
boton2.place(x = 280, y = 380, height = 100,width = 100)

boton3 = tkinter.Button(ventana, text = '3', command = 3, fg = 'blue')
boton3.pack()
boton3.place(x = 180, y = 380, height = 100,width = 100)

boton4 = tkinter.Button(ventana, text = '4', command = 4, fg = 'blue')
boton4.pack()
boton4.place(x = 80, y = 380, height = 100,width = 100)

boton5 = tkinter.Button(ventana, text = '5', command = 5, fg = 'blue')
boton5.pack()
boton5.place(x = 380, y = 280, height = 100,width = 100)

boton6 = tkinter.Button(ventana, text = '6', command = 6, fg = 'blue')
boton6.pack()
boton6.place(x = 280, y = 280, height = 100,width = 100)

boton7 = tkinter.Button(ventana, text = '7', command = 7, fg = 'blue')
boton7.pack()
boton7.place(x = 180, y = 280, height = 100,width = 100)

boton8 = tkinter.Button(ventana, text = '8', command = 8, fg = 'blue')
boton8.pack()
boton8.place(x = 80, y = 280, height = 100,width = 100)

boton9 = tkinter.Button(ventana, text = '9', command = 9, fg = 'blue')
boton9.pack()
boton9.place(x = 380, y = 180, height = 100,width = 100)

boton0 = tkinter.Button(ventana, text = '0', command = 0, fg = 'blue')
boton0.pack()
boton0.place(x = 280, y = 180, height = 100,width = 100)

boton10 = tkinter.Button(ventana, text = 'X', command = xor, fg = 'red')
boton10.pack()
boton10.place(x = 10, y = 380, height = 100,width = 60)







ventana.mainloop()


#num1 = int(input('enter num1: '))
#num2 = int(input('enter num2: '))
#action = str(input('choose action: add(a), sub(s), mult(m), div(d) ->'))

#print('the result is', end ='')
#if action == 'a':
  #  print(num1 + num2)
#elif action == 's':
#    print(num1 - num2)
#elif action == 'm':
 #   print(num1 * num2)
#else:
 #   print(num1 / num2)  