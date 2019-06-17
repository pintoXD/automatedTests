from serialTeste import *
from get_buzzer import *
from get_panel import *



def validateLED(ledInfo, ledToken):
    ###### Validação do teste ######
    '''
        Cada configuração de leds acesos produz um número
        em hexadecimal. Esse número deve ser enviado
        na variável ledToken, para comparação. 
        Pra mais informações, olhar a biblioteca.
    
    '''

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


def sceneOne():
    '''    
        Verificar se, depois de nada ser feito durante 3s, os LEDs todos se apagaram e um bipe
        de duração BEEP_TIME_3 segundos.  
    '''    
    command = '01'
    buttonArrow = '11'
    ON_OFF_TIME = '30'
    ARROW_TIME = '10'

     #Aperta o botão seta por ARROW_TIME * 100 milissegundos
    '''
        Esse while serve para apertar o botão seta duas vezes.
        Ele é necessário porque, é preciso verificar se o botão
        foi realmente acionado na placa em teste, a cada vez que
        for acionado. Enquanto ele não for acionado as duas vezes
        necessárias, esse loop não irá parar, contanto que não atinja
        um número limite de repetições.
    '''
    cont = 0
    limit = 0
    
    while cont < 2:

        

        returnSet = set_config(command, buttonArrow, ARROW_TIME)
        if (returnSet == bytes.fromhex('99' + command + 'FF')):
            print("Button configured")
            cont = cont + 1
        else: 
            print("Error on buttonArrow configuration")

        
        limit = limit + 1

        if limit > 15:
            print("Maximum iterations number reached. Button cannot be configured. Breaking loop")
            break

    

    #IF para saber se
    if (cont == 2):

       ### Momento de começar a validação do cenário, procurando ver
       # se os LEDs acesos irão se apagar no tempo determinado, bem como
       #  se o buzzer vai tocar certo.


        print("Button configured")

        '''
           O requisito diz que o após 3 segundos em espera,
           o sistema deve entrar em modo de baixo consumo. 
           Configurei então uma espera de 4 segundos por segurança
        '''    
        
        time.sleep(4)

        buzzerInfo = getBuzzer()
        ledInfo = getPanel()

        validateLED(ledInfo, '00')
        validateBuzzer(buzzerInfo)

 


    else: 
        print("Error on buttonArrow configuration")


    
   


   
 
 




