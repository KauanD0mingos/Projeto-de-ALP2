def buscar_evento(nome_busca, evento):
    evento_encontrado = False
    for buscar in evento:
        if nome_busca == buscar[0]:
            evento_encontrado = True
        else:
            print('\nEvento não existe na lista! ')
    if evento_encontrado:
        print(f'\nEvento {nome_busca} encontrado. ')
        