from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
from get_batlvl import *



def validateLED(ledInfo, ledToken):
    ###### Validação do teste ######

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
    buzzRelativeTime = [10, 20, 40, 60]

    for i in range(len(buzzerInfo)):

        if(auxBuzzerValidation[i][0] == buzzHighTime):
            print("Buzzer high time complies the specification for this case.")
        else:
            print("Buzzer high time does not comply the specification")

        ##Validação do tempo relativo do buzzer para o caso atual

        if(auxBuzzerValidation[i][1] == buzzRelativeTime):
            print("Relative time complies the specification")

        else:
            print("Relative time does not comply the specifitation")


def getCureProfileTime():

    command = '01'
    buttonArrow = '11'
    pressTime = '02'  # 10 em hexadecimal
    ##Botão passará 10 * 100 milissegundos pressionado

    returnSet = set_config(command, buttonArrow, pressTime)

    time.sleep(0.3)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

            aux = getPanel()

            if(aux == [0, 0, 0, 1]):
                return 60
            elif(aux == [0, 0, 1, 0]):
                return 40
            elif(aux == [0, 1, 0, 0]):
                return 20
            elif(aux == [1, 0, 0, 0]):
                return 10
            else:
                return 99

                #Se o botão for corretamente acionado
                # verifica se a potência do LED caiu a 0 e trata caso não haja.

    else:
      print("Error on buttonArrow configuration")


def sceneOne():
    
    '''
    Todos os comandos abaixo descritos devem ser escritos 
    como hexadecimais, mesmo se for um número. Por exemplo,
    a variável ON_OFF_TIME recebe valores inteiros arbritários. 
    Esses inteiros devem ser convertidos pra hexadecimal
    de dois digitos e depois atribuídos a variável. 
    Ex.: 10 (inteiro) -> 0A (hexadecimal)  

    '''
    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    buzzerInfo = []
    ledInfo = []
    ON_OFF_TIME = '01'  # Valor inteiro '10'

    #Configurar qual botão vai ser apertado
    #########################################   Cenario 1   ###############################################
def profile10():
    ####################### Perfil de 10s #############################

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    buzzerInfo = []
    ledInfo = []
    pressTime = '02'  # Valor inteiro '10'
    
    VBAT_MIN = 2420
    ##Verifica se o sistema está em baixo consumo antes

    if(getBatLvl() >= VBAT_MIN): 
        ### Inicia o perfil de cura. 
        
        
        returnSet = set_config(command, buttonPower, pressTime)
        #Aperta o botão de power duas vezes para ligar e desligar o perfil de cura.
        #Dessa forma o vetor dos tempos do buffer vai ser esvaziado.
        if (returnSet == bytes.fromhex('99' + command + 'FF')):
            #Esse primeiro if serve só pra configurar o perfil de cura desejado e depois verificar
            #se os buzzer e painel de led tão sendo acionados conforme as especificações.
        
            time.sleep(0.5)
            returnSet = set_config(command, buttonPower, pressTime)

            if (returnSet == bytes.fromhex('99' + command + 'FF')):

                profileCureTime = 0

                auxCont = 0
                #procura pelo perfil de cura desejado
                #nesse caso, vai atrás do perfil de 10s
                #A função de procura já valida o acendimento do led de 10s no painel de LEDs
                while(profileCureTime != 10):
                    auxCont = auxCont + 1
                    profileCureTime = getCureProfileTime()

                time.sleep(3)
                auxBuzzer = getBuzzer()

                if(len(auxBuzzer) == (2 + auxCont + 1)):

                    print("Buzzer count correct")


                else:
                    print("Buzzer count incorrect")



            else:
                    print("Second power press failed")

        else:
               print("First power press failed")

    
        
        returnSet = set_config(command, buttonPower, pressTime)
        #Aperta o botão de power duas vezes para ligar e desligar o perfil de cura.
        #Dessa forma o vetor dos tempos do buffer vai ser esvaziado.
        if (returnSet == bytes.fromhex('99' + command + 'FF')):
            time.sleep(0.2)    
            if(getPotLum != 0):

                time.sleep(profileCureTime + 5)

                auxBuzzer = getBuzzer()

                if(len(auxBuzzer) == (1 + (profileCureTime/10) + 1)):
                    print("Buzzer bips count in cure profile is ok")
                    print("Profile Analyzed: ", profileCureTime)
                    print("Number of bipes expected: ", 1 + (profileCureTime/10) + 1)
                    print("Number of got bipes: ", len(auxBuzzer))
                    
                else:
                    print("Buzzer bips count in cure profile isn't ok")
                    print("Number of bipes expected: ", 1 + (profileCureTime/10) + 1)
                    print("Number of bipes got: ", len(auxBuzzer))





        else:    

            print("Power press from second PS failed")

    else:
        print("System in low-power consuptiion. Scenario cannot be tested")

        
'''       
    #########################################################################   
    def profile20():
        ####################### Perfil de 20s #############################
        command = '01'
        buttonArrow = '11'
        buttonPower = '12'
        buzzerInfo = []
        ledInfo = []
        ON_OFF_TIME = '01'  # Valor inteiro '10'
            ### Configura o perfil de cura ###
        
        
        returnSet = set_config(command, buttonArrow, ON_OFF_TIME)
            

        if (returnSet == bytes.fromhex('99' + command + 'FF')):
            # Se a configuração do botão seta der certo, inicia 
            # o perfil de cura   
            print("Button configured")
            auxReturn = set_config(command, buttonPower, ON_OFF_TIME)
            # Esse if aqui verifica seo comando pra iniciar
            # o perfil de cura foi pressionado com sucesso.
            # Se não tiver sido, retorna mensagem de erro.

            if(auxReturn == bytes.fromhex('99' + command + 'FF')):

                # Momento de captar as respostas da placa
                ## Tratar o vetor de tuplas do buzzer
                ### Nesse caso tem de ter duas tuplas

                ledInfo = ledInfo + getPanel()

                time.sleep(20)

                buzzerInfo = buzzerInfo + getBuzzer()

            else:
                print("Error on buttonPower configuration")



        else:
            print("Error on buttonArrow configuration")






        #########################################################################
    def profile40():
        ####################### Perfil de 40s #############################
        command = '01'
        buttonArrow = '11'
        buttonPower = '12'
        buzzerInfo = []
        ledInfo = []
        ON_OFF_TIME = '01'  # Valor inteiro '10'
        
            ### Configura o perfil de cura ###
        returnSet = set_config(command, buttonArrow, ON_OFF_TIME)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):
            # Se a configuração do botão seta der certo, inicia
            # o perfil de cura
            print("Button configured")
            auxReturn = set_config(command, buttonPower, ON_OFF_TIME)
            # Esse if aqui verifica seo comando pra iniciar
            # o perfil de cura foi pressionado com sucesso.
            # Se não tiver sido, retorna mensagem de erro.

            if(auxReturn == bytes.fromhex('99' + command + 'FF')):

                # Momento de captar as respostas da placa
                ## Tratar o vetor de tuplas do buzzer
                ### Nesse caso tem de ter duas tuplas

                ledInfo = ledInfo + getPanel()

                time.sleep(40)

                buzzerInfo = buzzerInfo + getBuzzer()

            else:
                print("Error on buttonPower configuration")

        else:
            
            print("Error on buttonArrow configuration")

        
    


        #########################################################################
    def profile60():
    ####################### Perfil de 60s #############################
    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    buzzerInfo = []
    ledInfo = []
    ON_OFF_TIME = '01'  # Valor inteiro '10'
        ### Configura o perfil de cura ###
    returnSet = set_config(command, buttonArrow, ON_OFF_TIME)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):
        # Se a configuração do botão seta der certo, inicia
        # o perfil de cura
        print("Button configured")
        auxReturn = set_config(command, buttonPower, ON_OFF_TIME)
        # Esse if aqui verifica seo comando pra iniciar
        # o perfil de cura foi pressionado com sucesso.
        # Se não tiver sido, retorna mensagem de erro.

        if(auxReturn == bytes.fromhex('99' + command + 'FF')):

            # Momento de captar as respostas da placa
            ## Tratar o vetor de tuplas do buzzer
            ### Nesse caso tem de ter duas tuplas

            ledInfo = ledInfo + getPanel()

            time.sleep(60)

            buzzerInfo = buzzerInfo + getBuzzer()

        else:
            print("Error on buttonPower configuration")

    else:
        print("Error on buttonArrow configuration")
'''

  

    # else:
    #     print("System in low-power consuptiion. Scenario cannot be tested")

       

 #########################################################################


def sceneTwo():

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    
    

    #Configurar qual botão vai ser apertado
    ###########################################   Cenario 2   ##################################################

    ####################### Checar comportamento botão SETA #############################

    '''
            Pra esse caso do cenário, deve ser analisado se algum LED
            de perfil de cura foi acendido.

    '''
    
    ON_OFF_TIME = '02' # Valor inteiro '10'   
    ledInfoBefore = '' 
    ledInfoAfter = ''
    
    ledInfoBefore = getPanel()

    returnSet = set_config(command, buttonArrow, ON_OFF_TIME)  #Pressiona o botão por 10 * 100ms 
    
    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        ##Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        time.sleep(0.2)  # Dorme por X segundos

        ledInfoAfter = getPanel()

        


    else: 
        print("Error on buttonPower configuration")
    


    '''

        Precisa verificar qual o perfil de cura que vai ser iniciado. 
        Então precisa pegar o estado dos leds antes de apertar o botão seta.



    '''
    indexBefore = ''
    indexAfter = ''



    for i in range(len(ledInfoAfter)):
        
        if ledInfoBefore[i] == '1':
        
            indexBefore = i
        
        if ledInfoAfter[i] == '1':
        
            indexAfter = i
 
    if(indexAfter - indexBefore == 1) or (indexBefore - indexAfter == 3):
        print("Teste ok")
        



      
 ####################### Botão Power Pressionado < ON_OFF_TIME segundos #############################     
 # Falta implementar
   #
    ON_OFF_TIME_LOCAL = '01'

    returnSet = set_config(command, buttonPower, ON_OFF_TIME_LOCAL)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        ledInfo = getPanel()

    else:
        print("Error on buttonPower configuration")

    if(getPotLum() > 0):
        print("Battery level test ok.")
        print("Current Level: ", ledInfo)
    else:
        print("Battery level test find an error")




 ####################### Botão Power Pressionado > ON_OFF_TIME segundos #############################
  
    ON_OFF_TIME_LOCAL = '05'  # Valor inteiro '5'

    # Pressiona o botão por 10 * 100ms
    returnSet = set_config(command, buttonPower, ON_OFF_TIME_LOCAL)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        ledInfo = getPanel()

    else:
        print("Error on buttonPower configuration")


    if(ledInfo == '03' or ledInfo == '07' or ledInfo == '0f'):
        print("Battery level test ok.")
        print("Current Level: ", ledInfo)
    else:
        print("Battery level test find an error")
