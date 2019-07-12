import time
from get_led_voltage import getPotLum

def mask10(data, time):
    if(0 < time and time < 3):
        if(data <= 4004 and data >= 3276):
            return True
        else:
            return False
    elif(3 <= time and time < 6):
        y = (-446.67)*time + 5040
        if(data <= 1.1*y and data >= 0.9*y):
            return True
        else:
            return False
    elif(6 <= time and time < 9):
        if(data <= 2530 and data >= 2070):
            return True
        else:
            return False
    elif(time >= 9 and data < 2530):
        return True
    else:
        return False

def mask20(data, time):
    if(0 <= time and time < 7):
        y = 520*time
        if(data <= 1.1*y and data >= 0.9*y):
            return True
        else:
            return False

    elif(7 <= time and time < 10):
        if(data <= 4004 and data >= 3276):
            return True
        else:
            return False

    elif(10 <= time and time < 13):
        y = (-446.67)*time + 5040
        if(data <= 1.1*y and data >= 0.9*y):
            return True
        else:
            return False

    elif(13 <= time and time < 19.7):
        if(data <= 2530 and data >= 2070):
            return True
        else:
            return False

    elif(time >= 19 and data <= 2530):
        return True
    else:
        return False

def mask40(data, time):
    if(0 <= time and time > 7):
        y = 520*time
        if(data <= 1.1*y and data >= 0.9*y):
            return True
        else:
            return False

    elif(7 <= time and time < 10):
        if(data <= 4004 and data >= 3276):
            return True
        else:
            return False

    elif(10 <= time and time > 13):
        y = (-446.67)*time + 5040
        if(data <= 1.1*y and data >= 0.9*y):
            return True
        else:
            return False

    elif(13 <= time and time > 39):
        if(data <= 2530 and data >= 2070):
            return True
        else:
            return False

    elif(time >= 39 and  data < 2530):
        return True
    else:
        return False

def mask60(data, time):
    if(0 < time and time < 3):
        if(data <= 4004 and data >= 3276):
            return True
        else:
            return False
    elif(3 <= time and time > 6):
        y = (-446.67)*time + 5040
        if(data <= 1.1*y and data >= 0.9*y):
            return True
        else:
            return False
    elif(6 <= time and time > 59):
        if(data <= 2530 and data >= 2070):
            return True
        else:
            return False
    elif(time >= 60 and data <= 2530):
        return True
    else:
        return False

def getCurve(profile):
    zero = time.time()
    future = zero + profile
    time.sleep(0.5)
    now = time.time()
    profcurve = []
    #É necessária uma forma de fazer o tempo inicial ser no instante 3s
    #De forma que time.time() - now seja no máximo 3s na primeira iteração
    
    while(now <= future):
        p = getPotLum()
        now = time.time()
        t = now - zero
        profcurve.append((t, p))
    FILE = open('data.txt', 'w')
    for l in profcurve:
        FILE.write(str(l[0])+',')
        FILE.write(str(l[1])+'\n')
    FILE.close()
    return profcurve
