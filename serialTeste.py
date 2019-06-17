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
    # ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # WINDOWS ##
    ser = serial.Serial('COM12', 115200, timeout=3)  # WINDOWS ##

    #token_ACK='99' #Token para inicio de comunicação
    token_FIN='ff' #Token para fim de comunicação
    # command = 'a1b2c3' #Comando que se deseja enviar


    #Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSent = command + param + option + token_FIN

    #Codificação da mensagem em bytes
    msgToSent = bytes.fromhex(msgToSent) 

    print(msgToSent)  # Pequena prévia da mensagem a ser enviada
    return_set = ser.write((msgToSent))  # Pega o numero de bytes enviado
    print("Bytes sent: ", return_set)  # Exibe o numero de bytes enviado

    time.sleep(0.2)
    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    ser.close()
    #msgReceived = msgReceived.hex()

    print("Mensagem recebida: ", msgReceived)
    # print(ser.read_until(bytes.fromhex(token)))

    return msgReceived


def get_value(option):

    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos



    #### Escolher qual a porta serial que placa tá ##########

    #ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) ## LINUX ##
    ser = serial.Serial('COM12', 115200, timeout=3)  # WINDOWS ##
    
    # ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2) ## LINUX ##
    

    # token_ACK = '99'  # Token para inicio de comunicação
    token_FIN = 'ff'  # Token para fim de comunicação
    # Comando que se deseja enviar

    msgToSent = option+token_FIN  # Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSent = bytes.fromhex(msgToSent)  # Codificação da mensagem em bytes



    print(msgToSent) #Pequena prévia da mensagem a ser enviada
    return_get = ser.write((msgToSent)) #Pega o numero de bytes enviado
    print("Bytes sent: ", return_get) #Exibe o numero de bytes enviado

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

    if isinstance(msgReceived, bytes):
        print("é byte mesmo")
    # print(ser.read_until(bytes.fromhex(token)))
    
    print("Mensagem recebida: ", (msgReceived.hex()))
    print("Tamanho mensagem : ", len(msgReceived))


    return msgReceived.hex()
    


def main():
  print("Hello World!")
  print("Comando set_config: ") 	
  set_config('01', '0A', '11')
  print("")
  print("---------------------------")
  print("Comando 0x05")			
  get_value('05')
  print("")
  print("---------------------------")
  print("Comando 0x04")	
  get_value('04')
  print("")
  print("---------------------------")
  print("Comando 0x03")	
  get_value('03')
  print("")  
  print("---------------------------")
  print("Comando 0x02")	
  get_value('02')
  print("---------------------------")
  #set_config('01', '05', '11')


if __name__ == "__main__":
  main()
