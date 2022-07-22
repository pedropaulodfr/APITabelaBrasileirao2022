import requests


from bs4 import BeautifulSoup

def raspagem_rodadas():
    

    URL = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"

    hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/96.0.4664.110 Safari/537.36'}

    
    site = requests.get(URL, headers=hearders)

    soup = BeautifulSoup(site.content, 'html.parser')

    dados = []
    jogos_da_rodada = []

    header = soup.find_all("header", class_="aside-header")


    for i in range(0, len(header)):
        #print(header[i].h3.text)

        rodada = header[i].h3.text

        jogos_container = soup.find_all("div", class_="aside-content")

        
        numero_jogos_por_rodada = 10
        for index in range(0, numero_jogos_por_rodada):

            jogos_info = jogos_container[i].find_all("div", class_="clearfix")[index]
            time_casa = jogos_info.find_all("div", class_="time pull-left")[0].span.text
            time_fora = jogos_info.find_all("div", class_="time pull-right")[0].span.text
            resultado_info = jogos_info.find_all("strong", class_="partida-horario center-block")[0].prettify()
            confronto = time_casa + " x " + time_fora

            print(resultado_info)

            jogos_da_rodada.append([{'Confronto' : confronto}, {'Resultado' : '1 x 1'}])

        dados.append([{rodada: {'Jogos': jogos_da_rodada, 'Resultado': 'B'}}])

    #print(dados)

    return dados