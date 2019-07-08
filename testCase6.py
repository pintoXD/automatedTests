from serialTeste import *
from get_buzzer import *
from get_panel import *
import time
import random
import os


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
        while cont < 5:
            ledInfo = getPanel()
            
            if(ledInfo != ledInfoOld):
                cont = cont + 1
                ledInfoOld = ledInfo
                    
            
            time.sleep(0.1)    

     ########### TO DO #############
    #### Validate the test

        time.sleep(5)
        ledInfo = getPanel()

        if cont >= 5 and ledInfo == [0, 0, 0, 0]:
            print("Battery level read is runnning ok")
            print("Scenario One is ok")
            return True
        else:
            print("Battery level reading is not running ok")
            print("Scenario One isn't ok")
            return False

    else:

        print("Power button press failed")
        return False

def sceneTwo():

    '''
        Caso que testa o acionamento do botão ON/OFF durante o processo
        de leitura do nível da bateria.

    '''

    # checker = sceneOne()

    # if(checker == True):
        
        ##ON_OFF_TIME global é de 0x14 * 100 milssegundos.

    command = '01'
    buttonPower = '12'
    pressTime = '0A'    #10em hexadecimal
                                #Precisa ser em hexadeciaml o número

    #Aperta o botão power por ON_OFF_TIME * 100 milissegundos
    returnSet = set_config(command, buttonPower, '1E')
    time.sleep(3)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):
        returnSet = set_config(command, buttonPower, pressTime)
        time.sleep(1)
    else:
        print("First power press failed.")

    # returnSet = set_config(command, buttonPower, pressTime)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):
        
        print("Button configured")

        ledInfo = getPanel()

        if(ledInfo == [0, 0, 0, 0]):
            print("Test ok. Scenario 2 from case 6 was complied")
            return True

        else:
            print("Test is not ok. Scenario 2 from case 6 wasn't complied")    
            return False



        
    else:

        print("Button unconfigured")
        return False






def sceneThree():

        '''

            Esse cenário é realizado durante a leitura da tensão da bateria.
            Durante o processo, o botão seta deve ser acionado aleatoriamente,
            e nada deve acontecer.

        '''

        auxReturn = []

        startTime = time.time()

        # checker = sceneOne()


       ##ON_OFF_TIME global é de 0x14 * 100 milssegundos.

        command = '01'
        buttonPower = '12'
        buttonArrow = '11'
        pressTime = '02'  # 10 em hexadecimal
        #Precisa ser em hexadeciaml o número

 

        returnSet = set_config(command, buttonPower, '1E')
        #time.sleep(3)
        initialTime = time.time()

        if(returnSet == bytes.fromhex('99' + command + 'FF')):
             ##Espera um tempo aleatório antes de apertar o botão seta de vera.
        
            waitTime = random.uniform(0, 3)
            time.sleep(waitTime)

            returnSet = set_config(command, buttonArrow, pressTime)
            time.sleep(0.2)
        else:
            print("Power press failed.")


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
                

            #elapsedTime = time.time() - startTime

        else:
            print("Shuffle power press failed")

        ledInfo = getPanel()
        while(ledInfo != [0, 0, 0, 0]):
            ledInfo = getPanel()
            time.sleep(0.2)
        
        elapsedTime = time.time() - initialTime

        # print

        
        if(elapsedTime >= 5) and (ledInfo == [0, 0, 0, 0]):
            print("PS 2 Scenario 3 from case 6 was complied")
            auxReturn = auxReturn + [True]

        else:
            print("PS 2 Scenario 3 from case 6 was not complied")
            auxReturn = auxReturn + [False]


                
        


        return (auxReturn[0] and auxReturn[1]) #Só retorna verdadeiro se os dois PS derem certo.


def main():

    print("Hello World!")

#   sceneOne()
#   sceneTwo()
    sceneThree()
  #sceneFour()
  #   for i in range(50):
  #     print(i)
  #     sceneTwo()
  #     time.sleep(1)
'''   for index in range(3):
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


        with open('output_TC6.txt', 'a') as f:
                print("############# INIT ###########\n\n", file=f)
                
                print("Scene ", index, ":", file=f)

                print("Successful tests percentage: ", (cont/50)*100, file=f)

                print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100, file=f)

                print("Elapsed time: ", time.time() - initialTime, file = f)

                print("############# END ###########\n\n", file=f)

        f.close()

'''












if __name__ == "__main__":
  main()











