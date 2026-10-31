import json
import os

def salvar_dados(dados, arquivo):
    with open(arquivo, "w") as arquivo_aberto:
        json.dump(dados, arquivo_aberto)

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo_carregado:
            return json.load(arquivo_carregado)
    else:
        return[]