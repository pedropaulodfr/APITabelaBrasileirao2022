import requests


from bs4 import BeautifulSoup


def raspagem_tabela():


    URL = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022"

    hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/96.0.4664.110 Safari/537.36'}

    dados = []
    recentes = []

    site = requests.get(URL, headers=hearders)
    soup = BeautifulSoup(site.content, 'html.parser')
    tabela = soup.find_all('tr', class_='expand-trigger')


    for i in range(0, 20):

        linha = tabela[i].td

        nome = linha.find('span', class_='hidden-xs').text
        posicao = linha.b.text
        pontos = tabela[i].th.text
        jogos = tabela[i].find_all("td")[1].text
        vitorias = tabela[i].find_all("td")[2].text
        empates = tabela[i].find_all("td")[3].text
        derrotas = tabela[i].find_all("td")[4].text
        gols_pro = tabela[i].find_all("td")[5].text
        gols_conta = tabela[i].find_all("td")[6].text
        saldo_gols = tabela[i].find_all("td")[7].text
        cartoes_amarelos = tabela[i].find_all("td")[8].text
        cartoes_vermelhos = tabela[i].find_all("td")[9].text
        aproveitamento = tabela[i].find_all("td")[10].text
        recentes.append([
            tabela[i].find_all("td")[11].find_all("span")[0].text, 
            tabela[i].find_all("td")[11].find_all("span")[1].text, 
            tabela[i].find_all("td")[11].find_all("span")[2].text
            ])
        escudo = tabela[i].find_all("img", class_="icon escudo m-r-10")[0].get("src")
        try:
            proximo_jogo = tabela[i].find_all("img", class_="icon escudo")[0].get("title")
        except:
            proximo_jogo = ""

        dados.append([
            posicao,
            nome,
            pontos,
            jogos, 
            vitorias, 
            empates, 
            derrotas, 
            gols_pro, 
            gols_conta, 
            saldo_gols, 
            cartoes_amarelos, 
            cartoes_vermelhos, 
            aproveitamento, 
            recentes, 
            proximo_jogo,
            escudo
            ])

    return dados