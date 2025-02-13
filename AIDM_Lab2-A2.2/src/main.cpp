#include <Arduino.h>
#include <Arduino_LSM6DSOX.h>

float Ax, Ay, Az;
float Gx, Gy, Gz;

String date = "2025-02-13";
int hh = 13;
int mm = 30;
int ss = 00;

int delay_count = 0;

void setup() {
  Serial.begin(9600);

  while(!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println("Hz");
  Serial.println();

  Serial.print("Gyroscope sample rate = ");  
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println("Hz");
  Serial.println();

  Serial.print("Date, Time, Ax, Ay, Az, Gx, Gy, Gz");
  Serial.println();

}

void loop() {

  if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
    IMU.readAcceleration(Ax, Ay, Az);
    IMU.readGyroscope(Gx, Gy, Gz);

    Serial.print(date);
    Serial.print(',');
    Serial.print(hh);
    Serial.print(':');
    Serial.print(mm);
    Serial.print(':');
    Serial.print(ss);
    Serial.print(',');
    Serial.print(Ax);
    Serial.print(',');
    Serial.print(Ay);
    Serial.print(',');
    Serial.print(Az);
    Serial.print(',');
    Serial.print(Gx);
    Serial.print(',');
    Serial.print(Gy);
    Serial.print(',');
    Serial.println(Gz);
    Serial.println();
  }

delay(500);
// Every second increment the time
delay_count++;

if(delay_count == 2){
  delay_count = 0;
  ss++;
}

if(ss == 60){
  ss = 0;
  mm++;

}
}


