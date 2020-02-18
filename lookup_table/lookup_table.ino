// I have no idea what I'm doing.

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, HIGH);

}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);  
  Serial.println("I don't know what I'm doing.");
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);

}
