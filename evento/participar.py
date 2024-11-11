def participar_evento(nome_evento, participante, lista_eventos):
    for evento in lista_eventos:
        if evento[0] == nome_evento:
            if participante in evento[4]:
                print(f'\nParticipante {participante} já está inscrito no evento {nome_evento}.')
                return
            
            pergunta = input('Deseja participar do evento? (s/n) ').strip().lower()
            if pergunta == 's':
                evento[4].append(participante)
                print(f'\nParticipante {participante} adicionado ao evento {nome_evento}.')
            else:
                print('Inscrição cancelada!')
            return
    
    print(f'\nEvento {nome_evento} não encontrado.')
