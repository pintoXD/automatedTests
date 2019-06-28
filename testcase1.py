from serialTeste import set_config, get_value
from potMask import maskSelect
from get_panel import getPanel
from get_buzzer import getBuzzer
from get_led_voltage import getPotLum
from get_batlvl import getBatLvl
import random
import time

## Cenário 1: SETA
# Subcenário 1:
def switchCase2(var):
    switcher = {
<<<<<<< Updated upstream:testcase1.py
        '[0, 0, 0, 1]': 10,
        '[0, 0, 1, 0]': 20,
        '[0, 1, 0, 0]': 40,
        '[1, 0, 0, 0]': 60,
=======
        '[0,0,0,1]': 10,
        '[0,0,1,0]': 20,
        '[0,1,0,0]': 40,
        '[1,0,0,0]': 60,
>>>>>>> Stashed changes:TC-1.py
    }
    return switcher.get(var, 'invalid configuration')

def getIndex(var1 = [] ,var2 = []):
    index1 = 0
    index2 = 0
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

def subcenseta1():
    
    rtime = random.randint(10, 30)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    
    seta = set_config('01', '11', '0A')
    time.sleep(1)
    panel_before = getPanel()

    seta = set_config('01', '11', rhex)
    time.sleep((rtime/10))


    panel_after = getPanel()
    i, j = getIndex(panel_before, panel_after)

    if((j - i) == 1 or (i - j) == 3):
        print("teste ok")
        print(j , i)
    else:
        print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')
        print(j, i)
    return j

def subcenseta2():
    rtime = random.randint(10, 30)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    panel_before = getPanel()
    on_off = set_config('01', '12', '0A')
    time.sleep(1)
    print('ON/OFF: ',on_off)

    time.sleep(5)

    seta = set_config('01', '11', rhex)
    print('Seta: ',seta)
    time.sleep(rtime/10)
    panel_after = getPanel()
    
    i, j = getIndex(panel_before, panel_after)
    x = 0
    case = switchCase2(str(panel_after))

    while(x != case):
        x = x + 1
        if(getPotLum() == 0):
            return 'teste falhou. led azul nao parece estar ligado'
        else:
            time.sleep(1)
    
    if((j - i) == 1 or (i - j) == 3):
        print("teste ok")
        print(j , i)
    else:
        print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')
        print(j, i)
    return j

def subcenseta3():
    rtime = random.randint(10, 30)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    
    on_off = set_config('01', '12', '0A')
    time.sleep(1)
    panel_before = getPanel()

    time.sleep(5)

    seta = set_config('01', '11', rhex)
    time.sleep(rtime/10)
    print('Seta: ',seta)

    buz = getBuzzer()

    if(buz[0] == 0): #mudar depois para um teste com o período correto do buzzer
        return 'erro no teste. nao houve beep'
    else:
        if(getBatLvl() < 3.8):
            return 'teste falhou. perfil de cura executado alem da restricao de bateria'
        else:
            panel_after = getPanel()
            i, j = getIndex(panel_before, panel_after)
            if((j - i) == 1 or (i - j) == 3):
                print("teste ok")
                print(j , i)
            else:
                print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')
                print(j, i)
            return j
    
def censeta2():
    if(getPotLum() != 0):
        return 'led de cura ainda esta ativado'
    else:
        on_off = set_config('01', '12', '32')
        time.sleep(5)
        print('ON/OFF: '+ on_off)

        rtime = random.randint(10, 30)
        rhex = hex(rtime)[2:]
        if(len(rhex) < 2):
            rhex = '0' + rhex
        panel_before = getPanel()

        seta = set_config('01', '11', rhex)
        time.sleep(rtime/10)
        print('Seta: ', seta)
        panel_after = getPanel()

        if(panel_before != panel_after):
            return 'teste falhou. seta interfere no mosotrador de bateria'
        else:
            return 'teste passou'


def subcenonoff1():
    if(getPotLum() != 0):
        return 'led de cura ainda esta ativado'
    else:
        rtime = random.randint(2, 15)
        rhex = hex(rtime)[2:]
        if(len(rhex) < 2):
            rhex = '0' + rhex

        on_off = set_config('01', '12', rhex)
        time.sleep(rtime/10)
        panel = getPanel()
        panel = str(panel)
        profile = switchCase2(panel)
        print(profile)
        
        print('ON/OFF: ', on_off)
        time.sleep(3)
        if(maskSelect(profile)):
            return 'teste passou. perfil correto acendeu'
        else:
            return 'teste falhou. o perfil acionado nao e o correto'

def subcenonoff2():
    if(getPotLum() != 0):
        return 'led de cura ainda esta ativado'
    else:
        rtime = random.randint(2, 27)
        rhex = hex(rtime)[2:]
        if(len(rhex) < 2):
            rhex = '0' + rhex
        on_off = set_config('01', '12', rhex)
        time.sleep(rtime/10)
        print('ON/OFF: ', on_off)

        buz, = getBuzzer()
        if(buz == 0):
            return 'teste falhou. nao houve beep'
        else:
            if(getPotLum() != 0):
                return 'teste falhou. foi iniciado um novo ciclo'
            else:
                return 'teste passou'

def subcenonoff3():
    rtime = random.randint(30, 50)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex

    on_off = set_config('01', '12', rhex)
    time.sleep(rtime/10)
    print('ON/OFF: ', on_off)

    panel_before = getPanel()
    options = [[0,0,1,1], [0,0,0,1], [0,1,1,1], [1,1,1,1]]
    if(panel_before not in options):
        return 'falha. o mostrador de carga nao obedece as especificacoes'
    else:
        bat_adc_value = getBatLvl()
        print(panel_before, bat_adc_value)
    
    time.sleep(5)

    panel_after = getPanel()
    if(panel_after != [0,0,0,0]):
        return 'falha. dispositivo nao entrou em baixo consumo'
    else:
        return 'teste passou'

def subcenonoff4():
    rtime = random.randint(30, 50)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    panel_before = getPanel()
    if(panel_before != [0,0,0,0]):
        return 'falha. dispositivo nao entrou em baixo consumo'
    else:
        on_off = set_config('01', '12', rhex)
        time.sleep(rtime/10)
        print('ON/OFF: ', on_off)

        panel_after = getPanel()
        options = [[0,0,1,1], [0,0,0,1], [0,1,1,1], [1,1,1,1]]
        if(panel_before not in options):
            return 'falha. o mostrador de carga nao obedece as especificacoes'
        else:
            bat_adc_value = getBatLvl()
            print(panel_before, bat_adc_value)
    
        time.sleep(5)

        panel_after = getPanel()
        if(panel_after != [0,0,0,0]):
            return 'teste falhou. dispositivo nao entrou em baixo consumo'
        else:
            return 'teste passou'
    
def cen2subonoff1():
    rtime = random.randint(2, 29)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    on_off = set_config('01', '12', '0A')
    time.sleep(1)
    print(on_off)
    if(getPotLum() == 0):
        return 'teste falhou. led de cura ligou'
    else:
        time.sleep(5)

        on_off = set_config('01', '12', rhex)
        time.sleep(rtime/10)

        if(getPotLum() != 0):
            return 'teste falhou. led de cura nao desligou'
        else:
            return 'teste passou'


######---------------------------------------######
#falta desenvolver caso on_off 2 subcenario 2


def cen2subonoff3():
    rtime = random.randint(30, 60)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    on_off = set_config('01', '12', rhex)
    time.sleep(rtime/10)

    panel_before = getPanel()

    time.sleep(5)
    
    panel_after = getPanel()

    possibilities = [[1,1,1,1], [0,1,1,1], [0,0,1,1], [0,0,0,1]]
    if(panel_before in possibilities):
        pass
    else:
        return 'erro: carga da bateria nao esta sendo mostrada'

    if(panel_after in possibilities):
        return 'erro: dispositivo nao esta em baixo consumo'
    else:
        return 'teste passou'
    
def cen2subonoff4():
    rtime = random.randint(30, 60)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    time.sleep(3)

    on_off = set_config('01', '12', rhex)
    time.sleep(rtime/10)

    panel_before = get_value('02')

    time.sleep(5)
    
    panel_after = get_value('02')

    if(panel_before == [0,0,0,0]):
        pass
    else:
        return 'erro: dispositivo nao esta em baixo consumo'

    if(panel_after != [0,0,0,0]):
        return 'erro: dispositivo nao esta em baixo consumo'
    else:
        return 'teste passou'


print(subcenonoff1())