veiculos = []

def cadastrar_veiculo():
    """
    Realiza o cadastro de um novo veículo na locadora.

    Solicita a placa, modelo e ano do veículo, verificando
    se a placa já está cadastrada no sistema. Caso a placa
    seja única, cria o registro do veículo e o adiciona à
    lista de veículos.

    Novos veículos são cadastrados automaticamente com o
    status "Disponível", ficando aptos para futuras locações.
    """
    placa = input('Digite a placa: ')

    for item in veiculos:
        if item['placa'] == placa:
            print('Veículo já cadastrado.')
            return
    modelo = input('Digite o modelo: ')
    ano = int(input('Digite o ano: '))
    status = "Disponível"

    veiculo = {
        'placa': placa,
        'modelo': modelo,
        'ano': ano,
        'status': status
    }

    veiculos.append(veiculo)

    print('\nVeículo cadastrado com sucesso!')
    print(f'Placa: {placa}')
    print(f'Modelo: {modelo}')
    print(f'Ano: {ano}')
    print(f'Status: {status}')
    print(f'Total de veículos cadastrados: {len(veiculos)}')

def listar_veiculos():
    """
    Exibe todos os veículos cadastrados na locadora.

    Lista as informações de cada veículo, incluindo placa,
    modelo, ano e status atual. Caso não existam veículos
    cadastrados, informa a situação ao usuário.
    """
    print('===== VEÍCULOS =====')

    if len(veiculos) == 0:
        print('Nenhum veículo cadastrado.')
    else:
        for item in veiculos:
            print(f"Placa: {item['placa']}")
            print(f"Modelo: {item['modelo']}")
            print(f"Ano: {item['ano']}")
            print(f"Status: {item['status']}")
            print('-------------------')
            print()

def buscar_veiculo():
    """
    Busca um veículo pela placa informada pelo usuário.

    Exibe os dados do veículo caso ele seja encontrado,
    incluindo modelo, ano e status atual. Caso a placa
    não esteja cadastrada, informa que o veículo não foi
    encontrado.
    """
    placa_busca = input('Digite a placa do veículo que deseja buscar: ')

    encontrado = False

    for item in veiculos:
        if item['placa'] == placa_busca:
            encontrado = True
            print('Veículo encontrado:')
            print(f"Placa: {item['placa']}")
            print(f"Modelo: {item['modelo']}")
            print(f"Ano: {item['ano']}")
            print(f"Status: {item['status']}")
            print('-------------------')

            break

    if not encontrado:
        print('Veículo não encontrado.')

def editar_veiculo():
    """
    Permite alterar os dados de um veículo cadastrado.

    Localiza o veículo pela placa informada pelo usuário e
    disponibiliza opções para atualização do modelo, ano
    ou status. Após a alteração, exibe os dados atualizados
    do veículo.

    Caso a placa não esteja cadastrada, informa que o
    veículo não foi encontrado.
    """
    placa_editar = input('Digite a placa do veículo que deseja editar: ')

    encontrado = False

    for item in veiculos:
        if item['placa'] == placa_editar:
            encontrado = True
            print('Veículo encontrado:')
            print(f'Placa: {item["placa"]}')
            print(f'Modelo: {item["modelo"]}')
            print(f'Ano: {item["ano"]}')
            print(f'Status: {item["status"]}')
            print('-------------------')
            print('Opções:')
            print('[1] - Editar modelo')
            print('[2] - Editar ano')
            print('[3] - Editar status')
            print('[0] - Cancelar')

            escolha_edicao = int(input('Opção: '))

            if escolha_edicao == 1:
                novo_modelo = input('Digite o novo modelo: ')
                item['modelo'] = novo_modelo
                print('Veículo atualizado com sucesso!')
                print(f'Placa: {item["placa"]}')
                print(f'Modelo: {item["modelo"]}')
                print(f'Ano: {item["ano"]}')
                print(f'Status: {item["status"]}')
                print('-------------------')
                break

            elif escolha_edicao == 2:
                novo_ano = int(input('Digite o novo ano: '))
                item['ano'] = novo_ano
                print('Veículo atualizado com sucesso!')
                print(f'Placa: {item["placa"]}')
                print(f'Modelo: {item["modelo"]}')
                print(f'Ano: {item["ano"]}')
                print(f'Status: {item["status"]}')
                print('-------------------')
                break

            elif escolha_edicao == 3:
                novo_status = input('Digite o novo status (disponível, em manutenção, alugado): ')
                item['status'] = novo_status
                print('Veículo atualizado com sucesso!')
                print(f'Placa: {item["placa"]}')
                print(f'Modelo: {item["modelo"]}')
                print(f'Ano: {item["ano"]}')
                print(f'Status: {item["status"]}')
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
    """
    Remove um veículo cadastrado do sistema.

    Localiza o veículo pela placa informada pelo usuário,
    exibe seus dados e solicita confirmação antes da exclusão.
    Caso a remoção seja confirmada, o veículo é removido da
    lista de veículos da locadora.

    Caso a placa informada não esteja cadastrada, informa
    que o veículo não foi encontrado.
    """
    placa_excluir = input('Digite a placa do veículo que deseja excluir: ')

    encontrado = False

    for item in veiculos:
        if item['placa'] == placa_excluir:
            encontrado = True
            print('Veículo encontrado:')
            print(f'Placa: {item["placa"]}')
            print(f'Modelo: {item["modelo"]}')
            print(f'Ano: {item["ano"]}')
            print(f'Status: {item["status"]}')  
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
