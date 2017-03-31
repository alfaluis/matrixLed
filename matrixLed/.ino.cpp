#ifdef __IN_ECLIPSE__
//This is a automatic generated file
//Please do not modify this file
//If you touch this file your change will be overwritten during the next build
//This file has been generated on 2017-03-31 06:07:17

#include "Arduino.h"
#include <Arduino.h>
#include "FastLED.h"
#include <HardwareSerial.h>
#include <avr/pgmspace.h>
#include <MemoryFree.h>
#include "alpabethic8x8.hpp"
uint8_t returnIndexVowel(char text);
void setup() ;
void loop() ;
void textContatenation(String& text, byte text2matrix[]) ;
void updateMatrix(byte matrixText[], CRGB leds[], uint32_t color, int scroll, int updateTime) ;
void serialEvent() ;
String createInterString(String text);


#include "matrixLedAndSerial.ino"

#endif
