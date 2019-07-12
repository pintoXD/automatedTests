from serialTeste import *
from get_buzzer import *
from get_panel import *
from get_batlvl import *
import time
import random
# import os
import statistics
import os
import datetime

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

'''

Pra comparar os vetores do get_panel retornados, 
comparar eles e dizer se tivesse uma mudança

def getIndex(var1=[], var2=[]):
    if(var1 == None or var2 == None):
        return 'um dos vetores está vazio'
    else:
        for i in range(len(var1)):
            if(var1[i] != var2[i]):
                index1 = i
        for j in range(len(var2)):
            if(var2[j] == 1):
                index2 = j
        return index1, index2

'''


def sceneOne():
    '''    
       #ok por hora
       Verificar se, depois de o processo de análise da carga de bateria, os LEDs
       todos irão se apagar depois de 3s.

    '''
    ##ON_OFF_TIME_GLOBAL é de 2 segundos

    command = '01'
    buttonPower = '12'
    ON_OFF_TIME_LOCAL = '1E' #30 Em decimal

    ##ON_OFF_TIME global é de 0x1E * 100 milssegundos.
    print("Setting button power")
    returnSet = set_config(command, buttonPower, ON_OFF_TIME_LOCAL)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):

        print("Button configured")
        time.sleep(3)

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
        initialTime = time.time()
        cont = 0
        ledInfo = getPanel()
     
        while ledInfo != [0, 0, 0, 0]:
            ledInfo = getPanel()
            cont = cont + 1           
            time.sleep(0.2)    

     ########### TO DO #############
    #### Validate the test

        # time.sleep(5)
        ledInfo = getPanel()

        elapsedTime = time.time() - initialTime

        print("Elapsed time: ", elapsedTime)

        if cont >= 10 and ledInfo == [0, 0, 0, 0] and elapsedTime >= 5:
            print("Battery level read is runnning ok")
            print("Scenario One is ok")
            return True
        else:
            print("Battery level reading is not running ok")
            print("Scenario One isn't ok")
            now = datetime.datetime.now()
            with open('states_TC6.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Scenario One isn't ok.", file=f)
                # print("Error on inside if statement\n", file=f)
                print("Battery level reading is not running ok", file=f)
                print("current cont:", cont, file=f)
                print("Current ledInfo:", ledInfo, file=f)
                # print("Current ledInfoOld", ledInfoOld, file=f)
                # print("Current ledInfo", ledInfo, file=f)
                print("############ END #############", file=f)

            f.close()

            return False

    else:

        print("Power button press failed")

        now = datetime.datetime.now()
        with open('states_TC6.txt', 'a') as f:

            print("############ INIT #############", file=f)
            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

            print("Scenario One isn't ok.", file=f)
            # print("Error on inside if statement\n", file=f)
            print("Power button press failed", file=f)
            print("current returnSet:", returnSet, file=f)
            # print("Current ledInfo:", ledInfo, file=f)
            # # print("Current ledInfoOld", ledInfoOld, file=f)
            # print("Current ledInfo", ledInfo, file=f)
            print("############ END #############", file=f)

        f.close()

        return False

def sceneTwo():

    '''
        Caso que testa o acionamento do botão ON/OFF durante o processo
        de leitura do nível da bateria.

    '''

    time.sleep(5)

    # checker = sceneOne()

    # if(checker == True):
        
        ##ON_OFF_TIME global é de 0x14 * 100 milssegundos.

    command = '01'
    buttonPower = '12'
    pressTime = '0A'    #10em hexadecimal
                                #Precisa ser em hexadeciaml o número

    #Aperta o botão power por '1E' * 100 milissegundos
    returnSet = set_config(command, buttonPower, '1E')
    # time.sleep(3)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):
        time.sleep(3.2)
        returnSet = set_config(command, buttonPower, pressTime)
        time.sleep(1)
    else:
        print("First power press failed.")

        now = datetime.datetime.now()
        with open('states_TC6.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Scenario Two isn't ok.", file=f)
                # print("Error on inside if statement\n", file=f)
                print("First power press failed", file=f)
                print("current returnSet:", returnSet, file=f)
                # print("Current ledInfo:", ledInfo, file=f)
                # # print("Current ledInfoOld", ledInfoOld, file=f)
                # print("Current ledInfo", ledInfo, file=f)
                print("############ END #############", file=f)

        f.close()

        return False

    # returnSet = set_config(command, buttonPower, pressTime)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):
        
        print("Button configured")

        ledInfo = getPanel()

        if(ledInfo == [0, 0, 0, 0]):
            print("Test ok. Scenario 2 from case 6 was complied")
            return True

        else:
            print("Test is not ok. Scenario 2 from case 6 wasn't complied")

            now = datetime.datetime.now()
            with open('states_TC6.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                    print("Scenario Two isn't ok.", file=f)
                    # print("Error on inside if statement\n", file=f)
                    # print("First power press failed", file=f)
                    # print("current returnSet:", returnSet, file=f)
                    print("Current ledInfo:", ledInfo, file=f)
                    # # print("Current ledInfoOld", ledInfoOld, file=f)
                    # print("Current ledInfo", ledInfo, file=f)
                    print("############ END #############", file=f)

            f.close()

            return False



        
    else:

        print("Button unconfigured")
        now = datetime.datetime.now()
        with open('states_TC6.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Scenario Two isn't ok.", file=f)
                # print("Error on inside if statement\n", file=f)
                print("Second power press failed", file=f)
                print("current returnSet:", returnSet, file=f)
                # print("Current ledInfo:", ledInfo, file=f)
                # # print("Current ledInfoOld", ledInfoOld, file=f)
                # print("Current ledInfo", ledInfo, file=f)
                print("############ END #############", file=f)

        f.close()



        return False






def sceneThree():

        '''

            Esse cenário é realizado durante a leitura da tensão da bateria.
            Durante o processo, o botão seta deve ser acionado aleatoriamente,
            e nada deve acontecer.

        '''

        auxReturn = []

        

        # checker = sceneOne()


       ##ON_OFF_TIME global é de 0x14 * 100 milssegundos.

        command = '01'
        buttonPower = '12'
        buttonArrow = '11'
        pressTime = '02'  # 10 em hexadecimal
        #Precisa ser em hexadeciaml o número

 

        returnSet = set_config(command, buttonPower, '1E')
        time.sleep(3)
        initialTime = time.time()

        waitTime = 0

        if(returnSet == bytes.fromhex('99' + command + 'FF')):
             ##Espera um tempo aleatório antes de apertar o botão seta de vera.
        
            waitTime = random.uniform(0.5, 3)
            print("Sleep time: ", waitTime)
            time.sleep(waitTime)

            returnSet = set_config(command, buttonArrow, pressTime)
            time.sleep(0.5)
        else:
            print("Power press failed.")
            now = datetime.datetime.now()
            with open('states_TC6.txt', 'a') as f:

                    print("############ INIT #############", file=f)
                    print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                    print("Scenario Three isn't ok.", file=f)
                    # print("Error on inside if statement\n", file=f)
                    print("Power press failed", file=f)
                    print("current returnSet:", returnSet, file=f)
                    # print("Current ledInfo:", ledInfo, file=f)
                    # # print("Current ledInfoOld", ledInfoOld, file=f)
                    # print("Current ledInfo", ledInfo, file=f)
                    print("############ END #############", file=f)

            f.close()

            return False


        # waitTime = random.uniform(0, 4)
        # time.sleep(waitTime)

        

        if(returnSet == bytes.fromhex('99' + command + 'FF')):

            print("Button SETA configured")

            ledInfo = getPanel()

            ##Depois que o botão seta for pressionado, verificar 
            ##se o painel continua a mostrar a leitura da bateria.
           
            cont  = 0
            while cont < 5:

                ledInfo = getPanel()
                print("Cont: ", cont)

                if(ledInfo != [0, 0, 0, 0]):
                    cont = cont + 1
               
                time.sleep(0.15)

            if(cont >= 5):
                print("PS One from Scenario 3 was complied")
                print("Nothing happens")
                auxReturn = auxReturn + [True]
            else:
                print("PS One from Scenario 3 was complied")
                print("Something happens")
                auxReturn = auxReturn + [False]


                now = datetime.datetime.now()
                with open('states_TC6.txt', 'a') as f:

                            print("############ INIT #############", file=f)
                            print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                            print("Scenario Three isn't ok.", file=f)
                            # print("Error on inside if statement\n", file=f)
                            print(
                                "PS One from Scenario 3 wasn't complied\nSomething happens", file=f)
                            print("Current cont:", cont, file=f)
                            print("Current ledInfo:", ledInfo, file=f)
                            # # print("Current ledInfoOld", ledInfoOld, file=f)
                            # print("Current ledInfo", ledInfo, file=f)
                            print("############ END #############", file=f)

                f.close()



                

            #elapsedTime = time.time() - startTime

        else:
            print("Shuffle arrow press failed")
            now = datetime.datetime.now()
            with open('states_TC6.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Scenario Three isn't ok.", file=f)
                # print("Error on inside if statement\n", file=f)
                print(
                    "PS One from Scenario 3 get an error", file=f)
                print("Shuffle arrow press failed", file=f)
                print("Current waitTime to press arrow:", ledInfo, file=f)
                # # print("Current ledInfoOld", ledInfoOld, file=f)
                # print("Current ledInfo", ledInfo, file=f)
                print("############ END #############", file=f)

            f.close()
            return False



        ledInfo = getPanel()
        while(ledInfo != [0, 0, 0, 0]):
            ledInfo = getPanel()
            time.sleep(0.2)
        
        elapsedTime = time.time() - initialTime

        print("Elapsed time: ", elapsedTime)

        # print

        
        if(elapsedTime >= 5) and (ledInfo == [0, 0, 0, 0]):
            print("PS 2 Scenario 3 from case 6 was complied")
            auxReturn = auxReturn + [True]

        else:
            print("PS 2 Scenario 3 from case 6 was not complied")
            auxReturn = auxReturn + [False]
            now = datetime.datetime.now()
            with open('states_TC6.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Scenario Three isn't ok.", file=f)
                # print("Error on inside if statement\n", file=f)
                print(
                    "PS 2 Scenario 3 from case 6 was not complied", file=f)
                # print("Shuffle arrow press failed", file=f)
                print("Current elapsedTime:", elapsedTime, file=f)
                # # print("Current ledInfoOld", ledInfoOld, file=f)
                print("Current ledInfo", ledInfo, file=f)
                print("############ END #############", file=f)

            f.close()
            


                
        


        return (auxReturn[0] and auxReturn[1]) #Só retorna verdadeiro se os dois PS derem certo.



def sceneFour():

        '''

            Esse cenário procura verificar se o nível de bateria mostrado no painel de LEDs,
            corresponde ao nível da bateria lido pelo AD da placa de aquisição. Visa ratificar
            se a leitura da bateria para o painel de LEDs.
            
        '''


        auxReturn = []

        # checker = sceneOne()

       ##ON_OFF_TIME global é de 0x14 * 100 milssegundos.

        command = '01'
        buttonPower = '12'
        buttonArrow = '11'
        pressTime = '1E'  # 10 em hexadecimal
        #Precisa ser em hexadeciaml o número

        returnSet = set_config(command, buttonPower, '1E')
        # initialTime = time.time()

        if(returnSet == bytes.fromhex('99' + command + 'FF')):
             ##Espera um tempo aleatório antes de apertar o botão seta de vera.
            time.sleep(3)


            cont = 0
            ledInfo = getPanel()
            ledInfoOld = getPanel()

            myTuple = ''

            # ledInfo = []
            # ledInfoOld = []

 

            while (cont < 6):
                # print("Inside")
                aux = getPanel()
                # ledInfoOld = getPanel()

                # time.sleep(0.40)

                ledInfo = getPanel()

                if(ledInfo != ledInfoOld):

                    # print("LedInfo current inside: ", ledInfo)
                    # print("Ledinfo old inside: ", ledInfoOld)
                    # print("Cont is: ", cont)



                    if((ledInfo == [0, 0, 0, 0] and ledInfoOld == [0, 0, 0, 1])  or (ledInfo == [0, 0, 0, 1] and ledInfoOld == [0, 0, 0, 0])):
                            myTuple = (1, cont)

                    
                    if((ledInfo == [0, 0, 0, 1] and ledInfoOld == [0, 0, 1, 1])  or (ledInfo == [0, 0, 1, 1] and ledInfoOld == [0, 0, 0, 1])):
                            myTuple = (2, cont)


                    if((ledInfo == [0, 0, 1, 1] and ledInfoOld == [0, 1, 1, 1])  or (ledInfo == [0, 1, 1, 1] and ledInfoOld == [0, 0, 1, 1])):
                            myTuple = (3, cont)
                        

                    if((ledInfo == [0, 1, 1, 1] and ledInfoOld == [1, 1, 1, 1])  or (ledInfo == [1, 1, 1, 1] and ledInfoOld == [0, 1, 1, 1])):
                             myTuple = (4, cont)





                    ledInfoOld = ledInfo

                    cont = cont + 1



                time.sleep(0.05)


                # print("LedInfo current outside: ", ledInfo)
                # print("Ledinfo old outside: ", ledInfoOld)


            print("myTuple[0] is: ", myTuple[0])
            print("myTuple[1] is: ", myTuple[1])


            if(myTuple[1] == 5):
                auxBatLvl = round(getBatVoltage(), 3) + 0.04

                if(myTuple[0] == 1 and (auxBatLvl <= 3.8)):

                        print("Panel measure complies with battery read")
                        print("Level read: Lower than 25%")
                                                    

                elif(myTuple[0] == 1 and (auxBatLvl >= 3.816  and auxBatLvl <= 3.9)):
                        print("Panel measure complies with battery read")
                        print("Level read: 0'%' - 25'%'")


                elif(myTuple[0] == 2 and (auxBatLvl >= 3.916  and auxBatLvl <= 4.015)):
                        print("Panel measure complies with battery read")
                        print("Level read: 25'%' - 50'%'")



                elif(myTuple[0] == 3 and (auxBatLvl >= 4.016  and auxBatLvl <= 4.215)):   
                        print("Panel measure complies with battery read")
                        print("Level read: 50'%' - 75'%'")

                elif(myTuple[0] == 4 and (auxBatLvl >= 4.216)):   
                        print("Panel measure complies with battery read")
                        print("Level read: 75'%' - 100'%'")


                else:

                    print("Battery level out of interval considerations")
                    now = datetime.datetime.now()
                    with open('states_TC6.txt', 'a') as f:

                        print("############ INIT #############", file=f)
                        print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                        print("Scenario Four isn't ok.", file=f)
                        # print("Error on inside if statement\n", file=f)
                        print(
                            "Battery level out of interval considerations", file=f)
                        # print("Shuffle arrow press failed", file=f)
                        print("Current tuple:", myTuple, file=f)
                        print("Current rounded battery voltage",
                              round(getBatVoltage(), 3), file=f)
                        print("Current rounded battery voltage + 0.04",
                              round(getBatVoltage(), 3) + 0.04, file=f)
                        print("############ END #############", file=f)

                    f.close()

                    return False


        
        else:
            print("Power press failed.")
            now = datetime.datetime.now()
            with open('states_TC6.txt', 'a') as f:

                print("############ INIT #############", file=f)
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)

                print("Scenario Four isn't ok.", file=f)
                # print("Error on inside if statement\n", file=f)
                print(
                    "Power press failed", file=f)
                # print("Shuffle arrow press failed", file=f)
                print("Current returnSet:", returnSet, file=f)
                # print("Current rounded battery voltage",
                #         round(getBatVoltage(), 3), file=f)
                # print("Current rounded battery voltage + 0.04",
                #         round(getBatVoltage(), 3) + 0.04, file=f)
                print("############ END #############", file=f)

            f.close()

            return False


    








def main():

    
    print("Hello World!")

#   sceneOne()
#   sceneTwo()c\cc
    # sceneThree()
        # sceneFour()
    # for i in range(10):
    #   print("Round ", i)
    #   sceneOne()
    # #   sceneTwo()
    # #   sceneThree()
    #   time.sleep(1)



    with open('output_TC6.txt', 'w') as f:
        for index in range(3):
                print("Scene ", index, ":")

                cont = 0
                initialTime = time.time()
                for i in range(50):
                        print("Round ", i)
                        if(index == 0):
                            aux  = sceneOne()
                        elif(index == 1):
                            aux = sceneTwo()
                        elif(index == 2):
                            aux = sceneThree()

                        if(aux):
                            cont = cont + 1
                        
                        time.sleep(1)


                print("Successful tests percentage: ", (cont/50)*100)

                print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100)

                print("Elapsed time: ", time.time() - initialTime)


                # with open('output_TC6.txt', 'a') as f:
                print("############# INIT ###########\n\n", file=f)
                now = datetime.datetime.now()
                print("Date: ", now.strftime("%Y-%m-%d %H:%M"), file=f)
                
                print("Scene ", index + 1, ":", file=f)

                print("Successful tests percentage: ", (cont/50)*100, file=f)

                print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100, file=f)

                print("Elapsed time: ", time.time() - initialTime, file = f)

                print("############# END ###########\n\n", file=f)

                # f.close()

        f.close()
    











if __name__ == "__main__":
  main()











