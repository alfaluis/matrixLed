#include <avr/pgmspace.h>
#include <Arduino.h>
#include <FastLED.h>
#include <MemoryFree.h>
#include <SoftwareSerial.h>
#include "alpabethic8x8.hpp"


SoftwareSerial mySerial(10, 11); // RX, TX


// How many leds in your strip?
#define HEIGH_MATRIX 8
#define WIDTH_MATRIX 8

#define NUM_LEDS (HEIGH_MATRIX * WIDTH_MATRIX)

// For led chips like Neopixels, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
#define DATA_PIN 3
#define CLOCK_PIN 13
#define HEIGH 8

// **************** functions definition *************************

void textContatenation(String&, byte []);
void updateMatrix(byte [], CRGB [], uint32_t,  int, int = 500);
String createInterString(String);
uint8_t returnIndexVowel(char);


// **************** Variable definition **************************
CRGB leds[NUM_LEDS];
char color[7] = {'0','0','0','0','F','F','\0'};
String inputString = "";
int stringLength = 0;

boolean stringComplete = false;  // whether the string is complete
boolean newText = false;
byte byteText [300];

// ********************* main code *******************************
void setup() {
	Serial.begin(9600);
    FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);

}

void loop() {
	FastLED.setBrightness(10);
	if (stringComplete) {
		FastLED.clear(1);
	    Serial.println(inputString);
		Serial.print(F("large String: "));
		Serial.println(inputString.length());
		stringComplete = false;
		newText = true;
		inputString = createInterString(inputString);
		textContatenation(inputString, byteText);
		stringLength = inputString.length();
		inputString="";
	}
	// show text from serial or default text
	if (newText) {
		int lengthScroll = (stringLength - WIDTH_MATRIX/8) * wordSize[0];
		Serial.println(lengthScroll);
		uint32_t colorNum = strtol(color, NULL, 16);
		// for to scroll texts
		for (int scroll = 0; scroll < lengthScroll; scroll++) {
			updateMatrix(byteText, leds, colorNum, scroll, 100);
		}
	}
	else {
		String defaultText = "DEFAULT TEXT";
		uint32_t colorNum = strtol(color, NULL, 16);
		defaultText = createInterString(defaultText);
		textContatenation(defaultText, byteText);
		stringLength = defaultText.length();
		int lengthScroll = (stringLength - WIDTH_MATRIX / 8) * wordSize[0];
		Serial.println(lengthScroll);
		// for to scroll texts
		for (int scroll = 0; scroll < lengthScroll; scroll++) {
			updateMatrix(byteText, leds, colorNum, scroll, 100);
		}
	}

	Serial.print(F("freeMemory()="));
	Serial.println(freeMemory());
	delay(500);

}

// ******************* FUNCTIONS *******************************

uint8_t returnIndexVowel(char text){
	return (uint8_t)text - 32;
}

void textContatenation(String& text, byte text2matrix[]) {

	for (uint8_t i = 0; i < text.length(); i++) {
		uint8_t index = returnIndexVowel(text[i]);

		for (int r = 0; r < 8; r++) {
			text2matrix[r + i * 8] = pgm_read_byte_near(alpabethics + (index * 8 + r));
		}
	}
}

void updateMatrix(byte matrixText[], CRGB leds[], uint32_t rgb, int scroll, int updateTime) {
	// show as many words as possible
	FastLED.clear(1);
	for (int col = scroll; col < WIDTH_MATRIX + scroll; col++) {
		for (int i = 0; i < HEIGH_MATRIX; i++) {
			if ((matrixText[col] << i & 0x80) == 0x80) {
				leds[i + (col - scroll) * 8] = rgb;
			} else {
				leds[i + (col - scroll) * 8] = CRGB::Black;
			}
		}
	}
	FastLED.show();
	delay(updateTime);
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
	int index = 0;
	while (Serial.available()) {
		char a = Serial.read();
		if (a == '\r' || a == '\n') {
			stringComplete = true;
		}
		else {
			if(index <= 5){
				color[index] = a;
				index ++;
			}
			else{
				inputString += a;
				index ++;
			}
		}
		delay(2);
	}
}

String createInterString(String text){
	for(int n = 0; n < WIDTH_MATRIX / 8; n++){
		if(n % 2 == 0){
			text += " ";
		} else {
			text += ":";
		}
	}
	return text;
}
