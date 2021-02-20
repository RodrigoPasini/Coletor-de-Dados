aluno=dict()# CREATE DICTIONARY "ALUNO"
alunos=list()# CREATE LIST "ALUNOS"
estado={'AC', 'AL', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT','MS', 'MG',
        'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP',
        'SE', 'TO'}

def trata_string(msg):
    return msg.lstrip().rstrip()


def leiaPN(msg):
    ok=False
    valor=str()
    while True:
        #aluno['Primeiro Nome']=str(input(msg))
        valor=str(input(msg))
        if valor.isalpha():
            #valor=str(aluno['Primeiro Nome'])
            ok=True
        else:
            print('\033[0;31mERRO! Digite um nome válido.\033[m')
        if ok:
            break
    return trata_string(valor)


def leiaSN(msg):
    ok=False
    valor=str()
    while True:
        aluno['Segundo Nome']=str(input(msg))
        if aluno['Segundo Nome'].isnumeric():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        elif aluno['Segundo Nome'].isspace():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        else:
            valor = str(aluno['Segundo Nome'])
            ok = True
        if ok:
            break
    return valor


def leiaSobre(msg):
    ok=False
    valor=str()
    while True:
        valor = trata_string(str(input(msg)))
        str_compara = valor.replace(" ", "") 
        if len(str_compara) == 0 or str_compara.isnumeric():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        # elif aluno['Segundo Nome'].isspace():
        #     ok = False
        #     print('\033[0;31mERRO! Informação inválida.\033[m')
        else:
            #valor = str(aluno['Segundo Nome'])
            ok = True
        if ok:
            break
    return valor

def leiaCidade(msg):
    ok = False
    valor = 0
    while True:
        aluno['Cidade'] = str(input(msg))
        if aluno['Cidade'].isspace():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        elif aluno['Cidade'].isnumeric():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        else:
            valor = str(aluno['Cidade'])
            ok = True
        if ok:
            break
    return valor


def leiaUF(msg):
    valor=str()
    while True:
        valor = str(input(msg)).upper()
        if valor not in estado:
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        else:
            #valor = str(aluno['UF'])
            break
    return valor.upper()


def leiaIdade(msg):
    ok = False
    valor = 0
    while True:
        aluno['Idade'] = str(input(msg))
        if aluno['Idade'].isnumeric():
            valor = str(aluno['Idade'])
            ok = True
        else:
            print('\033[0;31mERRO! Digite um nome válido.\033[m')
        if ok:
            break
    return valor


def redeSocial(msg):
    ok=False
    valor=0
    while True:
        rs=str(input(msg)).upper()  # 'Facebook, Linkedin, Instagram'
        #------- NOVO
        # rs=rs.replace(' e ',',')
        rs=rs.replace(' ','')   #vamos remover qlquer espaco vazio  -- # 'Facebook,Linkedin,Instagram'
        #------------
        if rs.isspace():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        elif rs.isnumeric():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        else:
            # valor = str(rs)
            #------- NOVO
            valor = rs.split(',')   # vamos quebrar a string em itens, separando por virgula -- # 'Facebook\nLinkedin\nInstagram'
            #-------------
            ok = True
        if ok:
            break
    # print(list(valor))
    return list(valor)  #['Facebook,Linkedin,Instagram']


def gruporedeSocial(msg):
    ok=False
    valor=0
    while True:
        grupors=str(input(msg))
        if grupors.isspace():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        elif grupors.isnumeric():
            ok = False
            print('\033[0;31mERRO! Informação inválida.\033[m')
        else:
            valor = str(grupors)
            ok = True
        if ok:
            break
    return valor


def leiagrs(msg):
    ok=False
    valor=0
    while True:
        grs=str(input(msg))
        if grs.isalpha():       #NOTE: essa funcao nao deixa entrar espaço ou virgula, somente aceita letras. Como faz pra entrar mais de um grupo?
            valor=str(grs)      #       recomendo usar a mesma logica da entrada das redes sociais
            ok=True
        else:
            print('\033[0;31mERRO! Digite um nome válido.\033[m')
        if ok:
            break
    return valor