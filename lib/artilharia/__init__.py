import requests


from bs4 import BeautifulSoup

def raspagem_artilharia():
    

    URL = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"

    hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/96.0.4664.110 Safari/537.36'}

    

    site = requests.get(URL, headers=hearders)

    soup = BeautifulSoup(site.content, 'html.parser')

    tabela_artilharia = soup.find_all("table", class_="table border-body")
    tbody_artilharia = tabela_artilharia[0].find_all("tbody")
    tr_atilharia = tbody_artilharia[0].find_all("tr")

    artilheios = []


    for i in range(0, len(tr_atilharia) - 1):
    
        gols  = tr_atilharia[i].find_all("th")[0].text
        apelido = tr_atilharia[i].find_all("td")[2].text
        td_clube = tr_atilharia[i].find_all("td")
        img_clube = td_clube[0].find_all("img", class_="icon escudo")
        clube = img_clube[0].get("alt")

        artilheios.append([
            i + 1,
            apelido,
            clube,
            gols
        ])



    return artilheios