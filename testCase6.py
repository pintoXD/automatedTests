from serialTeste import *
from get_buzzer import *
from get_panel import *
import random
import time

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
    print("Settinf button power")
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
            return True
        else:
            print("Battery level reading is not running ok")
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

        else:
            print("Test is not ok. Scenario 2 from case 6 wasn't complied")    



        
    else:

        print("Button unconfigured")






def sceneThree():


        '''

            Esse cenário é realizado durante a leitura da tensão da bateria.
            Durante o processo, o botão seta deve ser acionado aleatoriamente,
            e nada deve acontecer.

        '''

        startTime = time.time()

        # checker = sceneOne()


       ##ON_OFF_TIME global é de 0x14 * 100 milssegundos.

        command = '01'
        buttonPower = '12'
        buttonArrow = '11'
        pressTime = '02'  # 10 em hexadecimal
        #Precisa ser em hexadeciaml o número

 

        returnSet = set_config(command, buttonPower, '1E')
        time.sleep(3)

        if(returnSet == bytes.fromhex('99' + command + 'FF')):
             ##Espera um tempo aleatório antes de apertar o botão seta de vera.

            waitTime = random.uniform(0, 4)
            time.sleep(waitTime)

            returnSet = set_config(command, buttonArrow, pressTime)
            time.sleep(0.5)
        else:
            print("Shuffle arrow press failed.")


        # waitTime = random.uniform(0, 4)
        # time.sleep(waitTime)

        # returnSet = set_config(command, buttonArrow, pressTime)

        if(returnSet == bytes.fromhex('99' + command + 'FF')):

            print("Button SETA configured")

            ledInfo = getPanel()

            ##Depois que o botão seta for pressionado, verificar 
            ##se o painel continua a mostrar a leitura da bateria.
            
            
 

            if(ledInfo == [0, 0, 0, 0]):
                print("PS 1 Scenario 3 from case 6 was complied")
            else:
                print("PS 1 is not ok. Scenario 3 from case 6 wasn't complied")


            


        else:

             print("Button SETA unconfigured")

        ##Momento de verificar se a leitura da bateria se manteve
        # pelos 5 segundos necessários.



        returnSet = set_config(command, buttonPower, '1E')
        time.sleep(3)
        # startTime = time.time()

        if(returnSet == bytes.fromhex('99' + command + 'FF')):
            ##Espera um tempo aleatório antes de apertar o botão seta de vera.
            startTime = time.time()
            cont  = 0
            while cont < 10:

                ledInfo = getPanel()
                print("Cont: ", cont)

                if(ledInfo == [0, 0, 0, 0]):
                    cont = cont + 1
                

            # time.sleep(0.1)



            elapsedTime = time.time() - startTime

            if(elapsedTime >= 5) and (ledInfo == [0, 0, 0, 0]):
                print("PS 2 Scenario 3 from case 6 was complied")

            else:
                print("PS 2 Scenario 3 from case 6 was not complied")


        
        
        
        
        
        
        else:
            print("Power press failed.")
        


   






      

        














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


if __name__ == "__main__":
  main()











