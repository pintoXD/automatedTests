import time
from get_led_voltage import getPotLum
from serialTeste import set_config
def mask10(data, time):
    if(1 < time and time < 3):
        if(data <= 3643 and data >= 2981):
            return True
        else:
            return False
    elif(3 <= time and time < 6):
        y = (-404)*time + 4524
        if(data <= y + 331 and data >= y - 331):
            return True
        else:
            return False
    elif(6 <= time and time < 9):
        if(data <= 2310 and data >= 1890):
            return True
        else:
            return False
    elif(time >= 9 and data < 2310):
        return True
    else:
        return True
    
def mask20(data, time):
    if(2.5 < time and time < 7):
        y = (552*time - 552)
        if(data <= y + 331 and data >= y - 331):
            return True
        else:
            return False

    elif(7 <= time and time < 10):
        if(data <= 3643 and data >= 2981):
            return True
        else:
            return False

    elif(10 <= time and time < 13):
        y = (-404)*time + 7352
        if(data <= y + 331 and data >= y - 331):
            return True
        else:
            return False

    elif(13 <= time and time < 19):
        if(data <= 2310 and data >= 1890):
            return True
        else:
            return False

    elif(time >= 19 and data <= 2310):
        return True
    else:
        return True


def mask40(data, time):
    if(2.5 < time and time < 7):
        y = (552*time - 552)
        if(data <= y + 331 and data >= y - 331):
            return True
        else:
            return False

    elif(7 <= time and time < 10):
        if(data <= 3643 and data >= 2981):
            return True
        else:
            return False

    elif(10 <= time and time < 13):
        y = (-404)*time + 7352
        if(data <= y + 331 and data >= y - 331):
            return True
        else:
            return False
    
    elif(13 <= time and time < 39):
        if(data <= 2310 and data >= 1890):
            return True
        else:
            return False

    elif(time >= 39 and  data < 2310):
        return True
    else:
        return True

def mask60(data, time):
    if(1 < time and time < 3):
        if(data <= 3643 and data >= 2981):
            return True
        else:
            return False
    elif(3 <= time and time < 6):
        y = (-404)*time + 4524
        if(data <= y + 331 and data >= y - 331):
            return True
        else:
            return False
    elif(6 <= time and time < 59):
        if(data <= 2310 and data >= 1890):
            return True
        else:
            return False
    elif(time >= 60 and data <= 2310):
        return True
    else:
        return True

def getCurve(profile):
    zero = time.time()
    future = zero + profile
    
    if(profile == 20 or profile == 40):
        time.sleep(1)
    
    now = time.time()
    profcurve = []
        
    while(now <= future):
        p = getPotLum()
        now = time.time()
        t = now - zero
        profcurve.append((t, p))
    FILE = open('data.txt', 'a')
    for l in profcurve:
        FILE.write(str(l[0])+'; ')
        FILE.write(str(l[1])+'\n')
    FILE.write('\n')
    FILE.close()
    return profcurve
