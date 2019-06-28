import time
from get_led_voltage import getPotLum

def mask10(data, time):
    if(0 < time and time < 3):
        if( data <= 1250 and data >= 950):
            return True
        else:
            return False
    if(3 <= time and time > 6):
        y = (-500/3)*time + 1600
        if(data <= y+150 and y >= y-150):
            return True
        else:
            return False
    if(6 <= time and time > 10):
        if(data <= 750 and data >= 450):
            return True
        else:
            return False
    if(time >= 10 and data != 0):
        return False

def mask20(data, time):
    if(0 <= time and time < 7):
        y = (1033/7)*time
        if(data <= (y+150) and data >= (y-150)):
            print('entrou')
            return True
        else:
            return False

    elif(7 <= time and time < 10):
        if( data <= 1250 and data >= 950):
            return True
        else:
            return False

    elif(10 <= time and time < 13):
        y = (-320/3)*time + 1740
        if(data <= y+150 and data >= y-150):
            return True
        else:
            return False

    elif(13 <= time and time < 20):
        if(data <= 850 and data >= 550):
            return True
        else:
            return False

    elif(time >= 20 and data != 0):
        return False
    else:
        return False

def mask40(data, time):
    if(0 <= time and time > 7):
        y = (1100/7)*time
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

    if(13 <= time and time > 40):
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
    if(6 <= time and time > 60):
        if(data <= 750 and data >= 450):
            return True
        else:
            return False
    if(time >= 60 and data != 0):
        return False

def maskSelect(profile):
    now = time.time()
    future = now + profile
    if(profile == 10):
        while(now < future):
            if(mask10(getPotLum(), (time.time() - now + 3))):
                continue
            else:
                return False
        return True
    elif(profile == future):
        while(now < future):
            data = getPotLum()
            if(mask20(data, (time.time() - now + 3))):
                now = time.time()
            else:
                return False
        return True
    elif(profile == 40):
        while(now < future):
            if(mask40(getPotLum(), (time.time() - now + 3))):
                continue
            else:
                return False
        return True
    elif(profile == 60):
        while(now < future):
            if(mask60(getPotLum(), (time.time() - now + 3))):
                continue
            else:
                return False
