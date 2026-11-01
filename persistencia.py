import json
import os

def salvar_dados(dados, arquivo):
    """
    Salva os dados informados em um arquivo JSON.

    Recebe uma estrutura de dados Python, como listas e
    dicionários, e grava seu conteúdo no arquivo especificado.
    Caso o arquivo já exista, seu conteúdo é sobrescrito com
    os dados mais recentes do sistema.
    """
    with open(arquivo, "w") as arquivo_aberto:
        json.dump(dados, arquivo_aberto)

def carregar_dados(arquivo):
    """
    Carrega dados de um arquivo JSON.

    Verifica se o arquivo informado existe e, em caso positivo,
    lê seu conteúdo e o converte para uma estrutura de dados
    Python. Caso o arquivo não exista, retorna uma lista vazia,
    permitindo que o sistema seja iniciado sem erros na primeira
    execução.
    """
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo_carregado:
            return json.load(arquivo_carregado)
    else:
        return[]