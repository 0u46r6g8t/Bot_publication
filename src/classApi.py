#-*- coding: utf-8 -*-

from flask import Flask
import json
from classBot import Bot 

# Criando o app flask
app = Flask(__name__)

# Dados renderizados

## Criando classe para mexer com a api
@app.route('/', methods=['GET'])
def bot_net():'
    return "Programa em desenvolvimento, por favor aguarde até o lançamento!" # Definir ainda o resultado

if __name__ == '__main__':
    app.run(debug=True)