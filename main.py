import requests

from bs4 import BeautifulSoup

from flask import Flask, jsonify




def raspagem_de_dados():


    soup = BeautifulSoup()

    URL = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"

    hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.110 Safari/537.36'}

    dados = []

    site = requests.get(URL, headers=hearders)
    soup = BeautifulSoup(site.content, 'html.parser')
    tabela = soup.find_all('tr', class_='expand-trigger')


    for i in range(0, 20):
        linha = tabela[i].td

        nome = linha.find('span', class_='hidden-xs').text
        posicao = linha.b.text
        pontos = tabela[i].th.text

        dados.append([posicao, nome, pontos])

    return dados



app = Flask(__name__)


@app.route("/tabela")
def tabela():


    att = raspagem_de_dados()

    time = []

    for i in range(0, len(att)):
        time.append({'Time': att[i][1], 'Posicao': att[i][0], 'Pontos': att[i][2]})

    return jsonify(time)


app.run()
