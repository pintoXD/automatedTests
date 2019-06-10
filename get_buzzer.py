from serialTeste import *

def getBuzzer():
    buz = get_value('03')
    
    if(buz[0:2] == '99'):
        buz = buz[2:]
    else:
        return 'error: message has no ACK'
    if(buz[0:2] == '03'):
        buz = buz[2:]
        print('responding to command 0x03')
    else:
        return 'error: response to unrequired command'
    if(buz[len(buz)-1:len(buz)-2] == 'ff'):
        buz = buz[:len(buz)-2]
    else:
        return 'error: message has no FIN'
    
    buz_info = []

    for x in range(len(buz)-1):
        #Sugestão de correção se necessário
        # if (x < 3):
        #     buz_infoA = buz_info + (int(buz[x], 16), int(buz[x+1], 16))
        # else:
        #     buz_infoB = buz_info + (int(buz[x], 16), int(buz[x+1], 16))
       
        buz_info = buz_info + (int(buz[x], 16), int(buz[x+1], 16))


  
    
    return buz_info
    

    

