def login(email, senha, usuarios):
    while True:
        login_sucesso = False
        for usuario in usuarios:
            if email == usuario[1] and senha == usuario[2]:
                print('\nUsuário Logado')
                login_sucesso = True
                break
        if login_sucesso:
            break
        else:
            print('\nE-mail ou senha inválido.')
            email = input('Digite seu E-mail novamente: ')
            senha = input('Digite sua senha novamente: ')

    return login_sucesso