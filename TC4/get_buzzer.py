from serialTeste import get_value, set_config

def getBuzzer():
    buz = get_value('03')
    # print("GetBuzzer - Received Word: ", buz)    
    if(buz[0:2] == '99'):
        buz = buz[2:]
    else:
        return 'error: message has no ACK'
    if(buz[0:2] == '03'):
        buz = buz[2:]
        print('responding to command 0x03')
    else:
        return 'error: response to unrequired command'
    if(buz[len(buz)-2:] == 'ff'):
        buz = buz[:len(buz)-2]
    else:
        return 'error: message has no FIN'
    
    buz_info = []

    '''

            Retorna um conjunto de tuplas para cada perfil de cura.
            Perfil de cura 10s -> retorna uma tupla
            Perifil de cura 20s -> Retorna duas tuplas
             
            E assim por diante

            As tuplas são da forma (a ,b), onde a e b significam:
            a -> Tempo de duração do bipe
            b - > Tempo em que o bipe tocou (se 10, 20, 40 ou 60s após o início
                                             do perfil de cura)


    '''
    while(len(buz) != 0):
    
     buz_info = buz_info + [(int(buz[:2], 16), int(buz[2:10], 16))]
     buz = buz[10:]
    
    return buz_info
    

    

