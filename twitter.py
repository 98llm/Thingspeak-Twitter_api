import time
import requests
import random

# url base para api
BASE_URL = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'

# KEY = 'Insira uma string da chave gerada na plataforma'
KEY = ''

# inteiro equivalente a uma hora
hora = 60 * 60

#verifica se um numero é maior que 50
def temp(n):
    if n > 50:
        return True
    else:
        return False

# envia parametro como post na api
def notification(param):
    status = str(param)
    data = {'api_key' : KEY,
            'status' : status}
    response = requests.post(url=BASE_URL, data=data)
    print(response)


while True:
    # gera numero randomico entre 20 e 70
    n = random.randint(20, 70)
    if temp(n):
        print(n)
        notification(n)
        time.sleep(hora)
