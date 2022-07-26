from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
#obj site recebendo o conteudo do site

sopa = BeautifulSoup(site, 'html.parser')
#obj sopa baixando o site o HTML

print(sopa.prettify())
#transforma html e o print vai exibir o html

#temperatura = sopa.find("span", class_="_block _margin-b-5 -gray")
#print(temperatura.string)