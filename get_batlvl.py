from serialTeste import set_config, get_value

def getBatLvl():
    batlvl = get_value('05')

    if(batlvl[0:2] == '99'):
        batlvl = batlvl[2:]
    else:
        return 'error: message has no ACK'
    if(batlvl[0:2] == '05'):
        batlvl = batlvl[2:]
        print('responding to command 0x04')
    else:
        return 'error: response to unrequired command'

    if(batlvl[len(batlvl)-2:] == 'ff'):
        batlvl = batlvl[:len(batlvl)-2]
        # print("ENTROU PORRA")
    else:
        print("Bat level is: ", batlvl)
        return 'error: message has no FIN'
        

    batlvl = int(batlvl, 16)

    # print("Volts: ", ((3.3 * batlvl)/4095)*2)
    return batlvl
    #return batlvl


def getBatVoltage():
    batlvl = getBatLvl()
    
    return ((3.3 * batlvl)/4095)*2
