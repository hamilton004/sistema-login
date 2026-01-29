import os
def cabecalho(palavra):
    print('-'*40)
    print(f'{palavra:^40}')
    print('-'*40)

def arquivo_existe(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('houve um erro para criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('houve um erro para ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrar(cadastros,nome= 'desconhecido',senha = 0):
    try:
        a = open(cadastros,'at')
    except:
        print('houve um erro para cadastrar o arquivo')
    else:
        a.write(f'{nome};{senha}\n')
        a.close()


def numero_inteiros(num):
    while True:
        try:
            msg = (int(input(num)))
            return msg
        except:
            print('-'*40)
            print('APENAS NUMEROS SÃO ACEITOS')
def escolha():
    while True:
        opc = numero_inteiros('1 - CADASTRAR\n2 - login\n3 - PESSOAS CADASTRADAS\n4 - SAIR\nESCOLHA UMA DAS OPÇÕES:')
        print('-'*40)
        return opc
def validar(arquivo,n,s):
    if not os.path.exists(arquivo):
        return False
    with open(arquivo,'rt') as a:
        for linha in a :
            if not linha:  # pula linha vazia
                continue
            if ';' not in linha:  # pula linhas mal formatadas
                continue
            name,password = linha.strip().split(';')
            if name.strip().lower() == n and password.strip() == str(s):
                return True
    return False
def validar_login(arquivo, nome):
    nome = nome.strip().lower()
    if not os.path.exists(arquivo):
        return False
    with open(arquivo, 'r') as a:
        for linha in a:
            linha = linha.strip()
            if not linha or ';' not in linha:
                continue
            name, _ = linha.split(';')
            if name.strip().lower() == nome:
                return True
    return False
