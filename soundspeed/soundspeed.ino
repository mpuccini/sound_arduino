#include <Ultrasonic.h>


  const int Nreads = 1000;

// defines pins numbers
  const int trigPin = 9;
  const int echoPin = 10;
  int sensorPin = 0;

  int index = 0;
  float soundtime = 0;
  float TMPread = 0;
  
// defines variables
  float temperatureC, soundspeed;
  

  void setup() {
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT); // Sets the echoPin as an Input
    Serial.begin(9600); // Starts the serial communication
  }

  void loop() {
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);

      soundtime += pulseIn(echoPin, HIGH);
      TMPread += analogRead(sensorPin);
      index += 1;
      delay(2);
      
      if (index >= Nreads) {
        index = 0;
        
        float ave_soundtime = soundtime / Nreads;
        float ave_TMPread = TMPread / Nreads;
        
        float voltage = ave_TMPread * 5./ 1023;

        soundspeed = 2. * 0.18 / (ave_soundtime / 1000000); 
        temperatureC = (voltage - 0.5) * 100 ; 
         
        Serial.print(temperatureC); 
        Serial.print(" ");
        Serial.println(soundspeed);          
    //    delay(50);

        soundtime = 0;
        TMPread = 0;
      }

  }
