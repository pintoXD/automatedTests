/*
  Sketch que faz um simples encaminhamento de bytes recebidos via serial

*/

const int tam = 3;

byte inByte[tam];
byte outByte[tam*2];

void setup() {
  // initialize both serial ports:
  Serial.begin(9600);
//  Serial1.begin(9600);

 outByte[0] = 0x99;
 outByte[1] = 0x01;
 outByte[2] = 0x7F;
 outByte[3] = 0x54;
 outByte[4] = 0x85;
 outByte[5] = 0xFF;


}

void loop() {

 //Se ele receber alguma coisa via serial, aí executa o que vem depois
 if(Serial.available()){
  
    
   //Lê os bytes enviados e amrazena no vetor de bytes de tamanho 'tam'
   Serial.readBytes(inByte, tam); 

   //Caraceter especial terminador que deve tá na mensagem recebida    
   char teste = 0xff;
  
       if((char)inByte[tam - 1] == teste){
        
        Serial.write(outByte, tam*2);
       
       }
    
   }

}
