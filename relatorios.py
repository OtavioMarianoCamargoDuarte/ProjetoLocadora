import veiculos
import motoristas
import alugueis

def relatorio_veiculos_disponiveis():
    """
    Gera um relatório de veículos disponíveis para aluguel.

    O relatório lista todos os veículos que estão atualmente
    disponíveis na locadora, permitindo ao usuário visualizar
    as opções de veículos que podem ser alugados.
    """

    total_disponiveis = 0
    print('===== VEÍCULOS DISPONÍVEIS =====')
    for veiculo in veiculos:
        if veiculo['status'] == 'Disponível':
            total_disponiveis += 1
            print(f"Placa: {veiculo['placa']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Ano: {veiculo['ano']}")
            print(f"Status: {veiculo['status']}")
            print('-------------------')
            print()
    
    if total_disponiveis == 0:
        print("Nenhum veículo disponível no momento.")
    else:
        print(f'Total de veículos disponíveis: {total_disponiveis}')

def relatorio_veiculos_alugados():
    """
    Gera um relatório de veículos atualmente alugados.

    O relatório lista todos os veículos que estão atualmente
    alugados, permitindo ao usuário visualizar quais veículos
    estão em uso e não disponíveis para aluguel.
    """

    total_alugados = 0
    print('===== VEÍCULOS ALUGADOS =====')
    for veiculo in veiculos:
        if veiculo['status'] == 'Alugado':
            total_alugados += 1
            print(f"Placa: {veiculo['placa']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Ano: {veiculo['ano']}")
            print(f"Status: {veiculo['status']}")
            print('-------------------')
            print()
    
    if total_alugados == 0:
        print("Nenhum veículo está alugado no momento.")
    else:
        print(f'Total de veículos alugados: {total_alugados}')

def relatorio_motoristas_inadimplentes():
    """
    Gera um relatório de motoristas inadimplentes.

    O relatório lista todos os motoristas que possuem pendências
    financeiras ou não cumpriram com suas obrigações, permitindo
    ao usuário identificar motoristas que precisam ser contatados
    ou que não estão em conformidade com as regras da locadora.
    """

    total_inadimplentes = 0
    print('===== MOTORISTAS INADIMPLENTES =====')
    for motorista in motoristas:
        if motorista['status'] == 'Inadimplente':
            total_inadimplentes += 1
            print(f"Nome: {motorista['nome']}")
            print(f"CPF: {motorista['cpf']}")
            print(f"CNH: {motorista['cnh']}")
            print(f"Telefone: {motorista['telefone']}")
            print(f"Status: {motorista['status']}")
            print('-------------------')
            print()
    
    if total_inadimplentes == 0:
        print("Nenhum motorista inadimplente no momento.")
    else:
        print(f'Total de motoristas inadimplentes: {total_inadimplentes}')

def relatorio_motoristas_ativos():
    """
    Gera um relatório de motoristas ativos.

    O relatório lista todos os motoristas que estão atualmente
    ativos e em conformidade com as regras da locadora, permitindo
    ao usuário visualizar os motoristas que estão aptos a realizar
    aluguéis de veículos.
    """

    total_ativos = 0
    print('===== MOTORISTAS ATIVOS =====')
    for motorista in motoristas:
        if motorista['status'] == 'Ativo':
            total_ativos += 1
            print(f"Nome: {motorista['nome']}")
            print(f"CPF: {motorista['cpf']}")
            print(f"CNH: {motorista['cnh']}")
            print(f"Telefone: {motorista['telefone']}")
            print(f"Status: {motorista['status']}")
            print('-------------------')
            print()
    
    if total_ativos == 0:
        print("Nenhum motorista ativo no momento.")
    else:
        print(f'Total de motoristas ativos: {total_ativos}')

def relatorio_motoristas_bloqueados():
    """
    Gera um relatório de motoristas bloqueados.

    O relatório lista todos os motoristas que estão atualmente
    bloqueados, permitindo ao usuário identificar motoristas que
    não estão autorizados a realizar aluguéis de veículos.
    """

    total_bloqueados = 0
    print('===== MOTORISTAS BLOQUEADOS =====')
    for motorista in motoristas:
        if motorista['status'] == 'Bloqueado':
            total_bloqueados += 1
            print(f"Nome: {motorista['nome']}")
            print(f"CPF: {motorista['cpf']}")
            print(f"CNH: {motorista['cnh']}")
            print(f"Telefone: {motorista['telefone']}")
            print(f"Status: {motorista['status']}")
            print('-------------------')
            print()
    
    if total_bloqueados == 0:
        print("Nenhum motorista bloqueado no momento.")
    else:
        print(f'Total de motoristas bloqueados: {total_bloqueados}')

def relatorio_alugueis_ativos():
    """
    Gera um relatório de aluguéis ativos.

    O relatório lista todos os aluguéis que estão atualmente
    ativos, permitindo ao usuário visualizar quais veículos estão
    em uso e quais motoristas estão realizando aluguéis.
    """

    total_ativos = 0
    print('===== ALUGUEIS ATIVOS =====')
    for aluguel in alugueis:
        if aluguel['status'] == 'Ativo':
            total_ativos += 1
            print(f"ID: {aluguel['id']}")
            print(f"CPF do motorista: {aluguel['cpf_motorista']}")
            print(f"Placa do veículo: {aluguel['placa_veiculo']}")
            print(f"Data de Início: {aluguel['data_inicio']}")
            print(f"Valor Semanal: R${aluguel['valor_semanal']:.2f}")
            print(f"Status: {aluguel['status']}")
            print('-------------------')
            print()
    
    if total_ativos == 0:
        print("Nenhum aluguel ativo no momento.")
    else:
        print(f'Total de aluguéis ativos: {total_ativos}')

def relatorio_alugueis_encerrados():
    """
    Gera um relatório de aluguéis encerrados.

    O relatório lista todos os aluguéis que foram encerrados,
    permitindo ao usuário visualizar quais veículos foram devolvidos
    e quais motoristas concluíram seus aluguéis.
    """

    total_encerrados = 0
    print('===== ALUGUEIS ENCERRADOS =====')
    for aluguel in alugueis:
        if aluguel['status'] == 'Encerrado':
            total_encerrados += 1
            print(f"ID: {aluguel['id']}")
            print(f"CPF do motorista: {aluguel['cpf_motorista']}")
            print(f"Placa do veículo: {aluguel['placa_veiculo']}")
            print(f"Data de Início: {aluguel['data_inicio']}")
            print(f"Valor Semanal: R${aluguel['valor_semanal']:.2f}")
            print(f"Status: {aluguel['status']}")
            print('-------------------')
            print()
    
    if total_encerrados == 0:
        print("Nenhum aluguel encerrado no momento.")
    else:
        print(f'Total de aluguéis encerrados: {total_encerrados}')