import time

hora = time.ctime()
_hora = time.localtime()
print("Hora actual:",time.strftime("%H:%M:%S",_hora))
x = list(_hora)
restante = 19 - x[3]
if restante <= 0:
    print("Es hora de ir a casa")
else:
    print("Quedan por trabajar: ",restante,"horas")