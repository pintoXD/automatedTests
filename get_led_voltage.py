from serialTeste import set_config, get_value
import time
def getPotLum():
    adc_value = get_value('04')

    if(adc_value[0:2] == '99'):
        adc_value = adc_value[2:]
    else:
        return 'error: message has no ACK'
    if(adc_value[0:2] == '04'):
        adc_value = adc_value[2:]
    else:
        return 'error: response to unrequired command'
    if(adc_value[len(adc_value)-2:] == 'ff'):
        adc_value = adc_value[:len(adc_value)-2]
    else:
        return 'error: message has no FIN'

    adc_value = int(adc_value, 16)
    if(adc_value <= 450):
        return 0
    else:
        # pot_lum = 1.794477785e-23*pow(adc_value, 8) - 2.710712994e-19*pow(adc_value, 7) + \
        #     1.702597885e-15*pow(adc_value, 6) - 5.762038572e-12*pow(adc_value, 5) + \
        #     1.14039482e-8*pow(adc_value, 4) - 1.34384905e-5*pow(adc_value, 3) + \
        #     9.132915482e-3*pow(adc_value, 2) - 2.824372903*adc_value + 422.2915764
        return adc_value