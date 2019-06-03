/*
  Multiple Serial test

  Receives from the main serial port, sends to the others.
  Receives from serial port 1, sends to the main serial (Serial 0).

  This example works only with boards with more than one serial like Arduino Mega, Due, Zero etc.

  The circuit:
  - any serial device attached to Serial port 1
  - Serial Monitor open on Serial port 0

  created 30 Dec 2008
  modified 20 May 2012
  by Tom Igoe & Jed Roach
  modified 27 Nov 2015
  by Arturo Guadalupi

  This example code is in the public domain.
*/

byte inByte[4];
byte outByte[tam*2];

void setup() {
  // initialize both serial ports:
  Serial.begin(9600);
//  Serial1.begin(9600);
}

void loop() {
  // read from port 1, send to port 0:
//  if (Serial1.available()) {
//    int inByte = Serial1.read();
//    Serial.write(inByte);
//  }

  // read from port 0, send to port 1:
//  if (Serial.available() > 0) {
//    inByte = Serial.read();
//    Serial.print("Received: ");
//    Serial.println(inByte, HEX);
//  }

   if(Serial.available()){
    
   
   Serial.readBytes(inByte, 4); 
   Serial.println("Msg rcv");
//   Serial.print(inByte[2], DEC);
//   byte teste = 0xc3;
//   int teste = 0xc3;
   char teste = 0xff;

    if((char)inByte[3] == teste){
    Serial.println("Message match. Sending back");
    Serial.write(inByte, 4);
   }
   
   
   }

}
