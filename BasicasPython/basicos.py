#primera practica
uno = input('ELIGE UNA OPCION: \n a)Suma de dos numeros \n \
b)tipos de variables y operadores aritmeticos \n c)Concatenación\n \
d)importar modulos \n e)funcion propia (Saludar)\nf)funcion propia(Adios)')
if uno == "a":
    print("SUMA DE DOS NUMEROS FLOTANTES")
    num1 = float(input('Coloca el primer numero'))
    num2 = float(input('Coloca el segundo numero'))
    suma = num1 + num2
    print ("el resultado de la suma es de: ", round(suma,2))
elif uno == "b" :
    print("OPERADORES ARITMETICOS")
    print(4+6)
    print(4-6)
    print(3*4)
    print(5/2)
    print(5+8-(5*(2+1)))
    #tipos de datos 
    print("TIPOS DE DATOS")
    print(type(uno))
    print(type(1))
    print(type(4.3))
    mensaje="mensaje"
    print(mensaje)
    mensaje ="mensaje modificado"
    print("Mensaje")
    print(type(mensaje))
    mensaje = 10
    print(mensaje)
    print(type(mensaje))
elif uno=="c":
    print("CONCATENACION DE VARIABLES")
        #separar en otra opcion
    textouno = "hola"
    textoDos ="buenos dias"
    print(textouno + textoDos)
    edad = 20
    print("la edad del usuario es: ", edad)
    print("la edad es: " + str(edad))
    print("el tipo de datos es: " + str(type(edad)))
    print("el tipo de datos es: ", (type(edad)))
    #importarmodulo
    #modulo: set de herramientas que trae python 
elif uno== "d":
    import math
    grados = 45.0
    radianes = grados * math.pi/ 180.0
    seno = math.sin(radianes)
    #para optimizarlos que sean flotantes 
    print("es resultado de seno de 45 grados es: ", radianes)
    #print("es resultado de seno de 45 grados es: " str(radianes))
elif uno == "e":
    def saludar(nombre):
        print("Hola\n¿Como estas?" + nombre)
     
    saludar(nombre = input("cual es tu nombre"))
elif uno == "f":
      #from tkinter import *
    def despedida():
        print("adios")
    despedida()
    def concatenar(parte1, parte2):
        return parte1 + parte2
    frase = concatenar("hola ", "adios")
    print(frase)
else:
    print("debes elegir una opcion")


