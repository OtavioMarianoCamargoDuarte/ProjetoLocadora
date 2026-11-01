"""
Sistema de gerenciamento para uma locadora de veículos.

Permite o gerenciamento de veículos, motoristas,
aluguéis e relatórios, com persistência de dados
em arquivos JSON.
"""

from menus import (
    menu_veiculos,
    menu_motoristas,
    menu_alugueis,
    menu_relatorios
)

escolha_usuario = -1

while escolha_usuario != 0:
    print('===== LOCADORA =====')
    print('[1] - Veículos')
    print('[2] - Motoristas')
    print('[3] - Aluguéis')
    print('[4] - Relatórios')
    print('[0] - Sair')
    print('=' * len('===== LOCADORA ====='))

    escolha_usuario = int(input('Opção: '))

    if escolha_usuario == 1:
        menu_veiculos()
    elif escolha_usuario == 2:
        menu_motoristas()
    elif escolha_usuario == 3:
        menu_alugueis()
    elif escolha_usuario == 4:
        menu_relatorios()
    elif escolha_usuario == 0:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')

print('Programa encerrado.')
