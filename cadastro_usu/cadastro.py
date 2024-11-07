def cadastrar_usuario(nome, email, senha, usuarios):
    if nome == '':
        print('\n\033[1;31mDigite um nome válido\033[m\n')
        return
    if '@gmail.com' not in email.lower() and '@gmail.edu' not in email.lower() and '@gmail.gov' not in email.lower():
        print('\t\n\033[1;31mE-mail inválido! Digite no formato (@gmail.)\033[m\n')
        return
    if senha.isdigit() or len(senha) < 5:
        print('\nSua senha deve conter letras e números e ter pelo menos 5 caracteres!')
        return

    senha2 = input('\nConfirme sua senha: ')
    if senha != senha2:
        print('\nAs senhas não conferem!')
    else:
        usuarios.append([nome, email, senha])
        print(f'\nUsuário {nome} cadastrado com sucesso!')
    return True