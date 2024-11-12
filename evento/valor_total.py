def verificar_valor_arrecadado(nome_evento, lista_eventos):
    total_geral = 0

    if not nome_evento:
        print('\nValor arrecadado por todos os eventos:')
        for evento in lista_eventos:
            valor_arrecadado = len(evento[4]) * evento[5]
            total_geral += valor_arrecadado
            print(f'Evento {evento[0]} : R${valor_arrecadado}')
        
        print(f'\nValor total arrecadado de todos os eventos: R${total_geral:.2f}')
        return
    
    for evento in lista_eventos:
        if evento[0] == nome_evento:
            valor_arrecadado = len(evento[4]) * evento[5]
            print(f'\nValor arrecadado do evento {nome_evento} : R${valor_arrecadado}')
            return

    print(f'\nEvento {nome_evento} não encontrado.')
