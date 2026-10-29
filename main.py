from veiculos import cadastrar_veiculo, listar_veiculos, buscar_veiculo

escolha_usuario = -1

while escolha_usuario != 0:
    print('===== LOCADORA =====')
    print('[1] - Cadastrar veículo')
    print('[2] - Buscar veículo')
    print('[3] - Listar veículos')
    print('[0] - Sair')

    escolha_usuario = int(input('Opção: '))

    if escolha_usuario == 1:
        cadastrar_veiculo()
    elif escolha_usuario == 2:
        buscar_veiculo()
    elif escolha_usuario == 3:
        listar_veiculos()

print('Programa encerrado.')
    
