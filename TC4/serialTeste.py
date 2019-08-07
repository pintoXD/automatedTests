# -*- coding: utf-8 -*-
import serial
import time

def set_config(command, param, option):
    #Para o cabeçalho dessa função:
    #command -> Código do comando a ser enviado
    #param - > Codigo das opções. Ex.: Numero do botão
    #opções -> Informações auxiliares em hex. Ex.: Tempo em segundos (hexadecimal)

    #Configuração da comunicação:
    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos

  #### Escolher qual a porta serial que placa tá ##########


  # ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) ## LINUX ## 
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # LINUX ##
    # ser = serial.Serial('COM5', 115200, timeout=3)  # WINDOWS ##

    #token_ACK='99' #Token para inicio de comunicação
    token_FIN='ff' #Token para fim de comunicação
    # command = 'a1b2c3' #Comando que se deseja enviar


    #Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSent = command + param + option + token_FIN

    #Codificação da mensagem em bytes
    msgToSent = bytes.fromhex(msgToSent) 

    #print(msgToSent)  # Pequena prévia da mensagem a ser enviada
    return_set = ser.write((msgToSent))  # Pega o numero de bytes enviado
    # print("Bytes sent: ", return_set)  # Exibe o numero de bytes enviado

    time.sleep(0.2)
    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    ser.close()
    #msgReceived = msgReceived.hex()

    # print("Mensagem recebida: ", msgReceived)
    # print(ser.read_until(bytes.fromhex(token)))

    return msgReceived

def set_sampling(sampling_time, command = '07'):
    #Para o cabeçalho dessa função:
    #command -> Código do comando a ser enviado
    #param - > Codigo das opções. Ex.: Numero do botão
    #opções -> Informações auxiliares em hex. Ex.: Tempo em segundos (hexadecimal)

    #Configuração da comunicação:
    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos

  #### Escolher qual a porta serial que placa tá ##########


  # ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) ## LINUX ## 
    #ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # LINUX ##
    ser = serial.Serial('COM5', 115200, timeout=3)  # WINDOWS ##

    #token_ACK='99' #Token para inicio de comunicação
    token_FIN='ff' #Token para fim de comunicação
    # command = 'a1b2c3' #Comando que se deseja enviar


    #Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSend= command + sampling_time + token_FIN

    #Codificação da mensagem em bytes
    msgToSend = bytes.fromhex(msgToSend) 

    #print(msgToSend)  # Pequena prévia da mensagem a ser enviada
    return_set = ser.write((msgToSend))  # Pega o numero de bytes enviado
    # print("Bytes sent: ", return_set)  # Exibe o numero de bytes enviado

    
    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    ser.close()
    #msgReceived = msgReceived.hex()

    # print("Mensagem recebida: ", msgReceived)
    # print(ser.read_until(bytes.fromhex(token)))

    return msgReceived


def setRepeat(buttonType, times, limit, pressTime):
    #buttonType -> Código do comando, em hexa, a ser enviado. Se buttonPower ou buttonArrow
    #times -> Número de vezes a se repetir o comando
    #limit -> Número máximo de tentativas para enviar os comandos.
    #pressTime -> Valor do tempo que o botão deve ser pressionado.
                #Lembrar que esse valor, em hexa, será multiplicado por 100 milissegundos
    
    
    auxLimit = 0
    counter = 0

    

    while counter < times:
        print(counter)
        returnSet = set_config('01', buttonType, pressTime)
        print(returnSet)
        if (returnSet == bytes.fromhex('99' + '01' + 'FF')):
            print("Button configured")
            counter = counter + 1
            time.sleep(1)
        else:
            print("Error on buttonArrow configuration")

        auxLimit = auxLimit + 1

        if auxLimit > limit:
            print("Maximum iterations number reached. Button cannot be configured. Breaking loop")
            break

    print("Counter: ", counter)
    print("Times: ", times)

    if counter >= times:
        print("Cure profile configured")
        return True
    else:
        print("Cure profile cannot be configured")
        return False


def get_value(option):

    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos



    #### Escolher qual a porta serial que placa tá ##########

    #ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) ## LINUX ##
    # ser = serial.Serial('COM5', 115200, timeout=3)  # WINDOWS ##
    
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) ## LINUX ##
    

    # token_ACK = '99'  # Token para inicio de comunicação
    token_FIN = 'ff'  # Token para fim de comunicação
    # Comando que se deseja enviar

    msgToSent = option + token_FIN  # Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSent = bytes.fromhex(msgToSent)  # Codificação da mensagem em bytes



    #print(msgToSent) #Pequena prévia da mensagem a ser enviada
    return_get = ser.write((msgToSent)) #Pega o numero de bytes enviado
    # print("Bytes sent: ", return_get) #Exibe o numero de bytes enviado

    #time.sleep(0.5)
    
    # msgReceived = ''
    #msgReceived = ser.readline()
    
    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    time.sleep(0.005)
    # msgReceived = ser.read(30)

    ser.close()
    

    #Amostra o que foi recebido no terminal
    #Tem que usar esse codec aí porque o UTF-8 num aguenta não
    
    #Mensagem recebida em bytes

    # if isinstance(msgReceived, bytes):
    #     print("é byte mesmo")
    # print(ser.read_until(bytes.fromhex(token)))
    
    # print("Mensagem recebida: ", (msgReceived.hex()))
    # print("Tamanho mensagem : ", len(msgReceived))


    return msgReceived.hex()
    


'''def main():
  print("Hello World!")
  print("Comando set_config: ") 	
  set_config('01', '11', '0A')
#   print("")
#   print("---------------------------")
#   print("Comando 0x05")			
#   get_value('05')
#   print("")
#   print("---------------------------")
#   print("Comando 0x04")	
#   get_value('04')
#   print("")
#   print("---------------------------")
#   print("Comando 0x03")	
#   get_value('03')
#   print("")  
#   print("---------------------------")
#   print("Comando 0x02")	
#   get_value('02')
#   print("---------------------------")
  #set_config('01', '05', '11')
'''

# if __name__ == "__main__":
#   main()
