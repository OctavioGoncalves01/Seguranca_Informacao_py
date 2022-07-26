import re, json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP:\n')
print(f'>IP: {ip}\n>Org: {org}\n>Cidade: {cid}\n'+
        f'>País: {pais}\n>Região: {regiao}\n')