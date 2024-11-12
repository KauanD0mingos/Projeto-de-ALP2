def remover_evento(nome_evento, lista_eventos):
    for i in range(len(lista_eventos)):
        if lista_eventos[i][0] == nome_evento:
            evento_removido = lista_eventos.pop(i)
            print(f'\nEvento "{evento_removido[0]}" removido com sucesso.')
            return
    print(f'\nEvento "{nome_evento}" não encontrado.')
