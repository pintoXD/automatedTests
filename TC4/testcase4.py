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
        '[0, 0, 0, 1]': 60,
        '[0, 0, 1, 0]': 40,
        '[0, 1, 0, 0]': 20,
        '[1, 0, 0, 0]': 10,
    }
    return switcher.get(var, 'invalid configuration')

def testscenario1():

    set_config('01', '11', '05')
    time.sleep(0.5)
    
    panel = getPanel()
    profile = switchCase(str(panel))
    if(profile == 'invalid configuration'):
        FILE = open('TC4_CEN_1.txt', 'a')
        print('Unexpected profile value. Panel read: {}'.format(panel), file = FILE)
        FILE.close()
        return False
    
    set_config('01', '12', '02')
    time.sleep(0.2)
    
    curve = getCurve(profile)

    for i in range(len(curve)):
        if(curve[i][1] == 0):
            if(i < 0 and i < len(curve) - 1):
                curve[i][1] = (curve[i-1][1] + curve[i+1][1])/2
    
    flag = []
    
    if(profile == 10):
        for c in curve:
            if(mask10(c[1], c[0])):
                flag.append(1)
            else:
                FILE = open('TC4_CEN_1.txt', 'a')
                print(c, '\t', profile, file = FILE)
                FILE.close()
                flag.append(0)
    elif(profile == 20):
        for c in curve:
            if(mask20(c[1], c[0])):
                flag.append(1)
            else:
                FILE = open('TC4_CEN_1.txt', 'a')
                print(c, '\t', profile, file = FILE)
                FILE.close()
                flag.append(0)
    elif(profile == 40):
        for c in curve:
            if(mask40(c[1], c[0])):
             flag.append(1)
            else:
                FILE = open('TC4_CEN_1.txt', 'a')
                print(c, '\t', profile, file = FILE)
                FILE.close()
                flag.append(0)
    else:
        for c in curve:
            if(mask60(c[1], c[0])):
                flag.append(1)
            else:
                FILE = open('TC4_CEN_1.txt', 'a')
                print(c, '\t', profile, file = FILE)
                FILE.close()
                flag.append(0)
    if(min(flag) == 1):
        return True
    else:
        return False


def main():
    # tests = [testscenario1, testscenario2, testscenario3, testscenario4, testscenario5, testscenario6,\
    #         testscenario7, testscenario8, testscenario9, testscenario10, testscenario11, testscenario12]
    cont = 0
    initialTime = time.time()
    for i in range(50):
            print("Round ", i)
            
            aux = testscenario1()
        
            if(aux):
                cont = cont + 1
            
            time.sleep(1)

    
    
    print("Successful tests percentage: ", (cont/50)*100)

    print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100)

    print("Elapsed time: ", time.time() - initialTime)


    with open('output_TC1s.txt', 'a') as f:
            print("Scene Four:")

            print("Successful tests percentage: ", (cont/50)*100, file=f)

            print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100, file=f)

            print("Elapsed time: ", time.time() - initialTime, file = f)

            print("############# END ###########\n\n", file=f)
    
    f.close()

if __name__ == "__main__":
  main()
    