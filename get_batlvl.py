from serialTestes import *

def getBatLvl():
    batlvl = get_value('04')

    if(batlvl[0:2] == '99'):
        batlvl = batlvl[2:]
    else:
        return 'error: message has no ACK'
    if(batlvl[0:2] == '04'):
        batlvl = batlvl[2:]
        print('responding to command 0x04')
    else:
        return 'error: response to unrequired command'
    if(batlvl[len(batlvl)-1:len(batlvl)-2] == 'ff'):
        batlvl = batlvl[:len(batlvl)-2]
    else:
        return 'error: message has no FIN'

    batlvl = int(batlvl, 16)

    return batlvl