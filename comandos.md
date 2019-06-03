# **Proposta de comandos para estrutura de testes**

## **Comandos:**

- Temporização feita via software,ou seja, a resposta será enviada
logo quando o comando for recebido
- Software deve esperar a resposta do request anterior antes de 
mandar um novo
- A comunicação sera feita via UART
- ACK = 0x99
- FIN = 0xFF
- Se a mensagem contiver um valor 0xFF, ele deve ser alterado pela placa de aquisição para o valor 0xFE, para que o software não entenda que é o fim da mensagem e pare de requerer próximos pacotes.



**SET_BOTAO:**

    1. Comando 0x01
    2. Botao:  
               0x11 botao SETA
               0x12 botao POWER
    3. Tempo:  X é um múltiplo de 100 milissegundos (Tempo em que o botao permanecerá ativo)

    RESPOSTA => ACK + 0x01 + FIN



**GET_LED:**

    1. Comando 0x02
    
    RESPOSTA => ACK 
                    + 0x02 
                    + byte em que 1 indica aceso e 0 indica apagado. Esse byte representa os quatro leds. O mais significativo é o de 60s e o menos é o de 10s.
                    + VALOR(0 ou 1)
                    + FIN
    *O valor é uint8_t



**GET_BUZZER:**

    1. Comando 0x03

    RESPOSTA => ACK 
                    + 0x03 
                    + Vetor de pares (tempo de duração do beep, tempo relativo de ocorrência do beep)
                	+ FIN
    *Os vetores sao de uint8_t
    *O caso em que não existe um tempo relativo em que houve a ativação de um beep, o byte que representa esse instante deve ser zero.

**GET_TENSAO_LED_AZUL:**

    1. Comando 0x04

    RESPOSTA => ACK 
                    + 0x04 
                    + valor da tensao sob o led
                    + FIN
    *O Valor sera enviado em uint32_t
    



**GET_NIVEL_BAT:**

    1. Comando 0x05

    RESPOSTA => ACK 
                    + 0x05 
                    + Valor da tensao sob a bateria 
    *O Valor sera enviado em uint32_t

