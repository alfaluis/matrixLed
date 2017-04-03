#ifdef __IN_ECLIPSE__
//This is a automatic generated file
//Please do not modify this file
//If you touch this file your change will be overwritten during the next build
//This file has been generated on 2017-04-02 14:16:03

#include "Arduino.h"
#include <avr/pgmspace.h>
#include <Arduino.h>
#include <FastLED.h>
#include <HardwareSerial.h>
#include <MemoryFree.h>
#include "alpabethic8x8.hpp"
void setup() ;
void loop() ;
uint8_t returnIndexVowel(char text);
void textContatenation(String& text, byte text2matrix[]) ;
void updateMatrix(byte matrixText[], CRGB leds[], uint32_t rgb, int scroll, int updateTime) ;
void serialEvent() ;
String createInterString(String text);


#include "matrixLedAndSerial.ino"

#endif
