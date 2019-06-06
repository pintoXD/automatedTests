import serial
import time

def set_config(command='', param='', option=''):
    #Para o cabeçalho dessa função:
    #command -> Código do comando a ser enviado
    #param - > Codigo das opções. Ex.: Numero do botão
    #opções -> Informações auxiliares em hex. Ex.: Tempo em segundos (hexadecimal)

    #Configuração da comunicação:
    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    token_ACK='99' #Token para inicio de comunicação
    token_FIN='ff' #Token para fim de comunicação
    # command = 'a1b2c3' #Comando que se deseja enviar


    #Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSent = token_ACK+command+option+param+token_FIN 

    #Codificação da mensagem em bytes
    msgToSent = bytes.fromhex(msgToSent) 

    print(msgToSent)  # Pequena prévia da mensagem a ser enviada
    return_set = ser.write((msgToSent))  # Pega o numero de bytes enviado
    print("Bytes sent: ", return_set)  # Exibe o numero de bytes enviado


 
    msgReceived=''
    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    ser.close()
    msgReceived = msgReceived.decode('ISO-8859-1')

    print("Mensagem recebida: ", msgReceived)
    # print(ser.read_until(bytes.fromhex(token)))


def get_value(option=''):

    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    token_ACK = '99'  # Token para inicio de comunicação
    token_FIN = 'ff'  # Token para fim de comunicação
    # Comando que se deseja enviar

    msgToSent = token_ACK+option+token_FIN  # Mensagem em hex, sem o prefixo 0x, para se enviar
    msgToSent = bytes.fromhex(msgToSent)  # Codificação da mensagem em bytes



    print(msgToSent) #Pequena prévia da mensagem a ser enviada
    return_get = ser.write((msgToSent)) #Pega o numero de bytes enviado
    print("Bytes sent: ", return_get) #Exibe o numero de bytes enviado

    time.sleep(0.5)
    
    # msgReceived = ''
    # msgReceived = ser.readline()

    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    ser.close()

    #Amostra o que foi recebido no terminal
    #Tem que usar esse codec aí porque o UTF-8 num aguenta não
    # msgReceived = msgReceived.decode('ISO-8859-1')
    
    #Mensagem recebida em bytes
    print("Mensagem recebida: ", msgReceived)
    # print(ser.read_until(bytes.fromhex(token)))


def main():
  print("Hello World!")
  get_value('b2')
  


if __name__ == "__main__":
  main()
