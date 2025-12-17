#include <SoftwareSerial.h>
SoftwareSerial bt(10,11);

int buzzer = 9;
int led = 7;

bool alarmActive = false;
unsigned long lastToggle = 0;
int interval = 300;
bool state = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);
  bt.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(bt.available()) {
    String cmd = bt.readStringUntil('\n');

    if(cmd == "START") {
      alarmActive = true;
    }
    else if (cmd == "STOP") {
      alarmActive = false;
      digitalWrite(buzzer, LOW);
      digitalWrite(led, LOW);
    }
  }

  if (alarmActive) {
    if (millis() - lastToggle >= interval){
      lastToggle = millis();
      state = !state;
      digitalWrite(buzzer, state);
      digitalWrite(led, state);
    }
  }
}
