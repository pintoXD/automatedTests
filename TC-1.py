from serialTeste import set_config, get_value
from potMask import mask10, mask20, mask40, mask60
from get_panel import getPanel
import random
import time

## Cenário 1: SETA
# Subcenário 1:

def getIndex(var1 = [] ,var2 = []):
    if(var1 == None or var2 == None):
        return 'um dos vetores está vazio'
    else:    
        for i in range(len(var1)):
            if(var1[i] == 1):
                index1 = i
        for j in range(len(var2)):
            if(var2[j] == 1):
                index2 = j
        return index1, index2

def switchCase(var):
    switcher = {
        0: 10,
        1: 20,
        2: 40,
        3: 60
    }
    return switcher.get(var, 'invalid configuration')

def subcen1():
    for i in range(31):
        rtime = random.randint(10, 30)
        rtime = hex(rtime)[2:]

        panel_before = getPanel()

        seta = set_config('01', '11', rtime)
        print(seta)

        panel_after = getPanel()

        i, j = getIndex(panel_before, panel_after)

        if((j - i) == 1 or (i - j) == 3):
            print("teste ok")
            print(j , i)
        else:
            print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')
            print(j, i)
        return j

def subcen2():
    rtime = random.randint(10, 30)
    rtime = hex(rtime)[2:]
    panel_before = getPanel()
    on_off = set_config('01', '12', '01')
    print('ON/OFF: ',on_off)

    time.sleep(5)

    seta = set_config('01', '11', rtime)
    print('Seta: ',seta)

    panel_after = getPanel()
    
    i, j = getIndex(panel_before, panel_after)

    if((j - i) == 1 or (i - j) == 3):
        print("teste ok")
        print(j , i)
    else:
        print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')
        print(j, i)
    return j

#if __name__ == "__main__":
    #main()
