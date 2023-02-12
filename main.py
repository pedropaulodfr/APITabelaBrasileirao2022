from flask import Flask, jsonify

from lib.tabela import raspagem_tabela
from lib.rodadas import raspagem_rodadas
from lib.artilharia import raspagem_artilharia



app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "API Tabela Campeonato Brasileiro 2022"})


@app.route("/tabela")
def tabela():


    att = raspagem_tabela()

    time = []

    for i in range(0, len(att)):

        time.append({
            'Posicao': att[i][0],
            'Time': att[i][1],
            'Pontos': att[i][2],
            'Jogos': att[i][3],
            'Vitorias': att[i][4],
            'Empates': att[i][5],
            'Derrotas': att[i][6],
            'Gols-Pro': att[i][7],
            'Gols-Contra': att[i][8],
            'Saldo-Gols': att[i][9],
            'Cartoes-Amarelos': att[i][10],
            'Cartoes-Vermelhos': att[i][11],
            'Aproveitamento': att[i][12],
            'Recentes': att[i][13][i],
            'Proximo-Jogo': att[i][14],
            'Escudo': att[i][15],
            })


    return jsonify(time)



@app.route("/rodadas")
def rodada():
    
    att = raspagem_rodadas()

    return jsonify(att)


@app.route("/artilheiros")
def artilharia():

    att = raspagem_artilharia()

    return jsonify(att)


app.run("0.0.0.0")
