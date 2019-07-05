from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
from get_batlvl import *



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


def profile(desiredCureProfile):
    ####################### Perfil de 10s #############################

    # desiredCureProfile deve ser os valores 10, 20, 40 ou 60

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    buzzerInfo = []
    ledInfo = []
    pressTime = '02'  # Valor inteiro '10'

    VBAT_MIN = 2420

    ##Verifica se o sistema está com a carga mínima
    if(desiredCureProfile == 10 or desiredCureProfile == 20 or
       desiredCureProfile == 40 or desiredCureProfile == 60):

        if(getBatLvl() > VBAT_MIN):
            ### Inicia o perfil de cura.

            returnSet = set_config(command, buttonPower, pressTime)
            #Aperta o botão de power duas vezes para ligar e desligar o perfil de cura.
            #Dessa forma o vetor dos tempos do buffer vai ser esvaziado.
            if (returnSet == bytes.fromhex('99' + command + 'FF')):
                #Esse primeiro if serve só pra configurar o perfil de cura desejado e depois verificar
                #se os buzzer e painel de led tão sendo acionados conforme as especificações.

                time.sleep(0.5)

                buzzerFirstPress = getBuzzer()

                print("buzzerFirstPress is: ", buzzerFirstPress)
                print("Length is: ", len(buzzerFirstPress))

                returnSet = set_config(command, buttonPower, pressTime)
                time.sleep(0.5)

                if (returnSet == bytes.fromhex('99' + command + 'FF')):

                    profileCureTime = 0

                    auxCont = 0
                    #procura pelo perfil de cura desejado
                    #nesse caso, vai atrás do perfil de 10s
                    #A função de procura já valida o acendimento do led de 10s no painel de LEDs
                    while(profileCureTime != desiredCureProfile):
                        profileCureTime = getCureProfileTime()
                        auxCont = auxCont + 1

                    time.sleep(3)
                    auxBuzzer = getBuzzer()

                    print("Current buzzer count: ", auxCont)
                    print("Current buzzer length: ", auxBuzzer)
                    ##A contagem  é 2 + auxCont - 1 + 1 porque
                    #2 seriam os bipes de pressionar o botão power pra ligar e desligar o perfil de cura,
                    #auxCont é as vezes que o botão seta foi pressionado, -1 é uma correção pois o bipe do botão
                    #de power quando pressionado no início de perfil de cura é perdido e o 1 é o bipe que indica
                    #a entrada no modo de baixo consumo.

                    if(len(auxBuzzer) == (2 + auxCont - 1 + 1)) and len(buzzerFirstPress) > 0:

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
                        print("Number of bipes expected: ",
                              1 + (profileCureTime/10) + 1)
                        print("Number of got bipes: ", len(auxBuzzer))

                    else:
                        print("Buzzer bips count in cure profile isn't ok")
                        print("Number of bipes expected: ",
                              1 + (profileCureTime/10) + 1)
                        print("Number of bipes got: ", len(auxBuzzer))

            else:

                print("Power press from second PS failed")

        else:
            print("System in low-power consuptiion. Scenario cannot be tested")

    else:
        print("Profile time not allowed")










def sceneOne():
    
    '''
    Todos os comandos abaixo descritos devem ser escritos 
    como hexadecimais, mesmo se for um número. Por exemplo,
    a variável ON_OFF_TIME recebe valores inteiros arbritários. 
    Esses inteiros devem ser convertidos pra hexadecimal
    de dois digitos e depois atribuídos a variável. 
    Ex.: 10 (inteiro) -> 0A (hexadecimal)  

    '''
    # command = '01'
    # buttonArrow = '11'
    # buttonPower = '12'
    # buzzerInfo = []
    # ledInfo = []
    # ON_OFF_TIME = '01'  # Valor inteiro '10'

    #Configurar qual botão vai ser apertado
    #########################################   Cenario 1   ###############################################

    profile(60)


     
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


def sceneTwo():
    # psOneSceneTwo()
    # psTwoSceneTwo()
    psThreeSceneTwo()




def psOneSceneTwo():
    ####################### Checar comportamento botão SETA #############################
    
    ledInfoBefore = getCureProfileTime()

    time.sleep(3.2)


    ledInfoAfter = getCureProfileTime()

    print("ledInfoBefore - after = ", ledInfoAfter - ledInfoBefore)

    if ((ledInfoAfter - ledInfoBefore == 20) or
        (ledInfoAfter - ledInfoBefore == 10)   or     
        (ledInfoBefore - ledInfoAfter == -50)):


        print("First PS from scenario 2 is ok")


    else:


        print("First PS from scenario 2 isn't ok")


   
def psTwoSceneTwo():
 ####################### Botão Power Pressionado < ON_OFF_TIME segundos #############################     
    #ON_OFF_TIME é de 2 segundos
    pressTime = '02'  # Vai multiplicar por 100mS #Menor que ON_OFF_TIME
    command = '01'
    buttonPower = '12'
    # ON_OFF_TIME_LOCAL = '01'

    if(getPotLum() > 0):
        #SE o led de cura tiver ligado, desligar ele antes
        set_config(command, buttonPower, pressTime)


    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

       

        if(getPotLum() > 0):
            print("PS Two from scenario two is ok")

            set_config(command, buttonPower, pressTime)



        else:
            print("PS Two from scenario two isn't ok")
    
    
    else:
        print("psTwoSceneTwo got an error.")
        print("Error on buttonPower configuration.")


def psThreeSceneTwo():




  ####################### Botão Power Pressionado > ON_OFF_TIME segundos #############################
  
    pressTime = '1E'  # Valor inteiro '10'
    command = '01'
    buttonPower = '12'



    ON_OFF_TIME_LOCAL = '05'  # Valor inteiro '5'

    # Pressiona o botão por 10 * 100ms
    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")
        time.sleep(3.2)

        ledInfo= getPanel()
        cont = 0
        # ledInfo = ledInfoOld

        #Esse while conta as variações nos leds do painel.
        #Se tiver mais de 5 variações dos leds, ele entende que a bateria tá sendo lida direitinho.
        while(cont < 5):
          aux = getPanel()  

          if(aux != ledInfo):
         
            ledInfo = getPanel()  
            cont = cont + 1
            time.sleep(0.1) 
          
          if(cont == 10):
              cont = 0
              break
        

        if(cont >= 5):
            # if(ledInfo == [1, 1, 1, 1] or ledInfo == [0, 1, 1, 1] or 
            #    ledInfo == [0, 0, 1, 1] or ledInfo == [0, 0, 0, 1]):
            print("PS three from scenario two is ok")
            print("Battery level test ok.")
            
        else:
            print("PS three from scenario two isn't ok")
            print("Battery level test find an error")





    else:
        print("Error on buttonPower configuration")



def main():

  print("Hello World!")

  sceneOne()
#   sceneTwo()
#   sceneThree()
#   sceneFour()
  #   for i in range(50):
  #     print(i)
  #     sceneTwo()
  #     time.sleep(1)


if __name__ == "__main__":
  main()
