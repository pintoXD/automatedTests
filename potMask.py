import time
from get_led_voltage import getPotLum

def mask10(data, time):
    if(0 < time and time < 3):
        if( data <= 1250 and data >= 950):
            return True
        else:
            return False
    elif(3 <= time and time < 6):
        y = (-288/3)*time + 1356
        if(data <= y+150 and data >= y-150):
            return True
        else:
            return False
    elif(6 <= time and time < 9.7):
        if(data <= 750 and data >= 550):
            return True
        else:
            return False
    elif(time >= 9.7 and data != 0):
        return False
    else:
        return False

def mask20(data, time):
    if(0 <= time and time < 7):
        y = 1.29463663*time**3  - 50.33672491*time**2 + 561.04598579*time -641.45642991
        if(data <= (y+150) and data >= (y-150)):
            return True
        else:
            return False

    elif(7 <= time and time < 10):
        if( data <= 1250 and data >= 950):
            return True
        else:
            return False

    elif(10 <= time and time < 13):
        y = (-288/3)*time + 1356
        if(data <= y+150 and data >= y-150):
            return True
        else:
            return False

    elif(13 <= time and time < 19.7):
        if(data <= 750 and data >= 550):
            return True
        else:
            return False

    elif(time >= 20 and data != 0):
        return False
    else:
        return False

def mask40(data, time):
    if(0 <= time and time > 7):
        y = 203.0051115649151895*time - 74.7630227525785544
        if(data <= y+150 and y >= y-150):
            return True
        else:
            return False

    if(7 <= time and time < 10):
        if( data <= 1250 and data >= 950):
            return True
        else:
            return False

    if(10 <= time and time > 13):
        y = (-320/3)*time + 1740
        if(data <= y+150 and y >= y-150):
            return True
        else:
            return False

    if(13 <= time and time > 39.7):
        if(data <= 750 and data >= 450):
            return True
        else:
            return False

    if(time >= 40 and data != 0):
        return False

def mask60(data, time):
    if(0 < time and time < 3):
        if( data <= 1250 and data >= 950):
            return True
        else:
            return False
    if(3 <= time and time > 6):
        y = (-320/3)*time + 1740
        if(data <= y+150 and y >= y-150):
            return True
        else:
            return False
    if(6 <= time and time > 59.7):
        if(data <= 750 and data >= 450):
            return True
        else:
            return False
    if(time >= 60 and data != 0):
        return False

def getCurve(profile):
    zero = time.time()
    future = zero + profile
    time.sleep(3)
    now = time.time()
    profcurve = []
    #É necessária uma forma de fazer o tempo inicial ser no instante 3s
    #De forma que time.time() - now seja no máximo 3s na primeira iteração
    while(now < future):
        profcurve.append((now - zero, getPotLum()))
        now = time.time()
    FILE = open('data.txt', 'w')
    for l in profcurve:
        FILE.write(str(l[0])+',')
        FILE.write(str(l[1])+'\n')
    FILE.close()
    return profcurve