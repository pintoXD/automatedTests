# -*- coding: utf-8 -*-
from serialTeste import set_config, get_value
from potMask import mask10, mask20, mask40, mask60, getCurve
from get_panel import getPanel
from get_buzzer import getBuzzer
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

    on_off = set_config('01', '12', '0a')
    time.sleep(1)
    profile = switchCase(getPanel())
    on_off = set_config('01', '12', '0a')
    time.sleep(1)
    
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


    