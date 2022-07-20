import requests


from bs4 import BeautifulSoup

def raspagem_rodadas():
    

    URL = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"

    hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/96.0.4664.110 Safari/537.36'}

    
    site = requests.get(URL, headers=hearders)

    soup = BeautifulSoup(site.content, 'html.parser')

    header = soup.find_all("header", class_="aside-header")
    jogos = soup.find_all("div", class_="aside-content")

    dados = []

    i = 0

    print(jogos[i].find_all("div", class_="clearfix")[i].find_all("div", class_="time pull-left")[0].span.text)


    for i in range(0, len(header)):
        #print(header[i].h3.text)

        rodada = header[i].h3.text


        dados.append([{rodada: {'Jogos': 'B'}}])

    #print(dados)

    return header