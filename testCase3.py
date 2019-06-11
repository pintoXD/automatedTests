from serialTeste import *
from get_buzzer import *
from get_panel import *



def sceneOne():
    
    '''
    Todos os comandos abaixo descritos devem ser escritos 
    como hexadecimais, mesmo se for um número. Por exemplo,
    a variável timeUp recebe valores inteiros arbritários. 
    Esses inteiros devem ser convertidos pra hexadecimal
    de dois digitos e depois atribuídos a variável. 
    Ex.: 10 (inteiro) -> 0A (hexadecimal)  

    '''
    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    buzzerInfo = []
    ledInfo = []
    

    #Configurar qual botão vai ser apertado
    #######################   Cenario 1   ############################# 

    ####################### Perfil de 10s #############################
    
    timeUp = '0A' # Valor inteiro '10'    
    ### Inicia o perfil de cura. 
    returnSet = set_config(command, buttonPower, timeUp)    
    
    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        ##Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        time.sleep(0.2)  # Dorme por X segundos
        ledInfo = ledInfo + getPanel()

        buzzerInfo = buzzerInfo + getBuzzer()


    else: 
        print("Error on buttonPower configuration")
    


   ####################### Perfil de 20s #############################

    timeUp = '0A'  # Para simular um aperto do botão durante 10s

    ### Configura o perfil de cura ###
    returnSet = set_config(command, buttonArrow, timeUp)
    

    if (returnSet == bytes.fromhex('99' + command + 'FF')):
         # Se a configuração do botão seta der certo, inicia 
         # o perfil de cura   
        print("Button configured")
        auxReturn = set_config(command, buttonPower, timeUp)
        # Esse if aqui verifica seo comando pra iniciar
        # o perfil de cura foi pressionado com sucesso.
        # Se não tiver sido, retorna mensagem de erro.

        if(auxReturn == bytes.fromhex('99' + command + 'FF')):

            # Momento de captar as respostas da placa
            ## Tratar o vetor de tuplas do buzzer
            ### Nesse caso tem de ter duas tuplas

            ledInfo = ledInfo + getPanel()

            time.sleep(200)

            buzzerInfo = buzzerInfo + getBuzzer()

        else:
            print("Error on buttonPower configuration")



    else:
        print("Error on buttonArrow configuration")

 ####################### Perfil de 40s #############################

    timeUp = '0A'  # Para simular um aperto do botão durante 10s

    ### Configura o perfil de cura ###
    returnSet = set_config(command, buttonArrow, timeUp)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):
         # Se a configuração do botão seta der certo, inicia
         # o perfil de cura
        print("Button configured")
        auxReturn = set_config(command, buttonPower, timeUp)
        # Esse if aqui verifica seo comando pra iniciar
        # o perfil de cura foi pressionado com sucesso.
        # Se não tiver sido, retorna mensagem de erro.

        if(auxReturn == bytes.fromhex('99' + command + 'FF')):

            # Momento de captar as respostas da placa
            ## Tratar o vetor de tuplas do buzzer
            ### Nesse caso tem de ter duas tuplas

            ledInfo = ledInfo + getPanel()

            time.sleep(400)

            buzzerInfo = buzzerInfo + getBuzzer()

        else:
            print("Error on buttonPower configuration")

    else:
        print("Error on buttonArrow configuration")

 ####################### Perfil de 60s #############################

    timeUp = '0A'  # Para simular um aperto do botão durante 10s

    ### Configura o perfil de cura ###
    returnSet = set_config(command, buttonArrow, timeUp)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):
         # Se a configuração do botão seta der certo, inicia
         # o perfil de cura
        print("Button configured")
        auxReturn = set_config(command, buttonPower, timeUp)
        # Esse if aqui verifica seo comando pra iniciar
        # o perfil de cura foi pressionado com sucesso.
        # Se não tiver sido, retorna mensagem de erro.

        if(auxReturn == bytes.fromhex('99' + command + 'FF')):

            # Momento de captar as respostas da placa
            ## Tratar o vetor de tuplas do buzzer
            ### Nesse caso tem de ter duas tuplas

            ledInfo = ledInfo + getPanel()

            time.sleep(600)

            buzzerInfo = buzzerInfo + getBuzzer()

        else:
            print("Error on buttonPower configuration")

    else:
        print("Error on buttonArrow configuration")



def sceneTwo():

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    buzzerInfo = []
    ledInfo = []
    

    #Configurar qual botão vai ser apertado
    #######################   Cenario 1   ############################# 

    ####################### Perfil de 10s #############################
    
    timeUp = '0A' # Valor inteiro '10'    
    ### Inicia o perfil de cura. 
    returnSet = set_config(command, buttonPower, timeUp)    
    
    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        ##Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        time.sleep(0.2)  # Dorme por X segundos
        ledInfo = ledInfo + getPanel()

        buzzerInfo = buzzerInfo + getBuzzer()


    else: 
        print("Error on buttonPower configuration")
    




      
      
