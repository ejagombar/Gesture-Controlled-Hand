#include <ESP32Servo.h>
#include <FastLED.h>

#define NUM_LEDS 7
#define DATA_PIN D0

CRGB leds[NUM_LEDS];

Servo Thumb;  
Servo ThumbBase;  
Servo Index;  
Servo Middle;  
Servo Ring;  
Servo Pinky;  

int pos = 0;    
int gHue= 0;    
int buttonPin = D10;
int buttonState = HIGH;   // HIGH when the button is not pressed, LOW when pressed
int lastButtonState = HIGH;  // Previous state of the button
unsigned long lastDebounceTime = 0;  // Last time the button state was changed
unsigned long debounceDelay = 90;  // Debounce time in milliseconds

int positions[2] = {0, 180};
int positions2[2] = {180, 0};
int positionState = D10;

void setup() {
	// Allow allocation of all timers
	ESP32PWM::allocateTimer(0);
	ESP32PWM::allocateTimer(1);
	ESP32PWM::allocateTimer(2);
	ESP32PWM::allocateTimer(3);
 
	Thumb.setPeriodHertz(50); 
	ThumbBase.setPeriodHertz(50); 
	Index.setPeriodHertz(50); 
	Middle.setPeriodHertz(50); 
	Ring.setPeriodHertz(50); 
	Pinky.setPeriodHertz(50); 

	Thumb.attach(D5, 500, 2500); //works
	ThumbBase.attach(D6, 500, 2500); 
	Index.attach(D1, 500, 2500); 
	Middle.attach(D2, 500, 2500); 
	Ring.attach(D3, 500, 2500); //works
	Pinky.attach(D4, 500, 2500); //works

//  FastLED.addLeds<SK6812, DATA_PIN>(leds, NUM_LEDS); 
  // FastLED.setBrightness(5);

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
        positionState = (positionState+1)%2;
      }
      Serial.println(positionState);
    }
  }
  lastButtonState = reading;
}

void loop() {
		Middle.write(positions[positionState]);    
		Thumb.write(positions[positionState]);    
		Index.write(positions2[positionState]);    
		Pinky.write(positions2[positionState]);    
		Ring.write(positions2[positionState]);    
    // fill_rainbow( leds, NUM_LEDS, gHue, 25);
    // FastLED.show();
    button();
  // EVERY_N_MILLISECONDS( 20 ) { gHue++; } // slowly cycle the "base color" through the rainbow

}