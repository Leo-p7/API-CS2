#campos e tipos de dados do time
_campos = {
    "nome": {"type": "string"},
    "sigla": {"type": "string"},
    "pais": {"type": "string"},
    "regiao": {"type": "string"},
    "ano_fundacao": {"type": "integer"},
    "ranking": {"type": "integer"}
}

#ID orbigatório recebido na URL
_id_param = {
    "name": "time_id",
    "in": "path",
    "type": "integer",
    "required": True,
    "description": "ID do time"
}

#requisição(JSON)
_body_param = {
    "name": "body",
    "in": "body",
    "required": True,
    "schema": {"type": "object", "properties": _campos}
}

#mostrar todos os times
get_all_spec = {
    "responses": {
        "200": {
            "description": "Lista de times retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"id": {"type": "integer"}, **_campos}
                }
            }
        }
    }
}

#buscar um time por ID 
get_by_id_spec = {
    "parameters": [_id_param],
    "responses": {
        "200": {"description": "Time encontrado com sucesso"},
        "404": {"description": "Time não encontrado"}
    }
}

#cadastrar novo time
insert_spec = {
    "parameters": [_body_param],
    "responses": {"201": {"description": "Time cadastrado com sucesso"}}
}

#atualizar um time existente
update_spec = {
    "parameters": [_id_param, _body_param],
    "responses": {
        "200": {"description": "Time atualizado com sucesso"},
        "404": {"description": "Time não encontrado"}
    }
}

#deletar um time por ID
delete_spec = {
    "parameters": [_id_param],
    "responses": {
        "200": {"description": "Time excluído com sucesso"},
        "404": {"description": "Time não encontrado"}
    }
}