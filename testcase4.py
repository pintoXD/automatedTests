# -*- coding: utf-8 -*-
from serialTeste import set_config, get_value
from potMask import maskSelect
from get_panel import getPanel
from get_buzzer import getBuzzer
from get_led_voltage import getPotLum
from potMask import maskSelect
from get_batlvl import getBatLvl
import random
import time

def switchCase(var):
    switcher = {
        [0,0,0,1]: 10,
        [0,0,1,0]: 20,
        [0,1,0,0]: 40,
        [1,0,0,0]: 60,
    }
    return switcher.get(var, 'invalid configuration')

def cen1():

    profile_on = switchCase(getPanel())
    
    on_off = set_config('01', '12', '0a')
    print(on_off)
    result = maskSelect(profile_on)
    if(result != 'ok'):
        print(result)
    else:
        return 'teste passou'


    