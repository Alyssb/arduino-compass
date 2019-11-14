#include <Stepper.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LSM9DS1.h>
#define SIG_DIG 3

//motor has almost 10 degrees of wiggle room (error)
int dirpin = A0; //2
int steppin = A1; //3

Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();
void setupSensor() {
  lsm.setupAccel(lsm.LSM9DS1_ACCELRANGE_16G);
  lsm.setupGyro(lsm.LSM9DS1_GYROSCALE_2000DPS);
  lsm.setupMag(lsm.LSM9DS1_MAGGAIN_4GAUSS);
}

void setup() {
  Serial.begin(9600);
  pinMode(dirpin, OUTPUT);
  pinMode(steppin, OUTPUT);
  if(!lsm.begin()) {
    while(1);
    Serial.print("Could not find sensor");
  }
  setupSensor();
}

void loop()
{  
  //delay(5000);
  int i;
  
  digitalWrite(dirpin, LOW);    // Change direction.
  delay(100);
  
  for (i = 0; i <= 3; i++) {
    //takeData();
    takeStep();
  }

  digitalWrite(dirpin, HIGH);    // Change direction.
  delay(100);
  for (i = 0; i <= 3; i++) {
    //takeData();
    Serial.print("\nTEST FINISHED\n");
    takeStep();                 
  }
  //takeData();

}

void takeStep() {
  int i;

  for (i = 0; i<100; i++)       // Iterate for 400 microsteps
  {
    digitalWrite(steppin, LOW);  // This LOW to HIGH change is what creates the
    digitalWrite(steppin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
    delayMicroseconds(10000);      
  }
  delay(2000);
}

// take data for one minute
void takeData() {
  int i;
  for (i = 0; i<60; i++) {
    delay(500);
    sensorData();
    delay(500);
    sensorData();
  }
}

void sensorData() {
  lsm.read(); // ask it to read in the data

  sensors_event_t a, m, g, temp;
  lsm.getEvent(&a, &m, &g, &temp); // in the Adafruit_LSM9DS1 library

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
