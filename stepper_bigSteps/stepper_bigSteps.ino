#include <Stepper.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LSM9DS1.h>
#define SIG_DIG 3

// global variables
int stepSize = 5; // number of steps to take. 100 is 90 degrees
int dataFrequency = 500; // how often to take data in microseconds
int dataLength = 240; // how many times to take data (# points = dataFrequencyE-3 * dataLength)
int numSteps = 80; // how many steps are taken. Consider stepSize when choosing value
bool wait = true;
int waitTime = (60 * 1000); // how long to wait between actions in microseconds
bool takingData = true;

//motor has almost 10 degrees of wiggle room (error)
int dirpin = A0; //2
int steppin = A1; //3

// sets up the sensor with the highest sensitivities for acceleration and gyroscope
// and the lowest sensitivity for the magnetoscope
Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();
void setupSensor() {
  lsm.setupAccel(lsm.LSM9DS1_ACCELRANGE_16G);
  lsm.setupGyro(lsm.LSM9DS1_GYROSCALE_2000DPS);
  lsm.setupMag(lsm.LSM9DS1_MAGGAIN_4GAUSS);
}

// sets up the board, waits for sensor to be findable.
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

// takes a step
void takeStep() {
  /**
   * iterates for a certain number of microsteps
   * global variables used:
   *  stepSize
   *  
   */
  int i;

  for (i = 0; i<stepSize; i++)
  {
    digitalWrite(steppin, LOW);  // This LOW to HIGH change is what creates the
    digitalWrite(steppin, HIGH); // "Rising Edge" so the easydriver knows to when to step.
    delayMicroseconds(5000);    // wait for 5 seconds
  }
}

// takes data from sensor
void takeData() {
  /**
   * calls sensorData(), which prints sensor data, a certain number of times
   * global variables used:
   *  dataLength
   *  dataFrequency
   */
   
  int i;
  for (i = 0; i<dataLength; i++) {
    delay(dataFrequency);
    sensorData();
  }
}

// prints sensor data to the serial port
void sensorData() {
  /**
   * prints data from the LSM9DS1 sensor in the format:
   * accelx accely  accelz  gyrox gyroy gyroz magx  magy  magz
   * where x, y, z are the axes
   */
  lsm.read(); // ask it to read in the data

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
  

  Serial.println(); // adds a new line at the end
}

// takes steps and writes data
void loop()
{  
  /*
   * Moves clockwise and then counterclockwise
   * Global variables used:
   *  wait
   *  waitTime
   *  takingData
   */
   
  if(wait) {
    delay(waitTime);
  }
  
  int i;
  
  digitalWrite(dirpin, LOW);    // Set direction to clockwise
  delay(100);
  
  for (i = 0; i <= numSteps; i++) {
    if(takingData) {
      takeData();
    }
    takeStep();
  }

  i = 0;

  Serial.print("FINISHED."); Serial.print("\n");

  digitalWrite(dirpin, HIGH);    // Set direction to counterclockwise
  delay(100);
  
  for (i = 0; i <= numSteps; i++) {
    if(takingData) {
      takeData();
    }
    takeStep();                 
  }
}
