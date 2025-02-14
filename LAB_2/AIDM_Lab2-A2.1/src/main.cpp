#include <Arduino.h>
#include <Arduino_LSM6DSOX.h>

float temp = 0;
int timestep = 0;

void setup() {
  Serial.begin(9600);

  while(!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.println("Timesteps, Temperature");
}

void loop() {

  while (timestep <= 999)
    {

      timestep ++;

      if (IMU.temperatureAvailable())
      {
        
        IMU.readTemperatureFloat(temp);
        Serial.print(timestep);
        Serial.print(", ");
        Serial.print(temp);
        Serial.println("");
        
      }
      delay(1000);
    }
}

