#importa a conexão com o banco de dados
from config.conexao import get_connection

#lista de colunas padrão nas consultas SELECT
COLUNAS = "id, nome, sigla, pais, regiao, ano_fundacao, ranking"


class Time:
    #busca toda a tabela
    @staticmethod
    def get_all():
        conn = get_connection()
        #retorna os dados como JSON
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT {COLUNAS} FROM times")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    #buscar equipe por id
    @staticmethod
    def get_by_id(time_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        #previne ataques de SQL Injection
        cursor.execute(f"SELECT {COLUNAS} FROM times WHERE id = %s", (time_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    #adiciona um novo time ao banco de dados
    @staticmethod
    def insert(dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO times (nome, sigla, pais, regiao, ano_fundacao, ranking) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (dados.get('nome'), dados.get('sigla'), dados.get('pais'),
                   dados.get('regiao'), dados.get('ano_fundacao'), dados.get('ranking'))
        cursor.execute(sql, valores)
        #commit salva a alteração no banco de dados
        conn.commit()
        last_id = cursor.lastrowid  #cria um ID automático
        cursor.close()
        conn.close()
        return last_id

    #atualizaa informações sobre um time existente no banco de dados
    @staticmethod
    def update(time_id, dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE times SET nome=%s, sigla=%s, pais=%s, regiao=%s, ano_fundacao=%s, ranking=%s WHERE id=%s"
        valores = (dados.get('nome'), dados.get('sigla'), dados.get('pais'),
                   dados.get('regiao'), dados.get('ano_fundacao'), dados.get('ranking'), time_id)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount  #linhas afetadas na alteração
        cursor.close()
        conn.close()
        return rowcount > 0  

    #exclui um time do banco de dados com base no ID
    @staticmethod
    def delete(time_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM times WHERE id = %s", (time_id,))
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount > 0  