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

from menus import (
    menu_veiculos,
    menu_motoristas,
    menu_alugueis
)

escolha_usuario = -1

while escolha_usuario != 0:
    print('===== LOCADORA =====')
    print('[1] - Veículos')
    print('[2] - Motoristas')
    print('[3] - Aluguéis')
    print('[0] - Sair')
    print('=' * len('===== LOCADORA ====='))

    escolha_usuario = int(input('Opção: '))

    if escolha_usuario == 1:
        menu_veiculos()
    elif escolha_usuario == 2:
        menu_motoristas()
    elif escolha_usuario == 3:
        menu_alugueis()
    elif escolha_usuario == 0:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')

print('Programa encerrado.')
