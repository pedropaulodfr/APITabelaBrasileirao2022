import requests


from bs4 import BeautifulSoup

def raspagem_rodadas():
    

    URL = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022"

    hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/96.0.4664.110 Safari/537.36'}

    
    site = requests.get(URL, headers=hearders)

    soup = BeautifulSoup(site.content, 'html.parser')

    rodadas_container = soup.find_all("div", class_="aside-content")

    dados = []
    jogos_da_rodada = []


    for rodada in range(0, 5): # (0, 38)


        rodadas_ul = rodadas_container[rodada].find_all("ul", class_="list-unstyled")
        rodadas_li = rodadas_ul[0].find_all("li")


        for jogo_da_rodada in range(0, len(rodadas_li)):


            rodadas_div = rodadas_li[jogo_da_rodada].find_all("div")
            clearfix = rodadas_div[0].find_all("div", class_="clearfix")
            clearfix_a = clearfix[0].find_all("a", class_="no-underline")

            time_casa_div = clearfix_a[0].find_all("div", class_="time pull-left")
            time_casa_nome = time_casa_div[0].find_all("span", class_="time-sigla")[0].text

            time_fora_div = clearfix_a[0].find_all("div", class_="time pull-right")
            time_fora_nome = time_fora_div[0].find_all("span", class_="time-sigla")[0].text

            confronto = time_casa_nome + " x " + time_fora_nome

            resultado_strong = clearfix_a[0].find_all("strong", class_="partida-horario center-block")


            try:
                resultado = resultado_strong[0].find_all("span")[0].text
            except:
                resultado = "- x -"


            data_partida = rodadas_div[0].find_all("span")[0].text
            data_partida = data_partida.replace("\n", "").replace("\r", "").replace("              ", " ").replace("          ", " ")

            local_partida = rodadas_div[0].find_all("span", class_="partida-desc text-1 color-lightgray block uppercase text-center")[0].text
            local_partida = local_partida.replace("\n", "").replace("\r", "").replace("              ", "").replace("Como foi o jogo", "").replace("Detalhes do jogo", "")


            jogos_da_rodada.append([{'Confronto' : confronto}, {'Resultado' : resultado}, {'Data' : data_partida}, {'Local' : local_partida}])
            '''jogos_da_rodada.append([
                confronto, 
                resultado, 
                data_partida, 
                local_partida
            ])'''

        #dados.append([{"Rodada " + str(rodada + 1): {'Jogos': jogos_da_rodada}}])
        dados.append([
            str(rodada + 1),
            jogos_da_rodada
        ])



    return dados