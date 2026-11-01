from veiculos import veiculos
from motoristas import motoristas
from alugueis import alugueis

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

def dashboard():
    """
    Exibe um resumo geral da situação da locadora.

    O dashboard apresenta indicadores consolidados de veículos,
    motoristas e aluguéis, além da taxa de ocupação da frota,
    permitindo uma visão rápida do estado atual da locadora.
    """
    print('===== DASHBOARD =====')
    print()

    print('🚗 VEÍCULOS')
    print(f'Total de veículos cadastrados: {len(veiculos)}')
    total_disponiveis = 0
    for veiculo in veiculos:
        if veiculo['status'] == 'Disponível':
            total_disponiveis += 1
    print(f'Disponíveis: {total_disponiveis}')

    total_alugados = 0
    for veiculo in veiculos:
        if veiculo['status'] == 'Alugado':
            total_alugados += 1
    print(f'Alugados: {total_alugados}')

    total_em_manutencao = 0
    for veiculo in veiculos:
        if veiculo['status'] == 'em manutenção':
            total_em_manutencao += 1
    print(f'Em Manutenção: {total_em_manutencao}')
    print()

    print('👤 MOTORISTAS')
    print(f'Total de motoristas cadastrados: {len(motoristas)}')
    total_ativos = 0
    for motorista in motoristas:
        if motorista['status'] == 'Ativo':
            total_ativos += 1
    print(f'Ativos: {total_ativos}')

    total_inadimplentes = 0
    for motorista in motoristas:
        if motorista['status'] == 'Inadimplente':
            total_inadimplentes += 1
    print(f'Inadimplentes: {total_inadimplentes}')

    total_bloqueados = 0
    for motorista in motoristas:
        if motorista['status'] == 'Bloqueado':
            total_bloqueados += 1
    print(f'Bloqueados: {total_bloqueados}')
    print()

    print('📋 ALUGUÉIS')
    print(f'Total de aluguéis cadastrados: {len(alugueis)}')
    total_ativos = 0
    for aluguel in alugueis:
        if aluguel['status'] == 'Ativo':
            total_ativos += 1
    print(f'Ativos: {total_ativos}')

    total_encerrados = 0
    for aluguel in alugueis:
        if aluguel['status'] == 'Encerrado':
            total_encerrados += 1
    print(f'Encerrados: {total_encerrados}')
    print()

    print('📈 INDICADORES')
    if len(veiculos) > 0:
        taxa_ocupacao = (total_alugados / len(veiculos)) * 100
    else:
        taxa_ocupacao = 0

    print(f'Taxa de ocupação da frota: {taxa_ocupacao:.1f}%')