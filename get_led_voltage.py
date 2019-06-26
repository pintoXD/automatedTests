from serialTeste import set_config, get_value

def getPotLum():
    voltg = get_value('04')

    if(voltg[0:2] == '99'):
        voltg = voltg[2:]
    else:
        return 'error: message has no ACK'
    if(voltg[0:2] == '04'):
        voltg = voltg[2:]
        print('responding to command 0x04')
    else:
        return 'error: response to unrequired command'
    if(voltg[len(voltg)-2:] == 'ff'):
        voltg = voltg[:len(voltg)-2]
    else:
        return 'error: message has no FIN'

    voltg = int(voltg, 16)

    if(voltg <= 300):
        return 0
    else:
        return 1.794477785e-23*pow(voltg, 8) - 2.710712994e-19*pow(voltg, 7) + \
        1.702597885e-15*pow(voltg, 6) - 5.762038572e-12*pow(voltg, 5) + \
        1.14039482e-8*pow(voltg, 4) - 1.34384905e-5*pow(voltg, 3) + \
         9.132915482e-3*pow(voltg, 2) - 2.824372903*voltg + 422.2915764

