from projeton1_funcoes import*
cadastros = 'cadastros.txt'
if not arquivo_existe(cadastros):
    criar_arquivo(cadastros)
while True:
    cabecalho('CADASTRANDO NOMES')

    opcao = escolha()
    if opcao == 1:
        cabecalho('CRIAR CADASTRO')
        nome = input('Qual seu nome? ').strip().lower()
        senha = numero_inteiros('Senha:')
        if validar_login(cadastros,nome):
            print('usuario ja existente')
        else:
            print('cadastro criado com sucesso')
            cadastrar(cadastros, nome, senha)
    elif opcao == 2:
        cabecalho('LOGIN')
        nome = input('Qual seu nome? ').strip().lower()
        senha = numero_inteiros('Senha:')
        if validar(cadastros,nome,senha):
            print('login feito com sucesso')
        else:
            print('nome ou senha incorreto')
    elif opcao == 3:
        lerarquivo(cadastros)
    elif opcao == 4:
        print('saindo do programa')
        break
    else:
        print('opcao invalida')