#include <Servo.h>
#include <FastLED.h>

Servo myservo = Servo();

const int potPin1 = 0, thumbBase = D2;
const int potPin2 = 1, middle = D1;
const int potPin3 = 2, ring = D3;
const int potPin4 = 3, pinky = D4;
const int potPin5 = 4, indexFinger = D5;
const int potPin6 = 5, thumb = D6;

#define DATA_PIN D0
#define NUM_LEDS 7

CRGB leds[NUM_LEDS];

int pos = 0;    
int gHue= 0;    
int buttonPin = D10;
int buttonState = HIGH;   // HIGH when the button is not pressed, LOW when pressed
int lastButtonState = HIGH;  // Previous state of the button
unsigned long lastDebounceTime = 0;  // Last time the button state was changed
unsigned long debounceDelay = 90;  // Debounce time in milliseconds

int positions[3] = {0, 90, 180};
int positions2[3] = {180, 90, 0};
int positionState = D10;

void setup() {
  pinMode(buttonPin, INPUT);

  FastLED.addLeds<SK6812, DATA_PIN>(leds, NUM_LEDS); 
  FastLED.setBrightness(50);
}

void button() {
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (reading == HIGH) {
        positionState = (positionState+1)%3;
      }
      Serial.println(positionState);
    }
  }
  lastButtonState = reading;
}
void loop() {
  button();

  myservo.write(thumbBase, positions2[positionState]);
  myservo.write(thumb, positions2[positionState]);
  myservo.write(indexFinger, positions[positionState]);
  myservo.write(middle, positions[positionState]);
  myservo.write(ring, positions2[positionState]);
  myservo.write(pinky, positions2[positionState]);


    fill_rainbow( leds, NUM_LEDS, gHue, 25);
    FastLED.show();
  EVERY_N_MILLISECONDS( 20 ) { gHue++; } // slowly cycle the "base color" through the rainbow
}