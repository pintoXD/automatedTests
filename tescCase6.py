from serialTeste import *
from get_buzzer import *
from get_panel import *

'''
def validateLED(ledInfo, ledToken):
    ###### Validação do teste ######
    
         Cada configuração de leds acesos produz um número
        em hexadecimal. Esse número deve ser enviado
        na variável ledToken, para comparação. 
        Pra mais informações, olhar a biblioteca.
    
    

    ## Validação do LED ##

    auxLedValidation = ledInfo

    if(auxLedValidation == ledToken):
        print("Test OK. Correct LED turned on")
    else:
        print("Test failed. Incorrect LED turned on")


def validateBuzzer(buzzerInfo):
    ## Validação do buzzer ##

    auxBuzzerValidation = buzzerInfo

    #Tempo de buzzer ligado depende da situação

    ##Validação do tempo em alto do buzzer para o caso atual
    buzzHighTime = 100  # Tempo em milissegundos
    # Não sei se a placa me envia os tempos nessa ordem não
    # buzzRelativeTime = [10, 20, 40, 60]

    ### Ele recebe uma tupla, no qual a primeira posição é o
    ### valor do tempo em alto que o buzzer passou
    if(auxBuzzerValidation[0] == buzzHighTime):
            print("Buzzer high time complies the specification for this case.")
    else:
            print("Buzzer high time does not comply the specification")
'''




def sceneOne():
    '''    
       Verificar se, depois de o processo de análise da carga de bateria, os LEDs
       todos irão se apagar depois de 3s.

    '''
    command = '01'
    buttonPower = '12'
    ON_OFF_TIME = '30'

    #Aperta o botão power por ON_OFF_TIME * 100 milissegundos

    returnSet = set_config(command, buttonPower, ON_OFF_TIME)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):

        print("Button configured")

        cont = 0
        ledInfoOld = getPanel()
        '''
            Esse while conta o número de mudanças na leitura dos leds.
            Cada leitura vai ser efetuada a cada 100ms.
            Como o tempo total do led piscando vai ser de 50000ms, com 500ms
            de tempo em alto ou em baixo, deve ser notado 5 mudanças de estado.

            Como a leitura dos leds será realizada a cada 100ms, dentro do período
            de 500ms, pelo menos 3 leituras serão realizadas. 

            Dentre essas 3 leituras, pelo menos uma delas vai ser diferente das demais, caracterizando
            assim, uma mudança de estados.

            Dessa forma, se pelo menos 1 mudança for notada, ao fim de 5000ms, teremos pelo menos 5 mudanças
            percebidas.

        '''    
        while cont < 5:
            ledInfo = getPanel()
            
            if(ledInfo != ledInfoOld):
                cont = cont + 1
                ledInfoOld = ledInfo
                    
            
            time.sleep(0.25)    


    ########### TO DO #############
    #### Validate the test
