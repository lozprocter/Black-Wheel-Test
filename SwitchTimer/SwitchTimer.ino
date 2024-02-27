unsigned long startTime;
unsigned long elapsedTime;

// Any needed setup stuff
void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
}

void loop()
{
  // Wait for input to go high
  while(digitalRead(2) == HIGH);

  // Start timing
  startTime = millis();

  // Wait for input to go low
  while(digitalRead(2) == LOW);

  // Now get the time interval
  elapsedTime = millis() - startTime;

  if (elapsedTime > 5){
    Serial.print(elapsedTime);
    Serial.println(" milliseconds");
  }
}