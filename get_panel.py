from serialTeste import get_value, set_config
import time

def switchCase(var):
    switcher = {
        # 00000000
        '00000001': [0,0,0,1],
        '00000100': [0,0,1,0],
        '00000101': [0,0,1,1],
        '00010000': [0,1,0,0],
        '00010101': [0,1,1,1],
        '01000000': [1,0,0,0],
        '01010101': [1,1,1,1],
        '00000000': [0,0,0,0]
    }
    return switcher.get(var, 'invalid configuration')
    
def getPanel():
    
    panel_value = get_value('02')
    
    if(panel_value[0:2] == '99'):
        panel_value = panel_value[2:]
    else:
        return 'error: message has no ACK'
    if(panel_value[0:2] == '02'):
        panel_value = panel_value[2:]
        print('responding to command 0x02')
    else:
        return 'error: response to unrequired command'
    if(panel_value[len(panel_value)-2:] == 'ff'):
        panel_value = panel_value[:len(panel_value)-2]
    else:
        return 'error: message has no FIN'
# 
    # panel_value = panel_value[6:]

    return switchCase(panel_value)
