#include <Servo.h>
#include <FastLED.h>

Servo myservo = Servo();

const int thumbBase = D1;
const int thumb = D4;
const int indexFinger = D6;
const int middle = D2;
const int ring = D5;
const int pinky = D3;

struct FingerData {
    uint8_t thumbAngle = 46;
    uint8_t thumb = 90;
    uint8_t index = 90;
    uint8_t middle = 90;
    uint8_t ring = 90;
    uint8_t pinky = 90;
    uint8_t ledColour[3] = {255, 255, 255};
    uint8_t ledBrightness = 90;
    uint8_t servoData = false;
};

#define DATA_PIN D7
#define NUM_LEDS 7

CRGB leds[NUM_LEDS];

int pos = 0;    
int gHue= 0;    

FingerData fingerData;

void setup() {
  Serial.begin(115200);

  FastLED.addLeds<SK6812, DATA_PIN>(leds, NUM_LEDS); 
  FastLED.setBrightness(50);
}

void capServoValue(uint8_t &value) {
    if (value > 180) {
        value = 180;
    } else if (value < 0) {
        value = 0;
    }
}

void processMessage(const char* data) {
}


void loop() {
    if (Serial.available() >= sizeof(fingerData)) {

        char receivedData[sizeof(fingerData)];
        Serial.readBytes(receivedData, sizeof(fingerData));

        memcpy(&fingerData, receivedData, sizeof(FingerData));

        // if (fingerData.servoData == 1) {
            capServoValue(fingerData.thumbAngle);
            capServoValue(fingerData.thumb);
            capServoValue(fingerData.index);
            capServoValue(fingerData.middle);
            capServoValue(fingerData.ring);
            capServoValue(fingerData.pinky);

            myservo.write(thumbBase, fingerData.thumbAngle);
            myservo.write(thumb, fingerData.thumb);
            myservo.write(indexFinger, 180 - fingerData.index);
            myservo.write(middle, 180 - fingerData.middle);
            myservo.write(ring, fingerData.ring);
            myservo.write(pinky,fingerData.pinky);
        // }

        if (fingerData.ledColour[0] == 1 && fingerData.ledColour[1] == 1 && fingerData.ledColour[2] == 1) {
            fill_rainbow( leds, NUM_LEDS, gHue, 10);
            gHue = gHue + 3;
        } else {
            CRGB rgb(fingerData.ledColour[0], fingerData.ledColour[1], fingerData.ledColour[2]);
            fill_solid(leds, NUM_LEDS, rgb);
        }

        FastLED.setBrightness(fingerData.ledBrightness);

        FastLED.show();
    }
}
