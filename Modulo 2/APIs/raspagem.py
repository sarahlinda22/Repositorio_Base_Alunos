from bs4 import BeautifulSoup 
import requests 

#url = 'https://www.estadao.com.br/'
#url = 'https://www.folha.uol.com.br/'
#url = 'https://g1.globo.com/'
resposta = requests.get(url)
conteudo_html = resposta.content
soup = BeautifulSoup(conteudo_html, 'html.parser')

links = soup.find_all('h2')
for link in links:
    print("texto:{%s},URL:{%s}"
    % (link.text, link.get('href')))