import funcao
aluno=dict()# CREATE DICTIONARY "ALUNO"
listars={'FACEBOOK', 'INSTAGRAM', 'LINKEDIN', 'TIKTOK', 'TWITTER'}# CREATE LIST FOR NETWORKS

def socialNetwork(msg):
    rs = str()
    while True:
        valor = str(input(msg))
        if valor in 'Ss':
            rs = funcao.redeSocial('Quais destas redes sociais você possui? (FACEBOOK - INSTAGRAM - LINKEDIN - TIKTOK - TWITTER): ') #.upper() #WHICH OF THIS SOCIAL NETWORK DO YOU HAVE
            elemento_invalido = False
            #['Facebook,Linkedin,Instagram']
            #count = 0
            for element in rs:                  # verifica cada item da lista preenchida pelo usuario,
                if element not in listars:      # se faz parte
                    print('\033[0;31mERRO! Informe pelo menos uma das redes sociais descritas.\033[m') #ERROR MESSAGE IF YOU HAVEN'T CHOSEN AT LEAST ONE OF THE SOCIAL NETWORK
                    elemento_invalido = True    # marca q tem um invalido na lista e sai do for()
                    break
                # else:
                #     if(count >= 1):
                #         rs[count] = "                                                                                                 " + rs[count]
                #     count += 1
                    # muda nome pra curto
            if not elemento_invalido:           # verifica se a lista esta sem elementos invalidos
                break                           # esse break sai do while()
        elif valor in 'Nn':
            break
        else:
            print('\033[0;31mERRO! Responda apenas S ou N.\033[m')  # ERROR MESSAGE IF WAS NOT PRESSED S OR N
    return ','.join(rs)               # queremos retornar a lista em forma de string


def groupSocialNetwork(msg):
    grs = str()
    while True:
        valor = str(input(msg))
        if valor in 'Ss':
            grs = funcao.leiagrs('Informe quais são os grupos em cada rede social que você participa: ')
            elemento_invalido = False
            count = 0
            for element in grs:  # verifica cada item da lista preenchida pelo usuario,
                if not elemento_invalido:
                    #print(f'{grs}')  # ERROR MESSAGE IF YOU HAVEN'T CHOSEN AT LEAST ONE OF THE SOCIAL NETWORK
                    #elemento_invalido = False  # marca q tem um invalido na lista e sai do for()
                    break
        elif valor in 'Nn':
            break
        else:
            print('\033[0;31mERRO! Responda apenas S ou N.\033[m')  # ERROR MESSAGE IF WAS NOT PRESSED S OR N
            elemento_invalido=True
        return ','.join(grs)



