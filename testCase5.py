from serialTeste import *
from get_buzzer import *
from get_panel import *
import time
import random
import os




# def validateLED(ledInfo, ledToken):
#     ###### Validação do teste ######
#     '''
#         Cada configuração de leds acesos produz um número
#         em hexadecimal. Esse número deve ser enviado
#         na variável ledToken, para comparação. 
#         Pra mais informações, olhar a biblioteca.
    
#     '''

#      ## Validação do LED ##

#     auxLedValidation = ledInfo

#     if(auxLedValidation == ledToken):
#         print("Test OK. Correct LED turned on")
#     else:
#         print("Test failed. Incorrect LED turned on")

# def validateBuzzer(buzzerInfo):
#     ## Validação do buzzer ##

#     auxBuzzerValidation = buzzerInfo

#     #Tempo de buzzer ligado depende da situação

#     ##Validação do tempo em alto do buzzer para o caso atual
#     buzzHighTime = 100  # Tempo em milissegundos
#     # Não sei se a placa me envia os tempos nessa ordem não
#     # buzzRelativeTime = [10, 20, 40, 60]
    
#     ### Ele recebe uma tupla, no qual a primeira posição é o 
#     ### valor do tempo em alto que o buzzer passou
#     if(auxBuzzerValidation[0] == buzzHighTime):
#             print("Buzzer high time complies the specification for this case.")
#     else:
#             print("Buzzer high time does not comply the specification")





def sceneOne():
    '''    
        Verificar se, depois de nada ser feito durante 3s, os LEDs todos se apagaram e um bipe
        de duração BEEP_TIME_3 segundos.  
    '''    
    command = '01'
    buttonPower = '12'
    buttonArrow = '11'
    ON_OFF_TIME = '30'
    ARROW_TIME = '10'

    times = 3
    limit = 15
    pressTime = '02'
        
    #Incia e para perfil de cura, para limpar o buffer dos tempos de buzzer
    #E haver só duas tuplas:
    #A de quando o botão é pressionado pela segunda vez e de quando entar em baixa consumo

    returnSet = set_config(command, buttonPower, '02')
    time.sleep(1)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):
        returnSet = set_config(command, buttonPower, pressTime)
        time.sleep(3.2)
    else:
        print("First power press failed")

    if(returnSet == bytes.fromhex('99' + command + 'FF')):

        buzzerInfo = getBuzzer()

        if(buzzerInfo[1][0] * 100 >= 100 and getPanel() == [0, 0, 0, 0]):
            #Verfica se o valor de buzzerInfo * 10mS é igual aos 3S da especificação
            print("Test successful. Bip time complies the specification")
            print("Scenario One is Ok")
            return True
        else:
            print("Buzzer bip time doesn't comply the specs or smothing else happened")
            print("Scenario One isn't Ok")
            return False




    else:
        print("Second power press failed")
        return False
 


   
def sceneTwo():
    '''    
       Verificar se, depois de o processo de análise da carga de bateria, os LEDs
       todos irão se apagar depois de 3s.

    '''    
    command = '01'
    buttonPower = '12'
    ON_OFF_TIME = '1E'
    pressTime = '02'

     #Aperta o botão power por ON_OFF_TIME * 100 milissegundos


    returnSet = set_config(command, buttonPower, ON_OFF_TIME)

    if(returnSet == bytes.fromhex('99' + command + 'FF')):
        time.sleep(3 + 5.2) #3s de botão pressionado + 5 segundos de mostragem dos leds
        buzzerInfo = getBuzzer()

        
  
        if((buzzerInfo[1][0] * 100 >= 100)  
            # and (buzzerInfo[1][1] - buzzerInfo[0][1] >= 495)
            and (getPanel() == [0, 0, 0, 0]) ):
            #Verfica se o valor de buzzerInfo * 10mS é igual aos 3S da especificação
            print("Test successful. Inactive period and bip time comply the specification")
            return True
        else:
            print("Inactive period uzzer bip time doesn't comply the specs or smothing else happened")
            return False

    else:
        print("Power pressa failed")    
        return False






   
def main():

    print("Hello World!")

#   sceneOne()
  #sceneTwo()
#   sceneThree()
  #sceneFour()
  #   for i in range(50):
  #     print(i)
  #     sceneTwo()
  #     time.sleep(1)

    cont = 0
    initialTime = time.time()
    for i in range(50):
            print("Round ", i)
            aux  = sceneOne()
            # aux = sceneTwo()
            # aux = sceneThree()

            if(aux):
                cont = cont + 1
            
            time.sleep(1)



    print("Successful tests percentage: ", (cont/50)*100)

    print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100)

    print("Elapsed time: ", time.time() - initialTime)


    with open('output_TC5.txt', 'a') as f:
            print("Scene X:")

            print("Successful tests percentage: ", (cont/50)*100, file=f)

            print("Unsuccessful tests percentage: ", ((50 - cont)/50) * 100, file=f)

            print("Elapsed time: ", time.time() - initialTime, file = f)

            print("############# END ###########\n\n", file=f)

    f.close()












if __name__ == "__main__":
  main()

 




