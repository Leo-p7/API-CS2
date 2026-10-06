
from flask import Flask, request
from flask_cors import CORS 
from flasgger import Swagger, swag_from

#importa o Controller com as regras
from controllers.time_controller import TimeController

#importa os dicionários do Swagger
from config.swagger import (
    get_all_spec,
    get_by_id_spec,
    insert_spec,
    update_spec,
    delete_spec
)

app = Flask(__name__)

#permite que aplicações front-end sem bloqueios
CORS(app)

#coloca palavras com acento sem converter para códigos no JSON
app.json.ensure_ascii = False

#interface onde o Swagger vai abrir
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda rule: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/times/swagger"  #URL de acesso
}

#inicializa o flasgger com as configurações customizadas
swagger = Swagger(app, config=swagger_config)


#caminho GET para listar todos os times
@app.route('/times', methods=['GET'])
@swag_from(get_all_spec)  # Conecta a documentação Swagger
def listar_todos():
    return TimeController.mostrar_tudo()


#caminho GET para buscar um time pelo ID na URL
@app.route('/times/<int:time_id>', methods=['GET'])
@swag_from(get_by_id_spec)
def listar_por_id(time_id):
    return TimeController.mostrar_por_id(time_id)


#caminho POST para cadastrar um novo time
@app.route('/times', methods=['POST'])
@swag_from(insert_spec)
def criar():
    dados = request.json  #deixa em formato JSON
    return TimeController.cadastrar(dados)


#caminho PUT para atualizar um time que existe pelo ID
@app.route('/times/<int:time_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar(time_id):
    dados = request.json
    return TimeController.atualizar(time_id, dados)


#caminho DELETE para excluír um time pelo ID
@app.route('/times/<int:time_id>', methods=['DELETE'])
@swag_from(delete_spec)
def deletar(time_id):
    return TimeController.excluir(time_id)


#executa o servidor Flask localmente em modo de desenvolvimento (debug=True)
if __name__ == '__main__':
    app.run(debug=True)