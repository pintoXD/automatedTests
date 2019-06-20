from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
import time


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
    times = 3
    limit = 15
    pressTime = '0A' ##10 em hexadecimal. Botão será então presssionado por
                     ## 10 * 100 milissegundos.
    pressTimePower = '28' ##40 em decimal. Botão power será pressionado 
                          ##por 40 * 100 milisseegundos

    returnSetRepeat = setRepeat(buttonArrow, times, limit, pressTime)

    if(returnSetRepeat):
        print("Cure profile successfully configured")

        returnSet = set_config(command, buttonPower, pressTimePower)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            print("Power pressed successfully")

            if(getPotLum() == 0):
                print("Main LED (cure LED) successfully shutdown")
            else:
                print("Main LED (cure LED) cannot be shutdown") 
                 
                 
    else:
        print("Error on buttonArrow configuration")





    





