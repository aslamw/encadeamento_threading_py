import time,threading

def carro(velocidade,piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        
        print(f'piloto: {piloto} km: {trajeto}')
        
t_carro1 = threading.Thread(target=carro, args=[1,'Markin'])
t_carro2 = threading.Thread(target=carro, args=[2,'JJ'])

t_carro1.start()
t_carro2.start()
        