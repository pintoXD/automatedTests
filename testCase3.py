from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
from get_batlvl import *
import time
import random
import os
import datetime



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




    auxReturn = []
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
                        print("PS1  from Scene is OK")

                        auxReturn = auxReturn + [True]


                    else:
                        print("Buzzer count incorrect")
                        auxReturn = auxReturn + [False]

                else:
                        print("Second power press failed")
                        auxReturn = auxReturn + [False]

            else:
                print("First power press failed")
                auxReturn = auxReturn + [False]

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

                        auxReturn = auxReturn + [True]

                    else:
                        print("Buzzer bips count in cure profile isn't ok")
                        print("Number of bipes expected: ",
                              1 + (profileCureTime/10) + 1)
                        print("Number of bipes got: ", len(auxBuzzer))
                        auxReturn = auxReturn + [False]

            else:

                print("Power press from second PS failed")
                auxReturn = auxReturn + [False]

        else:
            print("System in low-power consumption. Scenario cannot be tested")
            return False

    else:
        print("Profile time not allowed")
        return False

    return (auxReturn[0] and auxReturn[1])


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


    now = datetime.datetime.now()

    #Configurar qual botão vai ser apertado
    #########################################   Cenario 1   ###############################################
    auxReturn = []
    with open('output_TC3_SONE.txt', 'a') as scenario:



        print("############ INIT #############", file=scenario)

        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=scenario)

        auxReturn = auxReturn + [profile(10)]

        print("Return form profile 10s: ", auxReturn[0], file=scenario)

        auxReturn = auxReturn + [profile(20)]

        print("Return form profile 20s: ", auxReturn[1], file=scenario)

        auxReturn = auxReturn + [profile(40)]
        
        print("Return form profile 40s: ", auxReturn[2], file=scenario)

        auxReturn = auxReturn + [profile(60)]
    
        print("Return form profile 60s: ", auxReturn[3], file=scenario)


        print("############ END #############", file=scenario)

    scenario.close()


    return (auxReturn[0] and auxReturn[1] and auxReturn[2] and auxReturn[3])
     
def sceneTwo():
    auxReturn = []

    now = datetime.datetime.now()

    with open('output_TC3_STWO.txt', 'a') as scenario:
        
        
        print("############ INIT #############", file=scenario)
        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=scenario)

        time.sleep(5.1)

        auxReturn = auxReturn + [psOneSceneTwo()]

        print("Return from psOneSceneTwo: ", auxReturn[0], file=scenario)

        time.sleep(5.1)

        auxReturn = auxReturn + [psTwoSceneTwo()]

        print("Return from psTwoSceneTwo: ", auxReturn[1], file=scenario)

        time.sleep(5.1)

        auxReturn = auxReturn + [psThreeSceneTwo()]

        print("Return from psThreeSceneTwo: ", auxReturn[2], file=scenario)

        print("############ END #############", file=scenario)

    scenario.close()


    return (auxReturn[0] and auxReturn [1] and auxReturn[2])


def psOneSceneTwo():
    ####################### Checar comportamento botão SETA #############################
    
    ledInfoBefore = getCureProfileTime()

    time.sleep(3.2)


    ledInfoAfter = getCureProfileTime()

    time.sleep(0.2)

    print("ledInfoBefore - after = ", ledInfoAfter - ledInfoBefore)

    if ((ledInfoAfter - ledInfoBefore == 20) or
        (ledInfoAfter - ledInfoBefore == 10)   or     
        (ledInfoAfter - ledInfoBefore == -50)):


        print("First PS from scenario 2 is ok")
        return True


    else:


        print("First PS from scenario 2 isn't ok")
        return False


   
def psTwoSceneTwo():
 ####################### Botão Power Pressionado < ON_OFF_TIME segundos #############################     
    #ON_OFF_TIME é de 2 segundos
    pressTime = '02'  # Vai multiplicar por 100mS #Menor que ON_OFF_TIME
    command = '01'
    buttonPower = '12'
    # ON_OFF_TIME_LOCAL = '01'

    # auxPotLum = getPotLum()

    # auxPotLum = int(auxPotLum, 16)

    if(getPotLum() > 0):
        #SE o led de cura tiver ligado, desligar ele antes
        print("Cure on. Shutting down.")
        set_config(command, buttonPower, pressTime)
        time.sleep(1)


    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        time.sleep(5)
        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        # auxPotLum = getPotLum()

        # auxPotLum = int(auxPotLum, 16)

        if(getPotLum() > 0):
            print("PS Two from scenario two is ok")
            
            set_config(command, buttonPower, pressTime)

            return True    



        else:
            print("PS Two from scenario two isn't ok")
            return False
    
    
    else:
        print("psTwoSceneTwo got an error.")
        print("Error on buttonPower configuration.")
        return False

def psThreeSceneTwo():

    # time.sleep

    
  ####################### Botão Power Pressionado > ON_OFF_TIME segundos #############################
  
    pressTime = '1E'  # Valor inteiro '10'
    command = '01'
    buttonPower = '12'



    ON_OFF_TIME_LOCAL = '05'  # Valor inteiro '5'

    # Pressiona o botão por 10 * 100ms
    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        time.sleep(3)
        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")
        limiar = 6
        ledInfoOld = getPanel()
        cont = 0
        control = 0
        ledInfo = ledInfoOld

        #Esse while conta as variações nos leds do painel.
        #Se tiver mais de 5 variações dos leds, ele entende que a bateria tá sendo lida direitinho.
        while(cont < limiar):
          ledInfo = getPanel()
        #   print("Led info inside: ", ledInfo)
        #   print("ledInfoOld inside: ", ledInfoOld)
          if((ledInfo == [1, 1, 1, 1]) or (ledInfo == [0, 1, 1, 1]) or (ledInfo == [0, 0, 1, 1]) or (ledInfo == [0, 0, 0, 1]) or (ledInfo == [0, 0, 0, 0])):
                if(ledInfo != ledInfoOld):
                    ledInfoOld = ledInfo
         
                    ledInfo = getPanel()  
                    cont = cont + 1
            
          if(control >= 70):
              print("Cannot read the led pannel properly.\n PS 3 from Scenario two failed.")
              return False
            #   break

          time.sleep(0.05) 
        
          control = control + 1

        #   print("Control: ", control)

        if(cont >= limiar):
            # if(ledInfo == [1, 1, 1, 1] or ledInfo == [0, 1, 1, 1] or 
            #    ledInfo == [0, 0, 1, 1] or ledInfo == [0, 0, 0, 1]):
            print("PS three from scenario two is ok")
            print("Battery level test ok.")
            return True
        
        else:
            print("PS three from scenario two isn't ok")
            print("Battery level test find an error")
            return False





    else:
        print("Error on buttonPower configuration")
        return False



def main():

    print("Hello World!")
    totalRound = 50

    # for i in range(10):
    #     print("Rodada:", i)
    #     sceneTwo()
    #     time.sleep(1)


#   sceneOne()
    # sceneTwo()
    # psOneSceneTwo()
    # psTwoSceneTwo()
    # time.sleep(4)
    # psThreeSceneTwo()
#   sceneThree()
  #sceneFour()
  #   for i in range(50):
  #     print(i)
  #     sceneTwo()
  #     time.sleep(1)


    now = datetime.datetime.now()
    with open('output_TC3.txt', 'a') as f: 
                index = 1
        # for index in range(2):

                cont = 0
                initialTime = time.time()
                for i in range(totalRound):
                        print("Round ", i)
                        if(index == 0):
                            print("Scene One choosen")
                            aux = sceneOne()
                        elif(index == 1):
                            print("Scene Two choosen")
                            aux = sceneTwo()
                        if(aux):
                            cont = cont + 1
                        
                        time.sleep(1)

                print("############# INIT #############\n\n", file=f)

                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Successful tests percentage: ", (cont/50)*100)

                print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100)

                print("Elapsed time: ", time.time() - initialTime)



                
                print("Scene", index + 1 ,":", file=f)

                print("Successful tests percentage: ", (cont/50)*100, file=f)

                print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100, file=f)

                print("Elapsed time: ", time.time() - initialTime, file = f)

                print("\n\n############# END #############\n\n", file=f)


    f.close()







if __name__ == "__main__":
  main()
