pago_casa = -450
pago_movil = -25
pago_multas= -108
pagos_general = pago_casa + pago_movil + pago_multas


while True:
    try:
     ingresos = int(input("cuanto cobraste este mes"))
     break
    except ValueError:
        print("introduce un alor numerico sin signo de euro ")
print("tienes",ingresos + pagos_general)

if ingresos + pagos_general < 1000 :
    print("Balla otro mes que no ahorras")

else:

     print("enorabuena este mes has consegudo ahorrar") 
