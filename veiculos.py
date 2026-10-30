veiculos = []

def cadastrar_veiculo():

    placa = input('Digite a placa: ')

    for item in veiculos:
        if item['placa'] == placa:
            print('Veículo já cadastrado.')
            return
    modelo = input('Digite o modelo: ')
    ano = int(input('Digite o ano: '))

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

def editar_veiculo():

    placa_editar = input('Digite a placa do veículo que deseja editar: ')

    encontrado = False

    for item in veiculos:
        if item['placa'] == placa_editar:
            encontrado = True
            print('Veículo encontrado:')
            print(f'Placa: {item["placa"]}')
            print(f'Modelo: {item["modelo"]}')
            print(f'Ano: {item["ano"]}')
            print('-------------------')
            print('Opções:')
            print('[1] - Editar modelo')
            print('[2] - Editar ano')
            print('[0] - Cancelar')

            escolha_edicao = int(input('Opção: '))

            if escolha_edicao == 1:
                novo_modelo = input('Digite o novo modelo: ')
                item['modelo'] = novo_modelo
                print('Veículo atualizado com sucesso!')
                print(f'Placa: {item["placa"]}')
                print(f'Modelo: {item["modelo"]}')
                print(f'Ano: {item["ano"]}')
                print('-------------------')
                break

            elif escolha_edicao == 2:
                novo_ano = int(input('Digite o novo ano: '))
                item['ano'] = novo_ano
                print('Veículo atualizado com sucesso!')
                print(f'Placa: {item["placa"]}')
                print(f'Modelo: {item["modelo"]}')
                print(f'Ano: {item["ano"]}')
                print('-------------------')
                break

            elif escolha_edicao == 0:
                print('Edição cancelada.')
                break

            else:
                print('Opção inválida. Tente novamente.')
                break

    if not encontrado:
        print('Veículo não encontrado.')     

def excluir_veiculo():
    placa_excluir = input('Digite a placa do veículo que deseja excluir: ')

    encontrado = False

    for item in veiculos:
        if item['placa'] == placa_excluir:
            encontrado = True
            print('Veículo encontrado:')
            print(f'Placa: {item["placa"]}')
            print(f'Modelo: {item["modelo"]}')
            print(f'Ano: {item["ano"]}')
            print('-------------------')
            print('Deseja realmente excluir este veículo?')
            print('[1] - Sim')
            print('[0] - Não')
            escolha_exclusao = int(input('Opção: '))

            if escolha_exclusao == 1:
                veiculos.remove(item)
                print('Veículo excluído com sucesso!')
                break

            elif escolha_exclusao == 0:
                print('Exclusão cancelada.')
                break

    if not encontrado:
        print('Veículo não encontrado.')
