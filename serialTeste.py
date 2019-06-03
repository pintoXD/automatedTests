import serial


def set_config(): 
    # Primeiro parametro: Porta onde tá a placa que vai ser lida
    # Segundo parâmetro: Velocidade de transferência de dados (em bits/s)
    # Terceiro parâmetro: Tempo de timeout em segundos
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    token_ACK='99' #Token para inicio de comunicação
    token_FIN='ff' #Token para fim de comunicação
    command = 'a1b2c3' #Comando que se deseja enviar


    msgToSent = command+token_FIN #Mensagem em hex, sem o prefixo 0x, para se enviar

    msgToSent = bytes.fromhex(msgToSent) #Codificação da mensagem em bytes

    msgReceived=''



    print("Byte 1? ", msgToSent[0])

    print(msgToSent)




    retrono = ser.write((msgToSent))

    print("Retorno: ", retrono)

    # msgReceived = ser.readline()

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


    msgReceived = ''
    # msgReceived = ser.readline()
    
    msgReceived = ser.read_until(bytes.fromhex(token_FIN))
    ser.close()
    msgReceived = msgReceived.decode('ISO-8859-1')

    print("Mensagem recebida: ", msgReceived)
    # print(ser.read_until(bytes.fromhex(token)))




def main():
  print("Hello World!")
  communication()


if __name__ == "__main__":
  main()
