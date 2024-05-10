print(((3+2)/(2*5))**2)

horas = float(input("Horas trabajadas"))
precio = float(input("precio por hora"))
salario = horas * precio
print("has trabajado", horas,"horas, a un precio de", precio, "en total tu salario es de", salario,"€")
print(f"tu salario es de {salario}€")
print("tu salario es de %f" %(salario))


nombre, apellido, edad = str(input("escribe tu nombre")), str(input("escribe tu apellido")), int(input("indica tu edad"))

a, b, c, d, e, f, g = nombre

print(f"hola {nombre} {apellido}, tu edad es de {edad}años \n Haora escribire tu nombre de una forma diferente")
print(f"{a} \n {b} \n {c} \n {d} \n {e} \n {f} \n {g} \n")
print(f"{a}{b}{c}{d}{e}{f}{g}")



print(str(nombre.capitalize().count("a")))
print(str(nombre.capitalize()))

