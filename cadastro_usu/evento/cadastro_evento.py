def cadastrar_eventos(nome_evento, data, classificacao, local_evento, lista_eventos):
    while True:
        evento_existe = False
        for evento in lista_eventos:
            if nome_evento == evento[0]:
                evento_existe = True
                break
        if evento_existe:
            print('\nJá existe um evento com este nome!')
        elif nome_evento == '':
            print('\nDigite um nome válido')
        else:
            break
        
        return evento_existe

    while True:

        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])

        if dia < 1 or dia > 31:
            print('Dia inválido!')
        elif mes < 1 or mes > 12:
            print('Mês inválido!')
        elif ano < 2024:
            print('Ano inválido!')
        else:
            break
        return True

    evento = [nome_evento, f"{dia}/{mes}/{ano}", classificacao, local_evento]
    lista_eventos.append(evento)
    print(f'\nEvento {nome_evento} cadastrado com sucesso!')
