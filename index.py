from cadastro_usu import cadastro
from evento import cadastro_evento, buscar, listar, participar, listar_partici, valor_total, remover
from login import login

usuarios = [['kauan', '@gmail.com', 'k12345']]
eventos = [['semana academica', '04/11/2024', 'livre', 'faculdade', [], 50.00]]

while True:
    print('  [     Event List     ]')
    print('\n\n[ 1 ] - Cadastro de Usuário ')
    print('[ 2 ] - Fazer Login ') 
    
    opcao = input('\nDigite a opção desejada: ')
    if opcao == '1':
        nome = input('Digite seu nome: ')
        email = input('Digite seu E-mail: ')
        senha = input('Digite sua senha: ')
        cadastro.cadastrar_usuario(nome, email, senha, usuarios)
    
        
    elif opcao == '2':
        email = input('\nDigite seu E-mail: ')
        senha = input('Digite sua senha: ')
        login.login(email, senha, usuarios)
        
        while True:
            print('\n[ 1 ] - Cadastro de Evento')
            print('[ 2 ] - Buscar Evento')
            print('[ 3 ] - Listar Eventos')
            print('[ 4 ] - Remover Evento')
            print('[ 5 ] - Participar de Evento (Inscrição)')
            print('[ 6 ] - Listar Participantes do Evento')
            print('[ 7 ] - Verificar Valor Arrecadado')
            print('[ 8 ] - Funcionalidade extra (use criatividade)')
            print('[ 0 ] - Sair ')
            
            opcao = input('\nDigite a opção desejada: ')
            if opcao  == '1':
                while True:
                    nome_evento = input('\nDigite o nome do evento:')
                    if nome_evento == '':
                        print('Este campo não pode estar vazio! ')
                    else:
                        break
                    
                while True:
                    data = input('\nDigite a data do evento (dd/mm/aa):').split('/')
                    if not data[0].isdigit() or not data[1].isdigit() or not data[2].isdigit():
                        print('Erro: A data deve conter apenas números.')
                    else:
                        break

                while True:
                    classificacao = input('\nDigite a classificação do evento:')
                    if classificacao == '':
                        print('Este campo não pode estar vazio! ')
                    else:
                        break
    
                while True:
                    local_evento = input('\nDigite o local do evento:')
                    if local_evento == '':
                        print('Este campo não pode estar vazio! ')
                    else:
                        break
                cadastro_evento.cadastrar_eventos(nome_evento, data, classificacao, local_evento, eventos)
                
            elif opcao == '2':
                nome_busca = input('Digite o nome do evento que deseja buscar: ')
                buscar.buscar_evento(nome_busca, eventos)
                
            elif opcao == '3':
                listar.listar_evento(eventos)
                
            elif opcao == '4':
                nome_evento = input('Digite o nome do evento que deseja remover: ')
                remover.remover_evento(nome_evento, eventos)
                
            elif opcao == '5':
                print('\n[ Catálogo de Eventos Disponíveis ]')
                for evento in eventos:
                    print(f'\nNome: {evento[0]}, Data: {evento[1]}, Classificação: {evento[2]}, Local: {evento[3]}, valor: {evento[5]} R$ ')
        
                nome_evento = input('\nDigite o nome do evento que deseja participar? ')
                nome = input('Digite seu nome? ')
                participar.participar_evento(nome_evento, nome, eventos)
                
            elif opcao == '6':
                opcao = input('Digite o (1) para listar de um evento especifico ou (2) para listar todos? ')
                if opcao == '1':
                    nome_evento = input('Digite o nome do evento que deseja listar os participantes: ')
                    listar_partici.listar_participantes(nome_evento, eventos)
                elif opcao == '2':
                    listar_partici.listar_todos(eventos)
                else:
                    print('Opção inválida! ')
                    
            elif opcao == '7':
                nome_evento = input('Digite um nome de um evento ou não digite nada para verificar todos os valores: ')
                valor_total.verificar_valor_arrecadado(nome_evento, eventos)
            
            elif opcao == '0':
                print('\n     Saindo...')
                break
    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')