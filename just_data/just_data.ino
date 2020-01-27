#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LSM9DS1.h>
#define SIG_DIG 3

int dataFrequency = 500; // how often to take data in microseconds
int dataLength = 3600 * 2;

Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();
void setupSensor() {
  lsm.setupAccel(lsm.LSM9DS1_ACCELRANGE_16G);
  lsm.setupGyro(lsm.LSM9DS1_GYROSCALE_2000DPS);
  lsm.setupMag(lsm.LSM9DS1_MAGGAIN_4GAUSS);  
}

void setup() {
  Serial.begin(9600);
  if(!lsm.begin()) {
    while(1);
    Serial.print("Could not find sensor");
  }
  setupSensor();
}

void takeData() {
  int i;
  for (i = 0; i < dataLength; i++) {
    delay(dataFrequency);
    sensorData();
  }
  Serial.println("******** FINISHED. WEST LENGTH: 7200 lines *********");
}

void sensorData() {
  lsm.read();

  sensors_event_t a, m, g, temp;
  lsm.getEvent(&a, &m, &g, &temp);

  Serial.print(a.acceleration.x, SIG_DIG); Serial.print('\t');
  Serial.print(a.acceleration.y, SIG_DIG); Serial.print('\t');
  Serial.print(a.acceleration.z, SIG_DIG); Serial.print('\t');

  Serial.print(g.gyro.x, SIG_DIG); Serial.print('\t');
  Serial.print(g.gyro.y, SIG_DIG); Serial.print('\t');
  Serial.print(g.gyro.z, SIG_DIG); Serial.print('\t');

  Serial.print(m.magnetic.x, SIG_DIG); Serial.print('\t');
  Serial.print(m.magnetic.y, SIG_DIG); Serial.print('\t');
  Serial.print(m.magnetic.z, SIG_DIG); Serial.print('\t');

  Serial.println();
}

void loop() {

  delay(1000);
  takeData();

}
