// initially created referencing a processing tutorial
import processing.serial.*;

Serial mySerial;

String s = null;
int num1 = 10;
float myVal;

void setup() {
  size(200, 400);

  // link processing to serial port
  String myPort = Serial.list() [0]; // always on 0th port
  mySerial = new Serial(this, myPort, 9600);
}

void draw() {
  
  while(mySerial.available() > 0) {
    s = mySerial.readStringUntil(nl);

    if(myString != null) {
      background(0);
      myVal = float(myString);

      myVal = myVal/100 * height;

      rectMode(CENTER);
      rect(width/2, height - (myVal/2), 100, myVal);
    }
  }

}
