#include <Servo.h>
#include <FastLED.h>

Servo myservo = Servo();

const int thumbBase = D1;
const int thumb = D4;
const int indexFinger = D6;
const int middle = D2;
const int ring = D5;
const int pinky = D3;

#define DATA_PIN D7
#define NUM_LEDS 7

CRGB leds[NUM_LEDS];

int pos = 0;    
int gHue= 0;    
int values[6] = {46,90,90,90,90,90}; // Array to store servo motor values   
int hslbColours[4]; 
unsigned long previousMillis = 0;
unsigned long position = 0;
int direction = 5;

void setup() {
    Serial.begin(115200); // Set the baud rate to 9600 bps

    FastLED.addLeds<SK6812, DATA_PIN>(leds, NUM_LEDS); 
    FastLED.setBrightness(50);
}


void loop() {
    myservo.write(thumbBase, values[0]);
    myservo.write(thumb, values[1]);
    myservo.write(indexFinger, 180 - values[2]);
    myservo.write(middle, 180 - values[3]);
    myservo.write(ring, values[4]);
    myservo.write(pinky, values[5]);

    if (hslbColours[0] > 360 && hslbColours[1] > 255 && hslbColours[2] > 255) {
        fill_rainbow( leds, NUM_LEDS, gHue, 40);
        EVERY_N_MILLISECONDS( 20 ) { gHue++; }
    } else {
        CRGB rgbColor = CHSV(hslbColours[0], hslbColours[1], hslbColours[2]);
        fill_solid(leds, NUM_LEDS, rgbColor);
    }

    int brightness = hslbColours[3];

    if (brightness < 0) {brightness = 0;}
    if (brightness > 255) {brightness = 255;}

    FastLED.setBrightness(brightness);

    FastLED.show();

    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= 10) {
        previousMillis = currentMillis;

        position = position + direction;
        if (position >= 180) {
            direction = -5;
        }
        if (position <= 0) {
            direction = 5;
        }

        values[1] = position;
        values[2] = position;
        values[3] = position;
        values[4] = position;
        values[5] = position;
        // values[3] = (position + 20)%180;
        // values[4] = (position + 40)%180;
        // values[5] = (position + 60)%180;
    }
        
}
