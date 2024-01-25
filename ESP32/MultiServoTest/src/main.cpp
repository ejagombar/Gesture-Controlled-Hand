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
int hslbColours[3]; 
bool setupRainbow = false;

void setup() {
  Serial.begin(115200); // Set the baud rate to 9600 bps

  FastLED.addLeds<SK6812, DATA_PIN>(leds, NUM_LEDS); 
  FastLED.setBrightness(50);
        fill_rainbow( leds, NUM_LEDS, gHue, 40);
}


void loop() {
  myservo.write(thumbBase, values[0]);
  myservo.write(thumb, values[1]);
  myservo.write(indexFinger, 180 - values[2]);
  myservo.write(middle, 180 - values[3]);
  myservo.write(ring, values[4]);
  myservo.write(pinky, values[5]);


  // if (hslbColours[0] > 255 && hslbColours[1] > 255 && hslbColours[2] > 255) {
  //   if (setupRainbow == false) {
  //       fill_rainbow( leds, NUM_LEDS, gHue, 40);
  //       setupRainbow = true;
  //   }

    // EVERY_N_MILLISECONDS( 20 ) { gHue++; }
    gHue++;
  // } else {
  //   CRGB rgbColor = CHSV(hslbColours[0], hslbColours[1], 255);
  //   fill_solid(leds, NUM_LEDS, rgbColor);
  //   setupRainbow = false;
  // }

  // int brightness = hslbColours[2];
  // if (brightness < 0) {brightness = 0;}
  // if (brightness > 255) {brightness = 255;}

  // FastLED.setBrightness(brightness);
  FastLED.setBrightness(255);

  FastLED.show();

  if (Serial.available() > 0) {
    // Wait for the colon at the beginning
    while (Serial.peek() != ':') {
      Serial.read(); // Discard any characters until the colon is found
      //delay(10);
    }
    
    // Read the colon
    Serial.read(); // Consume the colon

    // Read the first six integers
    for (int i = 0; i < 6; i++) {
      int tmp = Serial.parseInt();
      if (tmp >= 0) {
          if (i == 0) {
            if (tmp > 104) {tmp = 104;}
            if (tmp < 12) {tmp = 12;}
          } else {
            if (tmp > 180) {tmp = 180;}
          }
          values[i] = tmp;
        }

      //delay(10);
    }

    // Wait for the opening bracket of the color values
    while (Serial.peek() != '[') {
      Serial.read(); // Discard any characters until the opening bracket is found
      //delay(10);
    }

    Serial.read(); // read the opening bracket

    // Read the three hsl color values
    for (int i = 0; i < 3; i++) {
      int tmp = Serial.parseInt();

      if (tmp >= 0) {
            hslbColours[i] = tmp;
        }
      //delay(10);
      
      // Check for the comma (except for the last color value)
      if (i < 2) {
        while (Serial.peek() != ',') {
          Serial.read(); // Discard any characters until the comma is found
          //delay(10);
        }
        // Read the comma
        Serial.read();
      }
    }

    // Clear the serial buffer
    Serial.flush();
  }
}
