def buscar_evento(nome_busca, evento):
    for buscar in evento:
        if nome_busca == buscar[0]:
            print(f'\nEvento {nome_busca} encontrado. ')
        else:
            print('\nEvento não existe na lista! ')