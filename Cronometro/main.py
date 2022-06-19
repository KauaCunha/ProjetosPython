import time, sys

minutos = 0
horas = 0

while True:

    for segundos in range(0, 60):
        sys.stdout.write("\r{} : {} : {} ".format(horas,minutos,segundos))
        sys.stdout.flush()
        time.sleep(1)

        if segundos == 59:
            minutos += 1
            segundos = 0
            if minutos == 60:
                horas += 1
                minutos = 0
                segundos = 0
                
            