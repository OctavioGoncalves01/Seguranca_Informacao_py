from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 15:
        trajeto += velocidade
        time.sleep(0.25)
        print(f'Poloto: {piloto}, KM: {trajeto}')



t_carro01 = Thread(target= carro, args=[1, 'Octavio'])
t_carro02 = Thread(target= carro, args=[2, "Black"])

t_carro01.start()
t_carro02.start()