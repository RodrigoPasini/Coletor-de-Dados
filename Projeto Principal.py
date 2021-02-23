import funcao
import redesocial
# PROGRAM - CADASTRO DOS ALUNOS
alunos=list()# CREATE LIST "ALUNOS"
aluno = dict()# CREATE DICTIONARY "ALUNO"
while True: # LOOP START
    aluno.clear()
    aluno['Primeiro Nome'] = funcao.leiaPN('Primeiro Nome: ').upper()# KEY: FIRST NAME
    aluno['Segundo Nome'] = funcao.leiaSN('Segundo Nome: ').upper()# KEY: SECOND NAME
    aluno['Sobrenome'] = funcao.leiaSobre('Sobrenome: ').upper()# KEY: SURNAME
    aluno['Cidade'] = funcao.leiaCidade('Cidade onde reside: ').upper() #KEY: CITY
    aluno['UF'] = funcao.leiaUF('Estado de residência: ').upper() #KEY: STATE
    aluno['Idade'] = funcao.leiaIdade('Idade: ') # Key: AGE
    aluno['Rede Social'] = redesocial.socialNetwork('Você possui rede social? [S/N]')  # QUESTION ABOUT SOCIAL NETWORK
    if len(aluno['Rede Social']) != 0:
       aluno['Grupo Rede Social'] = redesocial.groupSocialNetwork(('Você participa de algum grupo na área de TI em uma destas redes sociais? [S/N]'))  #DO YOU APLLIED IN ANYONE SOCIAL NETWORK GROUP?

    alunos.append(aluno.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0] # VARIABLE TO CONTINUE OR NOT
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.') # ERROR MESSAGE IF WAS NOT PRESS S OR N
    if resp == 'N':
        break

tamanhos = funcao.pega_maiores_tamanhos(aluno, alunos)

print('Código ', end='') # ORDER THE KEYS
count = 0
for i in aluno.keys():
    print(f'{i:<{tamanhos[count]}}', end='')
    count += 1
print()

count = 0
for k, v in enumerate(alunos): # ORDER THE KEYS
    count = 0
    print(f'{k+1:>6} ', end='')
    for d in v.values():
        print(f'{d:<{tamanhos[count]}}', end='')
        count += 1
    print()
print()
print(alunos)
