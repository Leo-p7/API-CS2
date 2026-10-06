from flask import jsonify


class TimeView:
    #cria as respostas JSON que a API devolve.

    @staticmethod
    def lista(times):
        return jsonify(times)

    @staticmethod
    def item(time):
        return jsonify(time)


    #mostra uma mensagem de sucesso ou erro em formato JSON
    
    @staticmethod
    def mensagem(texto, status=200, **extras):
        return jsonify({"mensagem": texto, **extras}), status

    @staticmethod
    def erro(texto, status=404):
        return jsonify({"erro": texto, "código": str(status)}), status
