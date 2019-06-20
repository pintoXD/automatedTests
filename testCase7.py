from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
from get_batlvl import *
import time
import random


def sceneOne():

    '''
          Esse cenário trata da situação que, estando sendo
          executado um perfil de cura, o botão ON/OFF é pressidonado
          por um tempo maior do que ON_OFF_TIME, devendo fazer
          com que a cura seja imediatamente encerrada.

    '''
    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    times = random.randint(1, 4)
    limit = 15
    pressTime = '0A' ##10 em hexadecimal. Botão será então presssionado por
                     ## 10 * 100 milissegundos.
    pressTimePower = '28' ##40 em decimal. Botão power será pressionado 
                          ##por 40 * 100 milisseegundos

    ##Seleciona e ativa um perfil de cura, antes de tudo
    returnSetRepeat = setRepeat(buttonArrow, times, limit, pressTime)

    if(returnSetRepeat):
        print("Cure profile successfully configured")
            
        #Se o perfil for iniciado corretamente,
        # esperar por waitTime segudnos e depois pressionar o botão ON/OFF
        waitTime = random.uniform(0, 9)
        time.sleep(waitTime)

        returnSet = set_config(command, buttonPower, pressTimePower)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            #Se o botão for corretamente acionado
            # verifica se a potência do LED caiu a 0 e trata caso não haja.
            #     
            
            print("Power pressed successfully")

            if(getPotLum() == 0):
                print("Main LED (cure LED) successfully shutdown")
            else:
                print("Main LED (cure LED) cannot be shutdown") 
                 
                 
    else:
        print("Error on buttonArrow configuration")

def sceneTwo():

    '''
        Este cenário possui estratégia semelhante ao cenário 1, contudo, 
        ao pressionar o botão ON/OFF, por ON_OFF_TIME antes do LED de cura
        ser desativado. Pensou-se usar thread para verificar a potência
        do LED a cada instante, mas foi notado que somente pressionar
        o botão ON/OFF pelo tempo exato de ON_OFF_TIME já seria suficiente
        para atender a especificação. Contudo, há necessidade de confirmar
        essa escolha.

    '''

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    times = random.randint(1,4)
    limit = 15
    pressTime = '1E'  # 20 em hexadecimal. Botão será então presssionado por
    ## 20 * 100 milissegundos.
    pressTimePower = '14'  # 40 em decimal. Botão power será pressionado
    ##por 40 * 100 milisseegundos

    ##Seleciona e ativa um perfil de cura, antes de tudo
    returnSetRepeat = setRepeat(buttonArrow, times, limit, pressTime)

    if(returnSetRepeat):
        print("Cure profile successfully configured")

        #Se o perfil for iniciado corretamente,
        # esperar por waitTime segundos e depois pressionar o botão ON/OFF
        waitTime = random.uniform(0, 9) #Requisito de acionamento aleatório do botão
        time.sleep(waitTime)


        #Acionar o botão por exatamente ON_OFF_TIME segundos
        returnSet = set_config(command, buttonPower, pressTimePower)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            #Se o botão for corretamente acionado
            # verifica se a potência do LED caiu a 0 e trata caso não haja.
            #

            print("Power pressed successfully")

            if(getPotLum() == 0):
                print("Main LED (cure LED) successfully shutdown")
            else:
                print("Main LED (cure LED) cannot be shutdown")
        
        else:
            print("Error on buttonPower configuration")

    else:
        print("Error on buttonArrow configuration")


def sceneThree():

    '''
        Esse cenário pede que o sistema esteja ligado, mas que
        não esteja executando nenhum perfil de cura.
        Então é solicitado que se mostre o nível da bateria.
        Depois de mostrado, a tensão real na bateria deve ser
        medida.

    '''

    command = '01'
    buttonPower = '12'
    pressTimePower = '28' #40 em hexadecimal
                        ##Botão passará 40 * 100 milissegundos pressionado

           #Acionar o botão por exatamente ON_OFF_TIME segundos
    returnSet = set_config(command, buttonPower, pressTimePower)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

            #Se o botão for corretamente acionado
            # verifica se a potência do LED caiu a 0 e trata caso não haja.
            #

        print("Power pressed successfully")

        ledInfo = getPanel()    

        ##Dorme pelo tempo que os LEDs ficarem acesos
        time.sleep(5)

        if(ledInfo == '01' or ledInfo == '03' or ledInfo == '07' or ledInfo == '0f'):
        
                print("Battery level showed in LEDs")
                print("Real battery level is: ", getBatLvl())

        
        else:
                print("Some error occured when showing battery level")

        
     

    else:
        print("Error on buttonPower configuration")


def sceneFour():

    













