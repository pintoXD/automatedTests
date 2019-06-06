from serialTeste import *

def switchCase(var):
    switcher{
        '01': [0,0,0,1]
        '02': [0,0,1,0]
        '03': [0,0,1,1]
        '04': [0,1,0,0]
        '07': [0,1,1,1]
        '08': [1,0,0,0]
        '0f': [1,1,1,1]
    }
    return switcher.get(var, 'invalid configuration')
    
def getPanel():
    valor_panel = get_value('02')

    if(valor_panel[0:2] == '99')
        valor_panel = valor_panel[2:]
    else:
        return 'error: message has no ACK'
    if(valor_panel[len(valor_panel)-1:len(valor_panel)-2]
        valor_panel = valor_panel[:len(valor_panel)-2]
    else:
        return 'error: message has no FIN'

    return switchCase(valor_panel)