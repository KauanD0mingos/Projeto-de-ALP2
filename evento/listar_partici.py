def listar_participantes(nome_evento, lista_eventos):
    for evento in lista_eventos:
        if evento[0] == nome_evento:
            if len(evento[4]) == 0:
                print(f'\nNão há participantes cadastrados para o evento "{nome_evento}".')
            else:
                print(f'\nParticipantes do evento "{nome_evento}":')
                for participante in evento[4]:
                    print(f'- {participante}')
            return  
    print(f'\nEvento "{nome_evento}" não encontrado.') 
    
def listar_todos(lista_eventos):
    for evento in lista_eventos:
            print(f'\nEvento: "{evento[0]}"')
            if len(evento[4]) == 0:
                print('  Não há participantes cadastrados.')
            else:
                print('  Participantes:')
                for participante in evento[4]:
                    print(f'  - {participante}')
    return