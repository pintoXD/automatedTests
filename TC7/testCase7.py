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




def sceneOne():

    '''
          Esse cenário trata da situação que, estando sendo
          executado um perfil de cura, o botão ON/OFF é pressidonado
          por um tempo maior do que ON_OFF_TIME, devendo fazer
          com que a cura seja imediatamente encerrada.

    '''


    
    # time.sleep(10)    

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    times = random.randint(1, 4)
    limit = 15
    pressTime = '02' ##2 em hexadecimal. Botão será então presssionado por
                     ## 30 * 100 milissegundos.
    pressTimePower = '28' ##40 em decimal. Botão power será pressionado 
                          ##por 40 * 100 milisseegundos

    ##Seleciona e ativa um perfil de cura, antes de tudo

    print("Times: ", times)

    returnSetRepeat = setRepeat(buttonArrow, times, limit, pressTime)

    if(returnSetRepeat):
        print("Cure profile successfully configured")
            
        #Se o perfil for iniciado corretamente,
        # esperar por waitTime segudnos e depois pressionar o botão ON/OFF
        
               
        returnSet = set_config(command, buttonPower, pressTime)
        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            waitTime = random.uniform(0, 8)
            time.sleep(waitTime)

            returnSet = set_config(command, buttonPower, pressTimePower)

        else:
            print("First power press failed")


            now = datetime.datetime.now()
            with open('states_TC7.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Scene One get an error.", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Power press failed", file=f)
                print("Current returnSet: ", returnSet, file=f)

                print("############ END #############\n\n", file=f)

            f.close()




            return False


        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            #Se o botão for corretamente acionado
            # verifica se a potência do LED caiu a 0 e trata caso não haja.
            #     
            
            print("Second Power pressed successfully")

            time.sleep(4.5)

            if(getPotLum() == 0):
                print("Main LED (cure LED) successfully shutdown")
                print("Test ok")
                return True
            else:
                print("Main LED (cure LED) cannot be shutdown") 
                print("Test is not ok")

                now = datetime.datetime.now()
                with open('states_TC7.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Scene One get an error.", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                    print("Main LED (cure LED) cannot be shutdown", file = f)
                    print("Current getPotLum", getPotLum(), file=f)
                    # print("Current returnSet: ", returnSet, file=f)

                    print("############ END #############\n\n", file=f)

                f.close()

            return False
                 
    else:
        print("Error on buttonArrow configuration")
        now = datetime.datetime.now()
        with open('states_TC7.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("Scene One get an error.", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

            print("Current getPotLum", getPotLum(), file=f)
            print("Error on buttonArrow configuration", file=f)
            print("Current returnSet: ", returnSet, file=f)

            print("############ END #############\n\n", file=f)

        f.close()





        

def sceneTwo():

    '''
        Este cenário possui estratégia semelhante ao cenário 1, contudo, 
        deve-se pressionar o botão ON/OFF, por ON_OFF_TIME antes do LED de cura
        ser desativado. Pensou-se usar thread para verificar a potência
        do LED a cada instante, mas foi notado que somente pressionar
        o botão ON/OFF pelo tempo exato de ON_OFF_TIME já seria suficiente
        para atender a especificação. Contudo, há necessidade de confirmar
        essa escolha.

    '''

    command = '01'
    buttonArrow = '11'
    buttonPower = '12'
    times = random.randint(1,4)
    limit = 15
    pressTime = '02'  # 20 em hexadecimal. Botão será então presssionado por
    ## 20 * 100 milissegundos.
    pressTimePower = '14'  # 40 em decimal. Botão power será pressionado
    ##por 40 * 100 milisseegundos

    ##Seleciona e ativa um perfil de cura, antes de tudo
    returnSetRepeat = setRepeat(buttonArrow, times, limit, pressTime)
    returnSet = set_config(command, buttonPower, pressTime)

    if(returnSetRepeat and returnSet == bytes.fromhex('99' + command + 'FF')):
        print("Cure profile and power successfully configured")

       
        #Se o perfil for iniciado corretamente,
        # esperar por waitTime segundos e depois pressionar o botão ON/OFF
        waitTime = random.uniform(0, 9) #Requisito de acionamento aleatório do botão
        time.sleep(waitTime)


        #Acionar o botão por exatamente ON_OFF_TIME segundos
        returnSet = set_config(command, buttonPower, pressTimePower)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            #Se o botão for corretamente acionado
            # verifica se a potência do LED caiu a 0 e trata caso não haja.
            #

            print("Power pressed successfully")
            time.sleep(2)

            if(getPotLum() == 0):
                print("Main LED (cure LED) successfully shutdown")
                print("Scene Two ok")
                return True
            else:
                print("Main LED (cure LED) cannot be shutdown")
                print("Scene Two not ok")


                now = datetime.datetime.now()
                with open('states_TC7.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Scene Two get an error.", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                    print("Main LED (cure LED) cannot be shutdown", file = f)
                    print("Current getPotLum", getPotLum(), file=f)
                    # print("Current returnSet: ", returnSet, file=f)

                    print("############ END #############\n\n", file=f)

                f.close()


                return False
        
        else:
            print("Error on buttonPower configuration")
            print("Scene Two not ok")

            now = datetime.datetime.now()
            with open('states_TC7.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Scene Two get an error.", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Error on buttonPower configuration", file=f)
                print("Current returnSet: ", returnSet, file=f)

                print("############ END #############\n\n", file=f)

            f.close()

            return False

    else:
        print("Error on buttonArrow configuration")
        print("Scene Two not ok")


        now = datetime.datetime.now()
        with open('states_TC7.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("Scene Two get an error.", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

            print("Error on buttonArrow configuration", file=f)
            print("Current returnSet: ", returnSet, file=f)

            print("############ END #############\n\n", file=f)

        f.close()


        return False


def sceneThree():

    '''
        Esse cenário pede que o sistema esteja ligado, mas que
        não esteja executando nenhum perfil de cura.
        Então é solicitado que se mostre o nível da bateria.
        Depois de mostrado, a tensão real na bateria deve ser
        medida.

    '''

    command = '01'
    buttonPower = '12'
    pressTimePower = '14' #40 em hexadecimal
                        ##Botão passará 40 * 100 milissegundos pressionado

           #Acionar o botão por exatamente ON_OFF_TIME segundos
    returnSet = set_config(command, buttonPower, pressTimePower)

    if (returnSet == bytes.fromhex('99' + command + 'FF')):

            #Se o botão for corretamente acionado
            # verifica se a potência do LED caiu a 0 e trata caso não haja.
            #

        print("Power pressed successfully")
        time.sleep(2)
        flag = False
        ledInfo = getPanel()
        for i in range(7):
            ledInfo = ledInfo + getPanel()
            time.sleep(0.3)
            if i > 0 and ledInfo[i] != [0, 0, 0, 0]:
                print("OK COMPUTER")
                flag = True
                break


        ##Dorme pelo tempo que os LEDs ficarem acesos
        time.sleep(5)

        if(flag):
        
                print("Battery level showed in LEDs")
                print("Real battery level is: ", getBatLvl())
                print("Scene Three ok")
                print("ledInfo is: ", ledInfo)
                return True
        
        else:
                print("Some error occured when showing battery level")
                print("Scene Three not ok")
                

                now = datetime.datetime.now()
                with open('states_TC7.txt', 'a') as f:

                        print("############ INIT #############", file=f)
                        print("Scene Three get an error.", file=f)
                        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)


                        print("Some error occured when showing battery level", file=f)
                        print("Current flag:", flag, file=f)
                        print("Current ledInfo", ledInfo, file=f)
                        # print("Error on buttonArrow configuration", file=f)
                        # print("Current returnSet: ", returnSet, file=f)

                        print("############ END #############\n\n", file=f)

                f.close()






                return False

        
     

    else:
        print("Error on buttonPower configuration")
        print("Scene Two not ok")

        now = datetime.datetime.now()
        with open('states_TC7.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Scene Three get an error.", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Error on buttonPower configuration", file=f)
                print("Current returnSet: ", returnSet, file=f)

                print("############ END #############\n\n", file=f)

        f.close()
      





        return False


def sceneFour():

    '''
        Para esse cenário, é pedido que o sistema esteja ligado, 
        mas não esteja realizando nenhum perfil de cura.
        Também é pedido que a bateria esteja abaixo de 25%
        de carga relativa.

        Tendo sido isso atendido, a bateria deve tentar 
        ser medida, mas 3 bipes devem ser acionados.

    '''

    # MAX_BAT_LEVEL = 4.2 ##Esse valor deve mudar. Favor conferir o valor total da tensão da bateria
    # CURRENT_BAT_LEVEL = getBatLvl()

    # batteryPercentage = 100 - ((CURRENT_BAT_LEVEL/MAX_BAT_LEVEL) * 100)

    SOC_25 = 2410

    SOC_25_VOLTAGE = 3.916

    adRead = round(getBatLvl(), 3) + 0.02


    #Cenário de teste só é iniciado se a bateria tever menos de 25% de carga
    if(adRead <= SOC_25_VOLTAGE):
        command = '01'
        buttonPower = '12'
        pressTimePower = '0A'  # 10 em hexadecimal
        ##Botão passará 10 * 100 milissegundos pressionado
        profileTime = getCureProfileTime()
        while(profileTime != 10):
            profileTime = getCureProfileTime()
            print("profileTime: ", profileTime)
            time.sleep(0.5)
       
        #Acionar o botão por exatamente menos que ON_OFF_TIME segundos (menos que 2 segundos)
        returnSet = set_config(command, buttonPower, pressTimePower)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

                #Se o botão for corretamente acionado
                # verifica se a potência do LED caiu a 0 e trata caso não haja.
                #
            #time.sleep(1)
            print("Power pressed successfully")
            # testeAux = getPotLum()    



            time.sleep(5)
            buzzerInfo = getBuzzer()
            testeAux = getPotLum()
            print("testAux: ", testeAux)
            print("Number of bips 1: ", len(buzzerInfo))
            print(buzzerInfo)
            # time.sleep(profileTime + 8)
            # buzzerInfo = getBuzzer()
            # print("Number of bips 2: ", len(buzzerInfo))
            # print(buzzerInfo)
            time.sleep(profileTime)

            if(testeAux != 0 and len(buzzerInfo) == 3):
                    print("Test succesffully done.")
                    print("Battery charge almost empty.")
                    print("Number of bips: ", len(buzzerInfo))
                    print("Scene Four ok")
                    return True
            else:

                    print("Test unsuccesfully. Some error occured.")
                    print("Buzzer beeps, main LED activated or battery level doesn't comply the specifications")
                    print("Scene Four not ok")

                    now = datetime.datetime.now()
                    with open('states_TC7.txt', 'a') as f:

                            print("############ INIT #############", file=f)
                            print("Scene Four got an error.", file=f)
                            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                            print("Buzzer beeps, main LED activated or battery level doesn't comply the specifications", file=f)


                            # print("Some error occured when showing battery level", file=f)
                            print("Current buzzerInfo:", buzzerInfo, file=f)
                            print("Current potLum", testeAux, file=f)
                            print("Currente profileTime:", profileTime, file=f)
                            # print("Error on buttonArrow configuration", file=f)
                            # print("Current returnSet: ", returnSet, file=f)

                            print("############ END #############\n\n", file=f)

                    f.close()




                    return False


        else:
            print("Error on buttonPower configuration")
            print("Scene Four not ok")

            now = datetime.datetime.now()
            with open('states_TC7.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Scene Four got an error.", file=f)
                    print("Date: ", now.strftime(
                        "%Y-%m-%d %H:%M"), file=f)

                    print("Error on buttonPower configuration", file=f)
                    print("Current returnSet: ", returnSet, file=f)

                    print("############ END #############\n\n", file=f)

            f.close()



            return False
    

    else:

        print("Battery level over 25%")
        print("Scene Four not ok")

        now = datetime.datetime.now()
        with open('states_TC7.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Scene Four got an error.", file=f)
                print("Date: ", now.strftime(
                    "%Y-%m-%d %H:%M"), file=f)

                print("Battery level over 25%", file=f)
                print("Current battery level: ", adRead, file=f)


                print("############ END #############\n\n", file=f)

        f.close()




        return False


def sceneFive():

    '''
        Para esse cenário, é pedido que o sistema esteja ligado,
        mas não esteja realizando nenhum perfil de cura.
        Também é pedido que a bateria esteja abaixo de 25% e também abaixo do limite de carga mínima.

     

    '''

    # MAX_BAT_LEVEL = 4.2 ##Esse valor deve mudar. Favor conferir o valor total da tensão da bateria
    # CURRENT_BAT_LEVEL = getBatLvl()

    # batteryPercentage = 100 - ((CURRENT_BAT_LEVEL/MAX_BAT_LEVEL) * 100)

    # SOC_THRESHOLD_CMIN = 2358 - 10 #hISTERESIS de +- 10. Coloquei pra mais aqui.
    voltagCalibration = 0.02

    SOC_THRESHOLD_CMIN_VOLTAGE = 3.8 - 0.016

    # adRead = getBatLvl() + 0.04
    adRead = round(getBatVoltage(), 3) + voltagCalibration

    print("BAttery voltage with compensation: ",
          round(getBatVoltage(), 3) + voltagCalibration)

    print("BAttery voltage without compensation: ",
          round(getBatVoltage(), 3))

    #Cenário de teste só é iniciado se a bateria tever menos de 25% de carga
    if(adRead <= SOC_THRESHOLD_CMIN_VOLTAGE):
       
        command = '01'
        buttonPower = '12'
        pressTimePower = '02'  # 10 em hexadecimal
        ##Botão passará 10 * 100 milissegundos pressionado
        profileTime = getCureProfileTime()

        while(profileTime != 10):
            profileTime = getCureProfileTime()
            print("profileTime: ", profileTime)
            time.sleep(0.5)



        '''

            A ideia aqui vai ser basicamente o seguinte:
            Eu não sei se, quando eocesses that have a file open with the commastá com carga mínima, ao mandar acionar o perfil de cura,
            o vetor dos buzzers é limpo como acontece no acionamento dos perfis de cura usualmente.

            Então, eu resolvi pegar o vetor de buzzer antes de acionar o botão power
            e pegar ele depois também. Dessa forma, eu posso comparar o tamanho deles e então pegar
            só os últimos elementos que foram adicionados.

            Espero que seja assim mesmo
        '''


        # buzzerInfoOld = getBuzzer()


        returnSet = set_config(command, buttonPower, pressTimePower)

        if (returnSet == bytes.fromhex('99' + command + 'FF')):

            print("Power pressed successfully")
            # testeAux = getPotLum()
            time.sleep(0.5)
            testePotLum = getPotLum()

            time.sleep(5)
            buzzerInfo = getBuzzer()
            print("testePotLum: ", testePotLum)

            # buzAux = []
            # lenAux = len(buzzerInfo) - len(buzzerInfoOld)

            # if(lenAux > 0):
            # buzAux = buzzerInfo[len(buzzerInfo) - lenAux :]


            #Aí aqui ele vai testar           
            if(testePotLum == 0 and (buzzerInfo[0][0] == 5)):
                    print("Test succesffully done.")
                    print("Insufficient batery charge to start a cure profile.")
                    print("Number of bips: ", len(buzzerInfo))
                    print("Scene Four ok")
                    return True
            else:

                    print("Test unsuccesfully. Some error occured.")
                    print("Buzzer beeps, main LED activated or battery level doesn't comply the specifications")
                    print("Scene Four not ok")
                    return False





    else:

        print("Battery level above the specification")
        print("BAttery voltage with compensation: ", round(getBatVoltage(), 3) + 0.04)





def main():

    print("Hello World!")
    totalRound = 50
        
    #sceneOne()
        # sceneTwo()
    #   sceneThree()
    
    #   sceneFour() ##Cenário quatro precisa da bateria a 3.8 ou abaixo
    # sceneFive()


    now = datetime.datetime.now()
    with open('output_TC7.txt', 'a') as f:
                # index = 1
        for index in range(2):

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

                        elif(index == 2):
                            print("Scene Three choosen")
                            aux = sceneThree()
                            

                        elif(index == 3):

                            print("Scene Four choosen")
                            aux = sceneFour()
                            


                        if(aux):
                            cont = cont + 1

                        time.sleep(1)

                print("############# INIT #############\n\n", file=f)

                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Successful tests percentage: ", (cont/50)*100)

                print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100)

                print("Elapsed time: ", time.time() - initialTime)

                print("Scene", index + 1, ":", file=f)

                print("Successful tests percentage: ", (cont/50)*100, file=f)

                print("Unsuccessful tests percentage: ",
                      ((50 - cont)/50) * 100, file=f)

                print("Elapsed time: ", time.time() - initialTime, file=f)

                print("\n\n############# END #############\n\n", file=f)

    f.close()



if __name__ == "__main__":
  main()












