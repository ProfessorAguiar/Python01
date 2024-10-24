#define umidadeDigital 7
#define bomba 6

void setup() {
  pinMode(umidadeDigital, INPUT);
  pinMode(bomba, OUTPUT);
}

void loop() {
  valorumidadeDigital = digitalRead(umidadeDigital);
  if (valorumidadeDigital == 0) {
    digitalWrite(bomba, HIGH);
  }
  else {
    digitalWrite(bomba, LOW);
  }
  delay(500);
}