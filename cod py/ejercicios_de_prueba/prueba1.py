#pide en pantalla nombre y apellido clear
nombre = input( "Cual es tu nombre: " )
apellido = input("Cual es tu apellido: ")
año= 2024
#creo un bucle, si se cumple el requisito avanza si no se cumple repite 
while True:
    try:
        #creo la variable edad y le digo que es un entero y pido al usuario que indique el entero si se cumple que es entero sigue 
        edad = int(input("cuantos años cumples este año : "))
        break  # Sale del bucle si se proporciona una entrada válida
    except ValueError:
        #excepcion : si hay un error que imprima un texto y vuelva al principio del bucle 
        print("Por favor, ingresa un número válido para la edad.")

  # Verifica si la edad es menor de 18
if edad < 18:
    #si edad es menor de 18 cambia el valor de la variable redad
    redad = "este año eres menor de edad porque tu edad es de"
else:
  #siel contenido de edad no cumple la condicion en este caso edad es > 18 cambia el valor de la variable redad 
    redad = "no aparentas la edad de"



#imprime el resultado final de las variables + string
print("Hola %s %s %s %d años" %(nombre, apellido, redad, edad))
print("naciste en el año", año - edad)
letras_n = len(nombre)
letras_a = len(apellido)

print ("tu nombre tiene", len(nombre), "letras")
print ("y tu apellido tiene", len(apellido), "letras\n")
print ("en total tu nombre y apellido tienen",letras_a + letras_n, "letras\n\n")

print(len("hola")+0)