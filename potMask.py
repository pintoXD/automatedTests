import time

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
        y = (-500/3)*time + 1600
        if(data <= y+150 and y >= y-150):
            return True
        else:
            return False

    if(13 <= time and time > 20):
        if(data <= 750 and data >= 450):
            return True
        else:
            return False

    if(time >= 20 and data != 0):
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
        y = (-500/3)*time + 1600
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
        y = (-500/3)*time + 1600
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