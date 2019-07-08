from serialTeste import set_config, get_value
from potMask import *
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
        '[0, 0, 0, 1]': 60,
        '[0, 0, 1, 0]': 40,
        '[0, 1, 0, 0]': 20,
        '[1, 0, 0, 0]': 10,
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
        FILE = open('randinfo.txt', 'w')
        FILE.write('{}\n'.format(rtime))
        FILE.close()
    
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
    x = 2.6
    case = switchCase2(str(panel_after))
    time.sleep(2.6)
    while(x < case):
        x = x + 1
        if(getPotLum() == 0):
            print('teste falhou. led azul nao parece estar ligado')
        else:
            time.sleep(1)
    
    if((j - i) == 1 or (i - j) == 3):
        print("teste ok")
        print(j , i)
    else:
        print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')

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
        print('erro no teste. nao houve beep')
    else:
        vbat = getBatLvl()
        print(vbat)
        if(vbat < 3.8):
            print('teste falhou. perfil de cura executado alem da restricao de bateria')
        else:
            panel_after = getPanel()
            i, j = getIndex(panel_before, panel_after)
            if((j - i) == 1 or (i - j) == 3):
                print("teste ok")
                print(j , i)
            else:
                print('falha. a ativacao de seta 1 vez nao mudou o perfil na ordem estabelecida')
                print(j, i)
            print(j)

def censeta2():
    if(getPotLum() != 0):
        print('led de cura ainda esta ativado')
    else:
        seta = set_config('01', '11', '02')
        time.sleep(0.2)
        panel_before = getPanel()

        on_off = set_config('01', '12', '32')
        time.sleep(5)        

        rtime = random.randint(10, 15)
        rhex = hex(rtime)[2:]
        if(len(rhex) < 2):
            rhex = '0' + rhex
        

        seta = set_config('01', '11', rhex)
        time.sleep(rtime/10)
        
        panel_after = getPanel()

        if(panel_before != panel_after):
            print('teste falhou. seta interfere no mosotrador de bateria')
        else:
            print('teste passou')


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
        print("Perfil ativo: ", profile)
        
        #print('ON/OFF: ', on_off)

        curve = getCurve(profile)
        if(profile == 10):
            for c in curve:
                if(mask10(c[1], c[0])):
                    return 'teste passou'
                else:
                    print(c)
                    return 'teste falhou'
        elif(profile == 20):
            for c in curve:
                if(mask20(c[1], c[0])):
                    return 'teste passou'
                else:
                    print(c)
                    return 'teste falhou'
        elif(profile == 40):
            for c in curve:
                if(mask40(c[1], c[0])):
                    return 'teste passou'
                else:
                    print(c)
                    return 'teste falhou'
        else:
            for c in curve:
                if(mask60(c[1], c[0])):
                    return 'teste passou'
                else:
                    print(c)
                    return 'teste falhou'

def subcenonoff2():
    if(getPotLum() != 0):
        return 'led de cura ainda esta ativado'
    else:
        if(getBatLvl() < 3.8):
            rtime = random.randint(2, 14)
            rhex = hex(rtime)[2:]
            if(len(rhex) < 2):
                rhex = '0' + rhex
            on_off = set_config('01', '12', rhex)
            time.sleep(rtime/10)
            print('ON/OFF: ', on_off)
            time.sleep(1)
            buz = getBuzzer()
            if(len(buz) == 0):
                return 'teste falhou. nao houve beep'
            else:
                if(getPotLum() != 0):
                    return 'teste falhou. foi iniciado um novo ciclo'
                else:
                    return 'teste passou'
        else:
            print('Bateria está acima de VBAT_MIN')

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
        vbat = getBatLvl()
        print(panel_before, vbat)
    
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
        if(panel_after not in options):
            return 'falha. o mostrador de carga nao obedece as especificacoes'
        else:
            vbat = getBatLvl()
    
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

    panel_before = getPanel()

    on_off = set_config('01', '12', rhex)
    time.sleep(rtime/10)

    time.sleep(5)
    
    panel_after = getPanel()

    if(panel_before != [0,0,0,0]):
        return 'erro: dispositivo nao esta em baixo consumo'
    else:
        pass

    if(panel_after != [0,0,0,0]):
        return 'erro: dispositivo nao esta em baixo consumo'
    else:
        return 'teste passou'

#for i in range(50):
print(cen2subonoff4())