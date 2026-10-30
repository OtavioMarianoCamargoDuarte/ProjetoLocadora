motoristas = []

def cadastrar_motorista():
    nome = input('Nome: ')
    data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ')
    cpf = input('CPF: ')
    for item in motoristas:
        if item['cpf'] == cpf:
            print('Motorista já cadastrado.')
            return
    telefone = input('Telefone: ')
    cnh = input('CNH: ')
    status = 'Ativo'

    motorista = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'telefone': telefone,
        'cnh': cnh,
        'status': status
    }

    motoristas.append(motorista)

    print('\nMotorista cadastrado com sucesso!')
    print(f'Nome: {nome}')
    print(f'Data de Nascimento: {data_nascimento}')
    print(f'CPF: {cpf}')
    print(f'Telefone: {telefone}')
    print(f'CNH: {cnh}')
    print(f'Status: {status}')
    print('-------------------')

def listar_motoristas():
    print('===== MOTORISTAS =====')

    if len(motoristas) == 0:
        print('Nenhum motorista cadastrado.')
    else:
        for item in motoristas:
            print(f'Nome: {item["nome"]}')
            print(f'Data de Nascimento: {item["data_nascimento"]}')
            print(f'CPF: {item["cpf"]}')
            print(f'Telefone: {item["telefone"]}')
            print(f'CNH: {item["cnh"]}')
            print(f'Status: {item["status"]}')
            print('-------------------')
            print()

def buscar_motorista():
    cpf_busca = input('Digite o CPF do motorista que deseja buscar: ')

    encontrado = False

    for item in motoristas:
        if item['cpf'] == cpf_busca:
            encontrado = True
            print('Motorista encontrado:')
            print(f'Nome: {item["nome"]}')
            print(f'Data de Nascimento: {item["data_nascimento"]}')
            print(f'CPF: {item["cpf"]}')
            print(f'Telefone: {item["telefone"]}')
            print(f'CNH: {item["cnh"]}')
            print(f'Status: {item["status"]}')
            print('-------------------')

            break

    if not encontrado:
        print('Motorista não encontrado.')

def editar_motorista():
    cpf_editar = input('Digite o CPF do motorista que deseja editar: ')

    encontrado = False

    for item in motoristas:
        if item['cpf'] == cpf_editar:
            encontrado = True
            print('Motorista encontrado:')
            print(f'Nome: {item["nome"]}')
            print(f'Data de Nascimento: {item["data_nascimento"]}')
            print(f'CPF: {item["cpf"]}')
            print(f'Telefone: {item["telefone"]}')
            print(f'CNH: {item["cnh"]}')
            print(f'Status: {item["status"]}')
            print('-------------------')
            print('Opções: ')
            print('[1] - Editar nome')
            print('[2] - Editar data de nascimento')
            print('[3] - Editar telefone')
            print('[4] - Editar CNH')
            print('[5] - Editar status')
            print('[0] - Cancelar')

            escolha_edicao = int(input('Opção: '))

            if escolha_edicao == 1:
                novo_nome = input('Digite o novo nome: ')
                item['nome'] = novo_nome
                print('Motorista atualizado com sucesso!')
                print(f'Nome: {item["nome"]}')
                print(f'Data de Nascimento: {item["data_nascimento"]}')
                print(f'CPF: {item["cpf"]}')
                print(f'Telefone: {item["telefone"]}')
                print(f'CNH: {item["cnh"]}')
                print(f'Status: {item["status"]}')
                print('-------------------')
                break

            elif escolha_edicao == 2:
                nova_data_nascimento = input('Digite a nova data de nascimento (dd/mm/aaaa): ')
                item['data_nascimento'] = nova_data_nascimento
                print('Motorista atualizado com sucesso!')
                print(f'Nome: {item["nome"]}')
                print(f'Data de Nascimento: {item["data_nascimento"]}')
                print(f'CPF: {item["cpf"]}')
                print(f'Telefone: {item["telefone"]}')
                print(f'CNH: {item["cnh"]}')
                print(f'Status: {item["status"]}')
                print('-------------------')
                break

            elif escolha_edicao == 3:
                novo_telefone = input('Digite o novo telefone: ')
                item['telefone'] = novo_telefone
                print('Motorista atualizado com sucesso!')
                print(f'Nome: {item["nome"]}')
                print(f'Data de Nascimento: {item["data_nascimento"]}')
                print(f'CPF: {item["cpf"]}')
                print(f'Telefone: {item["telefone"]}')
                print(f'CNH: {item["cnh"]}')
                print(f'Status: {item["status"]}')
                print('-------------------')
                break

            elif escolha_edicao == 4:
                nova_cnh = input('Digite a nova CNH: ')
                item['cnh'] = nova_cnh
                print('Motorista atualizado com sucesso!')
                print(f'Nome: {item["nome"]}')
                print(f'Data de Nascimento: {item["data_nascimento"]}')
                print(f'CPF: {item["cpf"]}')
                print(f'Telefone: {item["telefone"]}')
                print(f'CNH: {item["cnh"]}')
                print(f'Status: {item["status"]}')
                print('-------------------')
                break

            elif escolha_edicao == 5:
                novo_status = input('Digite o novo status (Ativo/Inadimplente/Bloqueado): ')
                item['status'] = novo_status
                print('Motorista atualizado com sucesso!')
                print(f'Nome: {item["nome"]}')
                print(f'Data de Nascimento: {item["data_nascimento"]}')
                print(f'CPF: {item["cpf"]}')
                print(f'Telefone: {item["telefone"]}')
                print(f'CNH: {item["cnh"]}')
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
        print('Motorista não encontrado.')

def excluir_motorista():
    cpf_excluir = input('Digite o CPF do motorista que deseja excluir: ')

    encontrado = False

    for item in motoristas:
        if item['cpf'] == cpf_excluir:
            encontrado = True
            print('Motorista encontrado:')
            print(f'Nome: {item["nome"]}')
            print(f'Data de Nascimento: {item["data_nascimento"]}')
            print(f'CPF: {item["cpf"]}')
            print(f'Telefone: {item["telefone"]}')
            print(f'CNH: {item["cnh"]}')
            print(f'Status: {item["status"]}')
            print('-------------------')
            print('Deseja realmente excluir este motorista?')
            print('[1] - Sim')
            print('[0] - Não')
            escolha_exclusao = int(input('Opção: '))

            if escolha_exclusao == 1:
                motoristas.remove(item)
                print('Motorista excluído com sucesso!')
                break

            elif escolha_exclusao == 0:
                print('Exclusão cancelada.')
                break
    if not encontrado:
        print('Motorista não encontrado.')
