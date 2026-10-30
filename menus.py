from veiculos import (
    cadastrar_veiculo,
    listar_veiculos,
    buscar_veiculo,
    editar_veiculo,
    excluir_veiculo
)

from motoristas import (
    cadastrar_motorista,
    listar_motoristas,
    buscar_motorista,
    editar_motorista,
    excluir_motorista
)

def menu_veiculos():

    escolha_usuario = -1

    while escolha_usuario != 0:
        print('===== VEÍCULOS =====')
        print('[1] - Cadastrar')
        print('[2] - Buscar')
        print('[3] - Listar')
        print('[4] - Editar')
        print('[5] - Excluir')
        print('[0] - Voltar')
        print('=' * len('===== VEÍCULOS ====='))

        escolha_usuario = int(input('Opção: '))

        if escolha_usuario == 1:
            cadastrar_veiculo()
        elif escolha_usuario == 2:
            buscar_veiculo()
        elif escolha_usuario == 3:
            listar_veiculos()
        elif escolha_usuario == 4:
            editar_veiculo()
        elif escolha_usuario == 5:
            excluir_veiculo()
        elif escolha_usuario == 0:
            print('Voltando ao menu principal...')
        else:
            print('Opção inválida. Tente novamente.')

def menu_motoristas():

    escolha_usuario = -1

    while escolha_usuario != 0:
        print('===== MOTORISTAS =====')
        print('[1] - Cadastrar')
        print('[2] - Buscar')
        print('[3] - Listar')
        print('[4] - Editar')
        print('[5] - Excluir')
        print('[0] - Voltar')
        print('=' * len('===== MOTORISTAS ====='))

        escolha_usuario = int(input('Opção: '))

        if escolha_usuario == 1:
            cadastrar_motorista()
        elif escolha_usuario == 2:
            buscar_motorista()
        elif escolha_usuario == 3:
            listar_motoristas()
        elif escolha_usuario == 4:
            editar_motorista()
        elif escolha_usuario == 5:
            excluir_motorista()
        elif escolha_usuario == 0:
            print('Voltando ao menu principal...')
        else:
            print('Opção inválida. Tente novamente.')

def menu_alugueis():
    pass
