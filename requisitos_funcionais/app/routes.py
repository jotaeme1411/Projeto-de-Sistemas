from flask import request, jsonify
from regras_de_negocio.CRUD.create.cadastro_de_itens import criar_item
from regras_de_negocio.CRUD.read.registro_de_solicitacoes import listar_solicitacoes
from regras_de_negocio.CRUD.read.registro_de_usuarios import listar_doadores
from requisitos_funcionais.app import app, db
from requisitos_funcionais.app.models import *

from regras_de_negocio.CRUD.create.cadastro_de_usuarios import criar_doador
from regras_de_negocio.CRUD.read.registro_de_itens import listar_itens
from regras_de_negocio.CRUD.create.solicitacoes_de_ajuda import criar_solicitacao
from regras_de_negocio.CRUD.read.relatorios_e_estatisticas import *
from regras_de_negocio.CRUD.update.atualizar_status import *

@app.route("/")
def homepage():
    return "Bem-vindo ao projeto Ajuda Solidária"

# RETORNA UMA LISTA DE USUARIOS
@app.route('/listar-usuarios', methods=['GET'])
def get_usuarios():
    try:
        usuarios = listar_doadores()
        resultado = []
        for u in usuarios:
            resultado.append({
                "id": u.id,
                "nome": u.nome,
                "contato": u.contato,
                "endereco": u.endereco
            })
        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# RETORNA UMA LISTA DE SOLICITACOES
@app.route('/listar-solicitacoes', methods=['GET'])
def get_solicitacoes():
    try:
        solicitacoes = listar_solicitacoes()
        resultado = []
        for s in solicitacoes:
            resultado.append({
                "id": s.id,
                "desc_necessidade": s.desc_necessidade,
                "status": s.status.value,
                "id_beneficiario": s.ID_beneficiario
            })
        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
# RETORNA UMA LISTA DE ITENS
@app.route('/listar-itens', methods=['GET'])
def get_itens():
    try:
        itens = listar_itens()
        resultado = []
        for item in itens:
            resultado.append({
                "id": item.id,
                "nome_do_item": item.nome_do_item,
                "status": item.status.value,
                "id_doador": item.ID_doador
            })
        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# REGISTRA NO BANCO DE DADOS UM USUARIO
@app.route('/cadastrar-usuario', methods=['POST'])
def cadastrar_usuario():
    try:
        dados = request.json
        doador = criar_doador(
            nome=dados.get('nome'),
            contato=dados.get('contato'),
            endereco=dados.get('endereco')
        )
        return jsonify({
            "mensagem": "Doador cadastrado com sucesso!",
            "id": doador.id
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
# REGISTRA NO BANCO DE DADOS UM ITEM
@app.route('/cadastrar-item', methods=['POST'])
def cadastrar_item():
    try:
        dados = request.json
        item = criar_item(
            nome_do_item=dados.get('nome_do_item'),
            quantidade=dados.get('quantidade'),
            ID_doador=dados.get('ID_doador')
        )
        return jsonify({
            "mensagem": "Item cadastrado com sucesso!",
            "id": item.id
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# REGISTRA NO BANCO DE DADOS UMA SOLICITACAO
@app.route('/registrar-solicitacao', methods=['POST']) 
def registrar_solicitacao():
    try:
        dados = request.json
        solicitacao = criar_solicitacao(
            desc_necessidade=dados.get('desc_necessidade'),
            id_beneficiario=dados.get('id_beneficiario')
        )
        return jsonify({
            "mensagem": "Solicitação registrada com sucesso!",
            "id": solicitacao.id
        }), 201

    except ValueError as ve:
        return jsonify({"erro": str(ve)}), 400

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# GERA UM RELATORIO LOGISTICO
@app.route('/gerar-relatorio', methods=['GET'])
def gerar_relatorio():
    try:
        return jsonify({
            "doacoes_realizadas": total_doacoes_realizadas(),
            "itens_entregues": lista_itens_entregues(),
            "beneficiarios_atendidos": total_beneficiarios_atendidos(),
            "solicitacoes_atendidas": total_solicitacoes_atendidas()
        }), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
# ATUALIZA O STATUS DO ITEM
@app.route('/itens/<int:item_id>/status', methods=['PUT'])
def atualizar_status_do_item(item_id):
    try:
        dados = request.json
        novo_status = dados.get("status")

        if not novo_status:
            return jsonify({"erro": "Campo 'status' é obrigatório"}), 400

        item = atualizar_status_item(item_id, novo_status)
        return jsonify({
            "mensagem": "Status do item atualizado com sucesso.",
            "id": item.id,
            "novo_status": item.status.value
        }), 200

    except ValueError as ve:
        return jsonify({"erro": str(ve)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ATUALIZA O STATUS DA SOLICITACAO
@app.route('/solicitacoes/<int:solicitacao_id>/status', methods=['PUT'])
def atualizar_status_da_solicitacao(solicitacao_id):
    try:
        dados = request.json
        novo_status = dados.get("status")

        if not novo_status:
            return jsonify({"erro": "Campo 'status' é obrigatório"}), 400

        solicitacao = atualizar_status_solicitacao(solicitacao_id, novo_status)
        return jsonify({
            "mensagem": "Status da solicitação atualizado com sucesso.",
            "id": solicitacao.id,
            "novo_status": solicitacao.status.value
        }), 200

    except ValueError as ve:
        return jsonify({"erro": str(ve)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500