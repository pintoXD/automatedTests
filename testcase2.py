from serialTeste import set_config, get_value
from potMask import *
from get_panel import getPanel
from get_buzzer import getBuzzer
from get_led_voltage import getPotLum
from get_batlvl import getBatLvl
import random
import time

def switchCase2(var):
    switcher = {
        '[0, 0, 0, 1]': 10,
        '[0, 0, 1, 0]': 20,
        '[0, 1, 0, 0]': 40,
        '[1, 0, 0, 0]': 60,
        '[0, 0, 0, 0]': 0
    }
    return switcher.get(var, 'invalid configuration')

#Cenário SETA 1:
def testscenario1():
    seta = set_config('01', '11', '0a')
    time.sleep(1)
    
    seta = set_config('01', '11', '0a')
    time.sleep(1)
    panel_before = switchCase2(str(getPanel()))

    seta = set_config('01', '11', '0a')
    time.sleep(1)
    panel_after = switchCase2(str(getPanel()))

    buz = getBuzzer()
    if(len(buz) == 0):
        return 'teste falhou. não há beeps'
    else:
        if(panel_before == 10):
            if(panel_after == 20):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
        elif(panel_before == 20):
            if(panel_after == 40):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
        elif(panel_before == 40):
            if(panel_after == 60):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
        elif(panel_before == 60):
            if(panel_after == 10):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
    return flag

#Cenário SETA 2:
def testscenario2():
    seta = set_config('01', '11', '0a')
    time.sleep(1)
    
    seta = set_config('01', '11', '0a')
    time.sleep(1)
    panel_before = switchCase2(str(getPanel()))

    on_off = set_config('01', '12', '0a')
    time.sleep(1)

    time.sleep(5)

    seta = set_config('01', '11', '0a')
    time.sleep(1)
    panel_after = switchCase2(str(getPanel()))

    buz = getBuzzer()
    if(len(buz) == 0):
        return 'teste falhou. não há beeps'
    else:
        if(panel_before == 10):
            if(panel_after == 20):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
        elif(panel_before == 20):
            if(panel_after == 40):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
        elif(panel_before == 40):
            if(panel_after == 60):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
        elif(panel_before == 60):
            if(panel_after == 10):
                flag = True
            else:
                print(panel_before, panel_after)
                return 'teste falhou. ordem de transição incorreta'
    return flag

#Cenário ON/OFF 1:
def testscenario3():
    seta = set_config('01', '11', '0a')
    time.sleep(1)

    rtime = random.randint(2, 15)
    rhex = hex(rtime)[2:]
    if(len(rhex) < 2):
        rhex = '0' + rhex
    
    on_off = set_config('01', '12', rhex)
    time.sleep(rtime/10)

    buz = getBuzzer()
    if(buz[0][0] == 0):
        return 'erro: não houve beep'

    panel = getPanel()
    profile = switchCase2(str(panel))
    
    now = time.time()
    future = now + profile
    while(now <= future):
        if(panel != getPanel()):
            return 'erro. led não corresponde ao perfil ativado'
        now = time.time()
    return 'teste passou'

#Cenário ON/OFF 2:
def testscenario4():
    seta = set_config('01', '11', '0a')
    time.sleep(1)

    on_off = set_config('01', '12', '0a')
    time.sleep(1)

    panel = getPanel()
    profile = switchCase2(str(panel))

    rtime = random.randint(1, profile)
    time.sleep(rtime)

    on_off = set_config('01', '12', '02')

    if(getPotLum() != 0):
        return 'erro: led de cura não desligou'
    else:
        return 'teste passou'