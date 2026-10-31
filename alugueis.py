from veiculos import veiculos
from motoristas import motoristas

alugueis = []

def criar_aluguel():
    cpf_solicitar = input('CPF: ')
    if len(motoristas) == 0:
        print('Nenhum motorista cadastrado.')
    else:

        encontrado = False

        for motorista in motoristas:
            if motorista['cpf'] == cpf_solicitar:
                encontrado = True
                if motorista['status'] != 'Ativo':
                    print('Motorista indisponível para locação.')
                    print(f'Status: {motorista["status"]}')
                    return
                else:
                    print('Motorista encontrado:')
                    print(f'Nome: {motorista["nome"]}')
                    print(f'Data de Nascimento: {motorista["data_nascimento"]}')
                    print(f'CPF: {motorista["cpf"]}')
                    print(f'Telefone: {motorista["telefone"]}')
                    print(f'CNH: {motorista["cnh"]}')
                    print(f'Status: {motorista["status"]}')
                    print('-------------------')
                    print('Motorista apto para locação.')
                    print()

                    placa_solicitar = input('Placa do veículo: ')

                    encontrado_veiculo = False

                    for veiculo in veiculos:
                        if veiculo['placa'] == placa_solicitar:
                            encontrado_veiculo = True
                            print('Veículo encontrado:')
                            print(f'Modelo: {veiculo["modelo"]}')
                            print(f'Ano: {veiculo["ano"]}')
                            print(f'Placa: {veiculo["placa"]}')
                            if veiculo['status'] != 'Disponível':
                                print('Veículo indisponível para locação.')
                                print(f'Status: {veiculo["status"]}')
                                return
                            else:
                                print('Veículo disponível para locação.')
                                break

                    if not encontrado_veiculo:
                        print('Veículo não encontrado.')
                        return

                    valor_semanal = float(input('Valor semanal: R$'))
                    data_inicio = input('Data de início (dd/mm/aaaa): ')
                    id_aluguel = len(alugueis) + 1

                    aluguel = {
                        'id' : id_aluguel,
                        'cpf_motorista' : cpf_solicitar,
                        'placa_veiculo' : placa_solicitar,
                        'data_inicio' : data_inicio,
                        'valor_semanal' : valor_semanal,
                        'status' : 'Ativo'
                    }

                    alugueis.append(aluguel)

                    veiculo['status'] = 'Alugado'

                    print('Aluguel criado com sucesso!')
                    print(f'ID: {id_aluguel}')
                    print(f'CPF do motorista: {cpf_solicitar}')
                    print(f'Placa do veículo: {placa_solicitar}')
                    print(f'Data de início: {data_inicio}')
                    print(f'Valor semanal: R${valor_semanal:.2f}')

                    break
                    
        if not encontrado:
            print('Motorista não encontrado.')

def listar_alugueis():
    print('===== ALUGUÉIS =====')

    if len(alugueis) == 0:
        print('Nenhum aluguel cadastrado.')
    else:
        for aluguel in alugueis:
            print(f"ID: {aluguel['id']}")
            print(f"CPF: {aluguel['cpf_motorista']}")
            print(f"Placa: {aluguel['placa_veiculo']}")
            print(f"Data de Início: {aluguel['data_inicio']}")
            print(f"Valor semanal: R${aluguel['valor_semanal']:.2f}")
            print(f"Status: {aluguel['status']}")
            print('-------------------')
            print()

def buscar_aluguel():
    id_busca = int(input('ID: '))

    encontrado = False

    for aluguel in alugueis:
        if aluguel['id'] == id_busca:

            encontrado = True

            print('Aluguel encontrado:')
            print(f"ID: {aluguel['id']}")
            print(f"CPF: {aluguel['cpf_motorista']}")
            print(f"Placa: {aluguel['placa_veiculo']}")
            print(f"Data de Início: {aluguel['data_inicio']}")
            print(f"Valor semanal: R${aluguel['valor_semanal']:.2f}")
            print(f"Status: {aluguel['status']}")
            print('-------------------')
            break

    if not encontrado:
        print('Aluguel não encontrado.')

def encerrar_aluguel():
    id_solicitar = int(input('ID: '))

    if len(alugueis) == 0:
        print('Nenhum aluguel realizado.')

    else:

        encontrado = False

        for aluguel in alugueis:
            if aluguel['id'] == id_solicitar:

                encontrado = True

                print('Aluguel encontrado.')
                if aluguel['status'] == 'Encerrado':
                    print('Este aluguel já foi encerrado.')
                    print(f'Status atual: {aluguel["status"]}')
                    return
                print(f'ID: {aluguel["id"]}')
                print(f'CPF do motorista: {aluguel["cpf_motorista"]}')
                print(f'Placa do veículo: {aluguel["placa_veiculo"]}')
                print(f'Data de início: {aluguel["data_inicio"]}')
                print(f'Valor semanal: R${aluguel["valor_semanal"]}')
                print(f'Status: {aluguel["status"]}')
                print('-------------------')

                print('Quer realizar o encerramento do aluguel?')
                print('[1] - SIM')
                print('[2] - NÃO')
                escolha_usuario = int(input('Opção: '))
                if escolha_usuario == 1:
                    aluguel['status'] = 'Encerrado'
                    for veiculo in veiculos:
                        if veiculo['placa'] == aluguel['placa_veiculo']:
                            veiculo['status'] = 'Disponível'
                            break
                    print('Aluguel encerrado com sucesso.')
                    break

                elif escolha_usuario == 2:
                    print('Encerramento cancelado.')
                    break

                else:
                    print('Escolha inválida.')
                    return
                
        if not encontrado:
            print('Aluguel não encontrado.')