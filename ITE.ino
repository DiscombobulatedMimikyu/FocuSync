#include "SoftwareSerial.h"
SoftwareSerial serial_connection(10, 11);//Create a serial connection with TX and RX on these pins
const int buzzer = 9;
const int led = 7;
void setup()
{
  pinMode(buzzer, OUTPUT); // Setup the pin7 as output
  pinMode(led, OUTPUT);
  digitalWrite(buzzer, LOW);
  digitalWrite(led, LOW);
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
}
void loop() {
  if(serial_connection.available()) {
    char cmd = serial_connection.read();
  
    if (cmd == '1')
    {
      Serial.println("********* Transmission Started *********");
      digitalWrite(buzzer, HIGH);
      tone(buzzer, 1000); // Send 1KHz sound signal...
      delay(1000);         // ...for 1 sec
      noTone(buzzer);     // Stop sound...
      delay(1000);         // ...for 1sec
      digitalWrite(led, HIGH);
    }
    if (cmd == '0')
    {
      Serial.println("********* Transmission Ended *********");
      digitalWrite(buzzer, LOW); // end buzz
    }
  }
  delay(100);
}