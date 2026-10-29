veiculos = []

def cadastrar_veiculo():

    placa = input('Digite a placa: ')

    for item in veiculos:
        if item['placa'] == placa:
            print('Veículo já cadastrado.')
            return
    modelo = input('Digite o modelo: ')
    ano = int(input('Digite o ano: '))

    print('\nVeículo cadastrado')
    print(f'Placa: {placa}')
    print(f'Modelo: {modelo}')
    print(f'Ano: {ano}')

    veiculo = {
        'placa': placa,
        'modelo': modelo,
        'ano': ano
    }

    veiculos.append(veiculo)

    print('\nVeículo cadastrado com sucesso!')
    print(f'Placa: {placa}')
    print(f'Modelo: {modelo}')
    print(f'Ano: {ano}')
    print(f'Total de veículos cadastrados: {len(veiculos)}')

def listar_veiculos():
    print('===== VEÍCULOS =====')

    if len(veiculos) == 0:
        print('Nenhum veículo cadastrado.')
    else:
        for item in veiculos:
            print(f"Placa: {item['placa']}")
            print(f"Modelo: {item['modelo']}")
            print(f"Ano: {item['ano']}")
            print('-------------------')

def buscar_veiculo():
    placa_busca = input('Digite a placa do veículo que deseja buscar: ')

    encontrado = False

    for item in veiculos:
        if item['placa'] == placa_busca:
            encontrado = True
            print('Veículo encontrado:')
            print(f"Placa: {item['placa']}")
            print(f"Modelo: {item['modelo']}")
            print(f"Ano: {item['ano']}")
            print('-------------------')

            break

    if not encontrado:
        print('Veículo não encontrado.')

