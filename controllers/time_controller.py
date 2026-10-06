from models.time import Time
from views.time_view import TimeView


class TimeController:
    @staticmethod
    def mostrar_tudo():
        return TimeView.lista(Time.get_all())

    @staticmethod
    def mostrar_por_id(time_id):
        time = Time.get_by_id(time_id)
        if time:
            return TimeView.item(time)
        return TimeView.erro("Time não encontrado", 404)

    @staticmethod
    def cadastrar(dados):
        if not dados or not dados.get('nome'):
            return TimeView.erro("Dados inválidos. O campo 'nome' é obrigatório.", 400)
            
        novo_id = Time.insert(dados)
        if novo_id:
            return TimeView.mensagem("Time criado com sucesso", 201, id=novo_id)
        return TimeView.erro("Erro ao cadastrar time", 500)

    @staticmethod
    def atualizar(time_id, dados):
        if not dados:
            return TimeView.erro("Nenhum dado fornecido para atualização", 400)

        if not Time.get_by_id(time_id):
            return TimeView.erro("Time não encontrado", 404)

        if Time.update(time_id, dados):
            return TimeView.mensagem("Time atualizado com sucesso", 200)
        return TimeView.erro("Erro ao atualizar o time", 500)

    @staticmethod
    def excluir(time_id):
        if not Time.get_by_id(time_id):
            return TimeView.erro("Time não encontrado", 404)

        if Time.delete(time_id):
            return TimeView.mensagem("Time excluído com sucesso", 200)
        return TimeView.erro("Erro ao excluir o time", 500)