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

from alugueis import (
    criar_aluguel,
    listar_alugueis,
    buscar_aluguel,
    encerrar_aluguel
)

from relatorios import (
    relatorio_veiculos_disponiveis,
    relatorio_veiculos_alugados,
    relatorio_motoristas_ativos,
    relatorio_motoristas_inadimplentes,
    relatorio_motoristas_bloqueados,
    relatorio_alugueis_ativos,
    relatorio_alugueis_encerrados
)

def menu_veiculos():
    """
    Exibe o menu de gerenciamento de veículos da locadora.

    Permite ao usuário acessar as operações de cadastro,
    busca, listagem, edição e exclusão de veículos. O menu
    permanece em execução até que o usuário escolha retornar
    ao menu principal.
    """
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
    """
    Exibe o menu de gerenciamento de motoristas da locadora.

    Permite ao usuário acessar as operações de cadastro,
    busca, listagem, edição e exclusão de motoristas. O menu
    permanece em execução até que o usuário escolha retornar
    ao menu principal.
    """
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
    """
    Exibe o menu de gerenciamento de aluguéis da locadora.

    Permite ao usuário acessar as operações de criação,
    busca, listagem e encerramento de aluguéis. O menu
    permanece em execução até que o usuário escolha retornar
    ao menu principal.
    """

    escolha_usuario = -1

    while escolha_usuario != 0:
        print('===== ALUGUEIS =====')
        print('[1] - Criar aluguel')
        print('[2] - Buscar aluguel')
        print('[3] - Listar alugueis')
        print('[4] - Encerrar aluguel')
        print('[0] - Voltar')
        print('=' * len('===== ALUGUEIS ====='))

        escolha_usuario = int(input('Opção: '))

        if escolha_usuario == 1:
            criar_aluguel()
        elif escolha_usuario == 2:
            buscar_aluguel()
        elif escolha_usuario == 3:
            listar_alugueis()
        elif escolha_usuario == 4:
            encerrar_aluguel()
        elif escolha_usuario == 0:
            print('Voltando ao menu principal...')
        else:
            print('Opção inválida. Tente novamente.')

def menu_relatorios():
    """
    Exibe o menu de relatórios da locadora.

    Permite ao usuário acessar relatórios de veículos,
    motoristas e aluguéis, apresentando informações
    organizadas sobre a situação atual da locadora.
    O menu permanece em execução até que o usuário
    escolha retornar ao menu principal.
    """
    escolha_usuario = -1

    while escolha_usuario != 0:
        print('===== RELATÓRIOS =====')
        print('[1] - Veículos disponíveis')
        print('[2] - Veículos alugados')
        print()
        print('[3] - Motoristas ativos')
        print('[4] - Motoristas inadimplentes')
        print('[5] - Motoristas bloqueados')
        print()
        print('[6] - Aluguéis ativos')
        print('[7] - Aluguéis encerrados')
        print()
        print('[0] - Voltar')
        print('=' * len('===== RELATÓRIOS ====='))

        escolha_usuario = int(input('Opção: '))

        if escolha_usuario == 1:
            relatorio_veiculos_disponiveis()
        elif escolha_usuario == 2:
            relatorio_veiculos_alugados()
        elif escolha_usuario == 3:
            relatorio_motoristas_ativos()
        elif escolha_usuario == 4:
            relatorio_motoristas_inadimplentes()
        elif escolha_usuario == 5:
            relatorio_motoristas_bloqueados()
        elif escolha_usuario == 6:
            relatorio_alugueis_ativos()
        elif escolha_usuario == 7:
            relatorio_alugueis_encerrados()
        elif escolha_usuario == 0:
            print('Voltando ao menu principal...')
        else:
            print('Opção inválida. Tente novamente.')
