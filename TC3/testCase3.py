from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_led_voltage import *
from get_batlvl import *
import time
import random
import os
import datetime
import statistics


rodada = 0
iteration = 0

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
    profileCureTime = 0
    auxPotLum = ''
    auxMeanPotLum = []

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

                time.sleep(0.3)



                # auxPotLum = int(auxPotLum, 16)
                ######### INIT #############
                ##Esse pedaço de código visa garantir que o botão de power vai realmente ser pressionado,
                ##que o perfil de cura vai realmente ser ativado, pra bypassar o bug que há atulamente.

                indexer = 0
                auxPotLum = 0
                auxMeanPotLum = []
                auxContTimes = 0

                while(indexer < 5):
                    print("Inside first while")
                    auxMeanPotLum = auxMeanPotLum + [getPotLum()]
                    # time.sleep(0.05)
                    indexer = indexer + 1

                auxPotLum = statistics.mean(auxMeanPotLum)
                if(auxPotLum < 0):
                    while(auxContTimes < 50):
                        print("Inside second while")
                        if(auxPotLum > 0):
                            break
                        else:
                            set_config(command, buttonPower, pressTime)
                            auxContTimes = auxContTimes + 1
                            time.sleep(2)
                            auxPotLum = getPotLum()

                if(auxContTimes > 0):

                    now = datetime.datetime.now()
                    with open('states_TC3_scene_one.txt', 'a') as f:

                        print("\n############ INIT #############\n", file=f)
                        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                        print("Iterarion: ", iteration, file=f)
                        print("Round: ", rodada, file=f)

                        # print("Error on inside if statement\n", file=f)
                        print(
                            "Part One\nCure LED not turned on. Tried tu turn it on.", file=f)
                        print(
                            "Statement to turn on the LED was called", file=f)
                        print("No. of times the needed to try turn on: ", auxContTimes, file=f)
                        # print("Current control:", control, file=f)
                        # print("Current ledInfoOld", ledInfoOld, file=f)
                        # print("Current ledInfo", ledInfo, file=f)

                        print("\n############ END #############\n", file=f)

                    f.close()

                ######### FIN #############


                buzzerFirstPress = getBuzzer()

                print("buzzerFirstPress is: ", buzzerFirstPress)
                print("Length is: ", len(buzzerFirstPress))

                returnSet = set_config(command, buttonPower, pressTime)
                time.sleep(0.5)

                if (returnSet == bytes.fromhex('99' + command + 'FF')):

                    ######### INIT #############
                    ##Esse pedaço de código visa garantir que o botão de power vai realmente ser pressionado,
                    ##que o perfil de cura vai realmente ser desligado, pra bypassar o bug da 
                    # placa de aquisição que há atulamente.

                    indexer = 0
                    auxPotLum = 0
                    auxMeanPotLum = []
                    auxContTimes = 0

                    while(indexer < 3):
                        print("Inside first while to turn off")
                        auxMeanPotLum = auxMeanPotLum + [getPotLum()]
                        # time.sleep(0.05)
                        indexer = indexer + 1

                    auxPotLum = statistics.mean(auxMeanPotLum)
                    if(auxPotLum > 0):
                        while(auxContTimes < 50):
                            print("Inside second while to turn off")
                            if(auxPotLum == 0):
                                break
                            else:
                                set_config(command, buttonPower, pressTime)
                                time.sleep(1)
                                auxPotLum = getPotLum()
                                auxContTimes = auxContTimes + 1
                            
                    if(auxContTimes > 0):

                        now = datetime.datetime.now()
                        with open('states_TC3_scene_one.txt', 'a') as f:

                            print("\n############ INIT #############\n", file=f)
                            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                            print("Iterarion: ", iteration, file=f)
                            print("Round: ", rodada, file=f)

                            
                            print(
                                "Part One\nCure LED not turned off. Tried tu turn it off.", file=f)
                            print(
                                "Statement to turn off the LED was called", file=f)
                            print("No. of times needed to try turn off: ", auxContTimes, file=f)
                            
                            print("\n############ END #############\n", file=f)

                        f.close()
                    

                    ######### FIN #############







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
                        print("Buzzer count incorrect or profile time selection failed")
                        auxReturn = auxReturn + [False]

                        now = datetime.datetime.now()
                        with open('states_TC3_scene_one.txt', 'a') as f:

                            print("############ INIT #############", file=f)
                            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                            print("Iterarion: ", iteration, file=f) 
                            print("Round: ", rodada, file=f) 

                            print("Error inside Profile\n Part One\nChecking buttoArrow beeps \nBuzzer Count Incorrect.", file=f)
                            print("Current buzzer count:",
                                  len(auxBuzzer), file=f)
                            print("Expected buzzer count: ", (2 + auxCont - 1 + 1), file=f)
                            print("Desired cure profile:", desiredCureProfile, file=f)
                            print("Current profile cure time:", profileCureTime, file=f)

                            print("############ END #############", file=f)

                        f.close()






                else:
                        print("Second power press failed")
                        auxReturn = auxReturn + [False]
                        now = datetime.datetime.now()
                        with open('states_TC3_scene_one.txt', 'a') as f:

                            print("############ INIT #############", file=f)
                            print("Date: ", now.strftime(
                                "%Y-%m-%d %H:%M"), file=f)


                            print("Iterarion: ", iteration, file=f)

                            print("Round: ", rodada, file=f) 
                            print("Desired cure profile:",
                                  desiredCureProfile, file=f)
                            print(
                                "Error inside Profile\n Part One\n Second power press failed.", file=f)
                            print("Current returnSet",
                                  returnSet, file=f)
                            # print("Current ledInfoAfter:", ledInfoAfter, file=f)

                            print("############ END #############", file=f)

                        f.close()

            else:
                print("First power press failed")
                auxReturn = auxReturn + [False]
                now = datetime.datetime.now()
                with open('states_TC3_scene_one.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime(
                        "%Y-%m-%d %H:%M"), file=f)
                    print("Iterarion: ", iteration, file=f)
                    print("Round: ", rodada, file=f) 
                    print("Desired cure profile:", desiredCureProfile, file=f)
                    print(
                        "Error inside Profile\nPart One\nFirst power press failed.", file=f)
                    print("Current returnSet",
                            returnSet, file=f)
                    # print("Current ledInfoAfter:", ledInfoAfter, file=f)

                    print("############ END #############", file=f)

                f.close()




            # set_config(command, buttonPower, pressTime)













            #Aqui não precisa apertar o botão de power duas vezes porque só uma vez 
            #já é o suficiente para se limpar o vetor de tempos.             
            
            returnSet = set_config(command, buttonPower, pressTime)
            if (returnSet == bytes.fromhex('99' + command + 'FF')):
                time.sleep(0.5)



                ######### INIT #############
                indexer = 0
                auxPotLum = 0
                auxMeanPotLum = []
                auxContTimes = 0

                while(indexer < 5):
                    print("Inside first while to turn on")
                    auxMeanPotLum = auxMeanPotLum + [getPotLum()]
                    # time.sleep(0.05)
                    indexer = indexer + 1

                auxPotLum = statistics.mean(auxMeanPotLum)

                if(auxPotLum < 0):
                    while(auxContTimes < 50):
                        print("Inside second while to turn on")
                        if(auxPotLum > 0):
                            break
                        else:
                            set_config(command, buttonPower, pressTime)
                            time.sleep(2)
                            auxPotLum = getPotLum()
                            auxContTimes = auxContTimes + 1
                        
                        
                if(auxContTimes > 0):

                    now = datetime.datetime.now()
                    with open('states_TC3_scene_one.txt', 'a') as f:

                        print("\n############ INIT #############\n", file=f)
                        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                        print("Iterarion: ", iteration, file=f)
                        print("Round: ", rodada, file=f)

                        # print("Error on inside if statement\n", file=f)
                        print(
                            "Part One\nCure LED not turned on. Tried tu turn it on.", file=f)
                        print(
                            "Statement to turn on the LED was called", file=f)
                        print("No. of times the needed to try turn on: ", auxContTimes, file=f)
                        # print("Current control:", control, file=f)
                        # print("Current ledInfoOld", ledInfoOld, file=f)
                        # print("Current ledInfo", ledInfo, file=f)

                        print("\n############ END #############\n", file=f)

                    f.close()
            

                ######### FIN #############




                
                if(auxPotLum != 0):

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

                        now = datetime.datetime.now()
                        with open('states_TC3_scene_one.txt', 'a') as f:

                            print("############ INIT #############", file=f)
                            print("Date: ", now.strftime(
                                "%Y-%m-%d %H:%M"), file=f)
                            print("Iterarion: ", iteration, file=f)
                            print("Round: ", rodada, file=f)  
                            print(
                                "Error inside Profile\n Part Two\n Checking profile beeps", file=f)
                            print("Buzzer bips count in cure profile isn't ok", file=f)
                            print("Desired cure profile:",
                                  desiredCureProfile, file=f)
                            print("Current profile cure time: ",(profileCureTime), file=f)
                            
                            print("Number of bipes expected: ",
                                1 + (profileCureTime/10) + 1, file=f)
                            print("Number of bipes got: ", len(auxBuzzer), file=f)

                                # print("Current ledInfoAfter:", ledInfoAfter, file=f)

                            print("############ END #############", file=f)

                        f.close()





                        

            else:

                print("Power press from second PS failed")
                auxReturn = auxReturn + [False]

                now = datetime.datetime.now()
                with open('states_TC3_scene_one.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime(
                        "%Y-%m-%d %H:%M"), file=f)
                    print("Iterarion: ", iteration, file=f)
                    print("Round: ", rodada, file=f)
                    print("Desired cure profile:", desiredCureProfile, file=f)

                    print(
                        "Error inside Profile\n Part Two\n First power press failed.", file=f)
                    print("Current returnSet",
                            returnSet, file=f)
                    # print("Current ledInfoAfter:", ledInfoAfter, file=f)

                    print("############ END #############", file=f)

                f.close()








        else:
            print("System in low-power consumption. Scenario cannot be tested")
            now = datetime.datetime.now()
            with open('states_TC3_scene_one.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime(
                    "%Y-%m-%d %H:%M"), file=f)
                print("Iterarion: ", iteration, file=f) 
                print("Round: ", rodada, file=f)  

                print(
                    "Error inside Profile\n Part Two\n System in low-power consumption. Scenario cannot be tested.\n", file=f)
                # print("Current returnSet",
                #         returnSet, file=f)
                print("Current bat level:", getBatLvl(), file=f)
                print("Current rounded bat voltage:", round(getBatVoltage(), 3), file=f)

                print("############ END #############", file=f)

            f.close()

            return False

    else:
        print("Profile time not allowed")
        now = datetime.datetime.now()
        with open('states_TC3_scene_one.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("Date: ", now.strftime(
                "%Y-%m-%d %H:%M"), file=f)
            print("Iterarion: ", iteration, file=f)
            print("Round: ", rodada, file=f)  
            print("Desired cure profile:", desiredCureProfile, file=f)

            print(
                "Error inside Profile\n Part Two\n Profile time not allowed.\n", file=f)
            # print("Current returnSet",
            #         returnSet, file=f)
            print("Current desiredCureProfile:", desiredCureProfile, file=f)
            # print("Current rounded bat voltage:",
            #         round(getBatVoltage(), 3), file=f)

            print("############ END #############", file=f)

        f.close()
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


    # now = datetime.datetime.now()

    #Configurar qual botão vai ser apertado
    #########################################   Cenario 1   ###############################################
    auxReturn = []
    # with open('output_TC3_SONE.txt', 'a') as scenario:

    auxElapsed = time.time()

    # print("############ INIT #############", file=scenario)

    # print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=scenario)

    auxReturn = auxReturn + [profile(10)]

    time.sleep(2)

    # print("Return form profile 10s: ", auxReturn[0], file=scenario)

    auxReturn = auxReturn + [profile(20)]

    time.sleep(2)

    # print("Return form profile 20s: ", auxReturn[1], file=scenario)

    auxReturn = auxReturn + [profile(40)]

    time.sleep(2)
    
    # print("Return form profile 40s: ", auxReturn[2], file=scenario)

    auxReturn = auxReturn + [profile(60)]

    time.sleep(2)

        # print("Return form profile 60s: ", auxReturn[3], file=scenario)


        # print("############ END #############", file=scenario)

    # scenario.close()

    print("Scene one elapsed time: ", round(time.time() - auxElapsed, 3))


    return (auxReturn[0] and auxReturn[1] and auxReturn[2] and auxReturn[3])
     
def sceneTwo():
        auxReturn = []

        auxNow = time.time()

        now = datetime.datetime.now()

    # with open('output_TC3_STWO.txt', 'a') as scenario:
        
        
        # print("############ INIT #############", file=scenario)
        # print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=scenario)

        time.sleep(5)

        auxReturn = auxReturn + [psOneSceneTwo()]

        # print("Return from psOneSceneTwo: ", auxReturn[0], file=scenario)


        time.sleep(5)

        auxReturn = auxReturn + [psTwoSceneTwo()]

        # print("Return from psTwoSceneTwo: ", auxReturn[1], file=scenario)

        time.sleep(5)

        auxReturn = auxReturn + [psThreeSceneTwo()]

    #     print("Return from psThreeSceneTwo: ", auxReturn[2], file=scenario)

    #     print("############ END #############", file=scenario)

    # scenario.close()
        elapsedAux = time.time() - auxNow

        print("Elapsed time in scene: ", elapsedAux)

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
        now = datetime.datetime.now()
        with open('states_TC3_sceneTwo_PS1.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("PS 1 from Scene 2 get an error.", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
            print("Iterarion: ", iteration, file=f)
            print("Round: ", rodada, file=f)  
            
            print("current ledInfoBefore:", ledInfoBefore, file=f)
            print("Current ledInfoAfter:", ledInfoAfter, file=f )

            print("############ END #############", file=f)


        f.close()



        return False


   
def psTwoSceneTwo():
 ####################### Botão Power Pressionado < ON_OFF_TIME segundos #############################     
    #ON_OFF_TIME é de 2 segundos
    pressTime = '02'  # Vai multiplicar por 100mS #Menor que ON_OFF_TIME
    command = '01'
    buttonPower = '12'
    # ON_OFF_TIME_LOCAL = '01'

    auxPotLum = ''
    auxMeanPotLum = []

    # auxPotLum = int(auxPotLum, 16)

    if(getPotLum() > 0):
        #SE o led de cura tiver ligado, desligar ele antes
        print("Cure on. Shutting down.")
        set_config(command, buttonPower, pressTime)
        time.sleep(1)


    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        time.sleep(1)
        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        indexer = 0

        auxTime = time.time()

        while(indexer < 10):
            auxMeanPotLum = auxMeanPotLum + [getPotLum()]
            # time.sleep(0.05)
            indexer = indexer + 1

        print("Elapsed inside while", time.time() - auxTime)

        auxPotLum = statistics.mean(auxMeanPotLum)
        

        print("Aux pot lum: ", auxPotLum)

        # auxPotLum = int(auxPotLum, 16)

        if(auxPotLum > 0):
            print("PS Two from scenario two is ok")
            
            set_config(command, buttonPower, pressTime)

            return True    



        else:
            print("PS Two from scenario two isn't ok")

            auxMsg=''

            if(getPanel() != [0, 0, 0, 0]):
                auxMsg = "Panel indicates that cure profile maybe activated. Need to check getPotLum()"


            now = datetime.datetime.now()
            with open('states_TC3_scene2_ps2.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                print("Iterarion: ", iteration, file=f)
                print("Round: ", rodada, file=f)  

                print("PS 2 from Scene 2 get an error.", file=f)
                print("Error on inside if statement\n", file=f)
                print(auxMsg, file=f)
                print("current auxPotLum:", auxPotLum, file=f)
                print("Current getPotLum: ", getPotLum(), file=f)
                print("Current returSet:", returnSet, file=f)

                print("############ END #############", file=f)

            if(getPotLum() > 0):
                set_config('01', '12', '02')

            f.close()

            return False
    
    
    else:
        print("psTwoSceneTwo got an error.")
        print("Error on buttonPower configuration.")


        now = datetime.datetime.now()
        with open('states_TC3_scene2_ps2.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("PS 2 from Scene 2 get an error.\n", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
            print("Iterarion: ", iteration, file=f)
            print("Round: ", rodada, file=f)  

            print("Error on pot Lum that checks if cure LED is alerady on.", file=f)
            print("Error on buttonPower configuration.", file=f)
            print("current auxPotLum:", auxPotLum, file=f)
            
           
            print("############ END #############", file=f)

        f.close()

        return False

def psThreeSceneTwo():

    # time.sleep


 ######### Checa se o LED de cura ainda está ligado, por algu motivo, tentando assim o desligar #######

    # auxLedCureOff = validateCureOff()
    auxControl = 0
    while(auxControl <= 50):

        auxLedCureOff = validateCureOff()

        if(auxLedCureOff == True):
            break

        auxControl = auxControl + 1

    if(auxControl > 0):

        now = datetime.datetime.now()
        with open('states_TC3_scene2_ps3.txt', 'a') as f:

            print("\n############ INIT #############\n", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
            print("Iterarion: ", iteration, file=f)
            print("Round: ", rodada, file=f)

            # print("Error on inside if statement\n", file=f)
            print(
                "Cure LED was on. Needed to shutting it dows before start PS3", file=f)
            print(
                "Function to shutdown the LED was called", file=f)
            print("No. of times the function was called: ", auxControl, file=f)
            # print("Current control:", control, file=f)
            # print("Current ledInfoOld", ledInfoOld, file=f)
            # print("Current ledInfo", ledInfo, file=f)

            print("\n############ END #############\n", file=f)

        f.close()


    
  ####################### Botão Power Pressionado > ON_OFF_TIME segundos #############################
  
    pressTime = '14'  # Valor inteiro '10'
    command = '01'
    buttonPower = '12'



    ON_OFF_TIME_LOCAL = '05'  # Valor inteiro '5'

    # Pressiona o botão por 10 * 100ms
    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        time.sleep(2.2)
        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        # print("Button configured")
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
            
          if(control >= 100):
                print("Cannot read the led pannel properly.\n While enters in a deadlock\n PS 3 from Scenario two failed.")


                now = datetime.datetime.now()
                with open('states_TC3_scene2_ps3.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                    print("Iterarion: ", iteration, file=f)
                    print("Round: ", rodada, file=f)  

                    print("PS 3 from Scene 2 get an error.", file=f)
                    # print("Error on inside if statement\n", file=f)
                    print(
                        "Cannot read the led pannel properly.\n While enters in a deadlock\n PS 3 from Scenario two failed.", file=f)

                    print("current returSet:", returnSet, file=f)
                    print("Current variation counter:", cont, file=f)
                    print("Current ledInfoOld", ledInfoOld, file=f)
                    print("Current ledInfo", ledInfo, file=f)

                    print("############ END #############", file=f)

                f.close()



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

            now = datetime.datetime.now()
            with open('states_TC3_scene2_ps3.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("PS 3 from Scene 2 get an error.", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                print("Iterarion: ", iteration, file=f)
                print("Round: ", rodada, file=f)  

                # print("Error on inside if statement\n", file=f)
                print("Battery level test find an error", file=f)
                print("current cont:", cont, file=f)
                print("Current control:", control, file=f)
                print("Current ledInfoOld", ledInfoOld, file=f)
                print("Current ledInfo", ledInfo, file=f)

                print("############ END #############", file=f)


            f.close()



            return False





    else:
        print("Error on buttonPower configuration")

        now = datetime.datetime.now()
        with open('states_TC3_scene2_ps3.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
            print("Iterarion: ", iteration, file=f)
            print("Round: ", rodada, file=f)  

            print("PS 3 from Scene 2 get an error.", file=f)
            # print("Error on inside if statement\n", file=f)
            print("Error on buttonPower configuration", file=f)
            print("current returSet:", returnSet, file=f)
            # print("Current control:", control, file=f)
            # print("Current ledInfoOld", ledInfoOld, file=f)
            # print("Current ledInfo", ledInfo, file=f)

            print("############ END #############", file=f)

        f.close()





        return False




def validateCureOff():


    pressTime = '02'  # Vai multiplicar por 100mS #Menor que ON_OFF_TIME
    command = '01'
    buttonPower = '12'
    # ON_OFF_TIME_LOCAL = '01'

    auxPotLum = ''
    auxMeanPotLum = []

    # auxPotLum = int(auxPotLum, 16)



    indexer = 0
    while(indexer < 5):
        auxMeanPotLum = auxMeanPotLum + [getPotLum()]
        # time.sleep(0.05)
        indexer = indexer + 1

    auxPotLum = statistics.mean(auxMeanPotLum)

    if(auxPotLum > 0):
        #SE o led de cura tiver ligado, desligar ele antes
        print("########### CURE ON ###############")
        print("Cure on. Shutting down.")
        returnSet = set_config(command, buttonPower, pressTime)
        time.sleep(0.8)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            time.sleep(0.8)
            ### Momento de captar as respostas da placa
            #tratar o vetor de tuplas do buzzer
            # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

            print("Button power configured")
            indexer = 0
            while(indexer < 3):
                auxMeanPotLum = auxMeanPotLum + [getPotLum()]
                # time.sleep(0.05)
                indexer = indexer + 1

            auxPotLum = statistics.mean(auxMeanPotLum)


            if(auxPotLum == 0):
                print("OK. Shutdown press was successful. Cure LED turned off.")

                # set_config(command, buttonPower, pressTime)
                return True


            else:
                print("######## ERROR ###############")
                print("Shutdown button was pressed but cure led didn't shutdown")
                print("Current getPotLum: ", getPotLum())

                now = datetime.datetime.now()
                with open('states_TC3_scene2_ps3.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                    print("Iterarion: ", iteration, file=f)
                    print("Round: ", rodada, file=f)

                    # print("Error on inside if statement\n", file=f)
                    print("Cure LED was on. Needed to shutting it dows before start PS3", file=f)
                    print("Shutdown button was pressed but cure led didn't shutdown", file=f)
                    print("Current getPotLum: ", getPotLum(), file=f)
                    # print("Current control:", control, file=f)
                    # print("Current ledInfoOld", ledInfoOld, file=f)
                    # print("Current ledInfo", ledInfo, file=f)

                    print("############ END #############", file=f)

                f.close()

      
                return False
    else:

        print("Cure Led is already off")
        return True




def sceneThree():

    #ON_OFF_TIME é de 2 segundos
    pressTime = '05'  # Vai multiplicar por 100mS #Menor que ON_OFF_TIME
    command = '01'
    buttonPower = '12'
    # ON_OFF_TIME_LOCAL = '01'

    auxPotLum = ''
    auxMeanPotLum = []

    # auxPotLum = int(auxPotLum, 16)

    if(getPotLum() > 0):
        #SE o led de cura tiver ligado, desligar ele antes
        print("########### CURE ON ###############")
        print("Cure on. Shutting down.")
        set_config(command, buttonPower, pressTime)
        time.sleep(0.8)

    returnSet = set_config(command, buttonPower, pressTime)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

        time.sleep(0.8)
        ### Momento de captar as respostas da placa
        #tratar o vetor de tuplas do buzzer
        # Nesse caso, só vai ter uma tupla por ser o primeiro perfil

        print("Button configured")

        indexer = 0

        auxTime = time.time()

        while(indexer < 5):
            auxMeanPotLum = auxMeanPotLum + [getPotLum()]
            # time.sleep(0.05)
            indexer = indexer + 1

        print("Elapsed inside while", time.time() - auxTime)

        auxPotLum = statistics.mean(auxMeanPotLum)

        print("Aux pot lum: ", auxPotLum)

        # auxPotLum = int(auxPotLum, 16)

        if(auxPotLum > 0):
            print("OK. Half of the test is nice.")

            set_config(command, buttonPower, pressTime)
        else:
            print("######## ERROR ###############")
            print("Shutdown was pressed but cure led didn't turned on")
            print("Current getPotLum: ", getPotLum())

            now = datetime.datetime.now()
            with open('states_TC3_scene3.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                print("Iterarion: ", iteration, file=f)
                print("Round: ", rodada, file=f)

                # print("Error on inside if statement\n", file=f)
                print("Shutdown was pressed but cure led didn't turned on", file=f)
                print("Current getPotLum: ", getPotLum(), file=f)
                # print("Current control:", control, file=f)
                # print("Current ledInfoOld", ledInfoOld, file=f)
                # print("Current ledInfo", ledInfo, file=f)

                print("############ END #############", file=f)

            f.close()



            return False

        

        if (returnSet == bytes.fromhex('99' + command + 'FF')):
            time.sleep(0.7)
            if(getPotLum() == 0):
                print("Test is ok")
                return True
            else:
                print("######## ERROR ###############")
                print("Shutdown was pressed but cure led didn't shutdown")
                print("Current getPotLum: ", getPotLum())

                now = datetime.datetime.now()
                with open('states_TC3_scene3.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                    print("Iterarion: ", iteration, file=f)
                    print("Round: ", rodada, file=f)

                    # print("Error on inside if statement\n", file=f)
                    print("Shutdown was pressed but cure led didn't shutdown", file=f)
                    print("Current getPotLum: ", getPotLum(), file=f)
                    # print("Current control:", control, file=f)
                    # print("Current ledInfoOld", ledInfoOld, file=f)
                    # print("Current ledInfo", ledInfo, file=f)

                    print("############ END #############", file=f)

                f.close()






                return False








            # return True





    






def main():
    '''
    print("Hello World!")
    totalRound = 50
    cont = 0
    for i in range(totalRound):
        print("Rodada:", i)
        aux = sceneTwo()
        if(aux):
            cont = cont + 1

        time.sleep(1)


    print("Successful tests percentage: ",
                (cont/50)*100)

    print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100)

    '''
    global rodada
    global iteration


    totalRound = 5
    totalIteration = 5

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
    # aux = ''
    for iterationIndex in range(totalIteration):
                        # index = 0
            # for index in range(2):
                with open('output_TC3.txt', 'a') as f: 
                        iteration = iterationIndex
                        index = 0

                        cont = 0
                        initialTime = time.time()
                        for i in range(totalRound):
                                print("Round ", i)
                                print("Iteration ", iterationIndex)
                                rodada = i
                                if(index == 0):
                                    print("Scene One choosen")
                                    aux = sceneOne()
                                    time.sleep(1)
                                elif(index == 1):
                                    print("Scene Two choosen")
                                    aux = sceneTwo()
                                    time.sleep(1)
                                elif(index == 2):
                                    print("Scene Three choosen")
                                    aux = sceneThree()    
                                
                                if(aux):
                                    cont = cont + 1
                                
                                # time.sleep(1)

                        print("############# INIT #############\n\n", file=f)

                        print("Current iteration: ", iteration)
                    
                        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                        print("Iteration No.:", totalIteration, file=f)  
                        print("Round No.:", totalRound, file=f)
                        print("Successful tests percentage: ", (cont/totalRound)*100)

                        print("Unsuccessful tests percentage: ",
                            ((totalRound - cont)/totalRound) * 100)

                        print("Elapsed time: ", time.time() - initialTime)



                        
                        print("Scene", index + 1 ,":", file=f)

                        print("Successful tests percentage: ",
                            (cont/totalRound)*100, file=f)

                        print("Unsuccessful tests percentage: ",
                            ((totalRound - cont)/totalRound) * 100, file=f)

                        print("Elapsed time: ", time.time() - initialTime, file = f)

                        print("\n\n############# END #############\n\n", file=f)


                f.close()







if __name__ == "__main__":
  main()
