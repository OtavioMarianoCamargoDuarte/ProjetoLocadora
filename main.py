from veiculos import (
    cadastrar_veiculo,
    listar_veiculos,
    buscar_veiculo,
    editar_veiculo,
    excluir_veiculo
)

escolha_usuario = -1

while escolha_usuario != 0:
    print('===== LOCADORA =====')
    print('[1] - Cadastrar veículo')
    print('[2] - Buscar veículo')
    print('[3] - Listar veículos')
    print('[4] - Editar veículo')
    print('[5] - Excluir veículo')
    print('[0] - Sair')

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
    else:
        print('Opção inválida. Tente novamente.')

print('Programa encerrado.')
    
