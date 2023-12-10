#include <ESP32Servo.h>
#include <FastLED.h>

#define NUM_LEDS 7
#define DATA_PIN D0

CRGB leds[NUM_LEDS];

Servo myservo;  
int pos = 0;    
int gHue= 0;    
int servoPin = D6;
int buttonPin = D10;
int buttonState = HIGH;   // HIGH when the button is not pressed, LOW when pressed
int lastButtonState = HIGH;  // Previous state of the button
unsigned long lastDebounceTime = 0;  // Last time the button state was changed
unsigned long debounceDelay = 90;  // Debounce time in milliseconds

int positions[5] = {0, 45, 90, 135, 180};
int positionState = D10;

void setup() {
	// Allow allocation of all timers
	ESP32PWM::allocateTimer(0);
	ESP32PWM::allocateTimer(1);
	ESP32PWM::allocateTimer(2);
	ESP32PWM::allocateTimer(3);
	myservo.setPeriodHertz(50); 
	myservo.attach(servoPin, 500, 2500); 
  FastLED.addLeds<SK6812, DATA_PIN>(leds, NUM_LEDS); 
  FastLED.setBrightness(50);

  Serial.begin(115200);
  pinMode(buttonPin, INPUT);

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
        positionState = (positionState+1)%5;
      }
      Serial.println(positionState);
    }
  }
  lastButtonState = reading;
}

void loop() {
		myservo.write(positions[positionState]);    
    leds[0] = CRGB::Red;
    fill_rainbow( leds, NUM_LEDS, gHue, 25);
    FastLED.show();
    button();
  EVERY_N_MILLISECONDS( 20 ) { gHue++; } // slowly cycle the "base color" through the rainbow

}