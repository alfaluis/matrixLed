/*
 * alpabethic.hpp
 *
 *  Created on: Jan 28, 2017
 *      Author: laab
 */

#ifndef ALPABETHIC8X8_HPP_
#define ALPABETHIC8X8_HPP_

const uint8_t wordSize[2] = {8,8};

const PROGMEM byte alpabethics[59*8] = {

					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000, //9
					   0b00000000,
					   0b00000000,
					   0b11011110,
					   0b11011110,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000, //17
					   0b00001000,
					   0b00001110,
					   0b00000110,
					   0b00001000,
					   0b00001110,
					   0b00000110,
					   0b00000000,

					   0b00101000,	//25
					   0b00101000,
					   0b11111110,
					   0b00101000,
					   0b11111110,
					   0b00101000,
					   0b00101000,
					   0b00000000,

					   0b01001000,	//$ (33)
					   0b01011100,
					   0b01010100,
					   0b11111110,
					   0b01010100,
					   0b01110100,
					   0b00100100,
					   0b00000000,

					   0b01000110,
					   0b01100110,
					   0b00110000,
					   0b00011000,
					   0b00001100,
					   0b01100110,
					   0b01100010,
					   0b00000000,

					   0b00000000,	//&
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000,	//'
					   0b00000000,
					   0b00001000,
					   0b00001110,
					   0b00000110,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b01111100,
					   0b11111110,
					   0b10000010,
					   0b00000000,
					   0b00000000,

					   0b00000000,
					   0b10000010,
					   0b11111110,
					   0b01111100,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000,
					   0b00101010,
					   0b00011100,
					   0b00111110,
					   0b00011100,
					   0b00101010,
					   0b00000000,
					   0b00000000,

					   0b00000000,
					   0b00010000,
					   0b00010000,
					   0b01111100,
					   0b01111100,
					   0b00010000,
					   0b00010000,
					   0b00000000,

					   0b00000000,	//,
					   0b00000000,
					   0b10000000,
					   0b11100000,
					   0b01100000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000,	//-
					   0b00010000,
					   0b00010000,
					   0b00010000,
					   0b00010000,
					   0b00010000,
					   0b00000000,
					   0b00000000,

					   0b00000000,	//.
					   0b00000000,
					   0b11000000,
					   0b11000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b11000000,	// /
					   0b01100000,
					   0b00110000,
					   0b00011000,
					   0b00001100,
					   0b00000110,
					   0b00000000,
					   0b00000000,

					   0b01111100,	// 0
					   0b11111110,
					   0b10000010,
					   0b10000010,
					   0b10000010,
					   0b11111110,
					   0b01111100,
					   0b00000000,

					   0b00000000,
					   0b00000000,
					   0b00000100,
					   0b11111110,
					   0b11111110,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b11000100,
					   0b11100110,
					   0b10100010,
					   0b10110010,
					   0b10010010,
					   0b10011110,
					   0b10001100,
					   0b00000000,

					   0b01000100,
					   0b11000110,
					   0b10010010,
					   0b10010010,
					   0b10010010,
					   0b11111110,
					   0b01101100,
					   0b00000000,

					   0b00110000,
					   0b00111000,
					   0b00101100,
					   0b00100110,
					   0b11111110,
					   0b11111110,
					   0b00100000,
					   0b00000000,

					   0b01001110,	//5
					   0b11001110,
					   0b10001010,
					   0b10001010,
					   0b10001010,
					   0b11111010,
					   0b01110010,
					   0b00000000,

					   0b01111000,	//6
					   0b11111100,
					   0b10010110,
					   0b10010010,
					   0b10010010,
					   0b11110010,
					   0b01100000,
					   0b00000000,

					   0b00000010,	//7
					   0b00000010,
					   0b11100010,
					   0b11110010,
					   0b00011010,
					   0b00001110,
					   0b00000110,
					   0b00000000,

					   0b01101100,	//8
					   0b11111110,
					   0b10010010,
					   0b10010010,
					   0b10010010,
					   0b11111110,
					   0b01101100,
					   0b00000000,

					   0b00001100,	//9
					   0b10011110,
					   0b10010010,
					   0b10010010,
					   0b11010010,
					   0b01111110,
					   0b00111100,
					   0b00000000,

					   0b00000000,	//:
					   0b00000000,
					   0b01101100,
					   0b01101100,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000,	//;
					   0b10000000,
					   0b11100110,
					   0b01100110,
					   0b00000000,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b00000000,	//<
					   0b00010000,
					   0b00111000,
					   0b01101100,
					   0b11000110,
					   0b10000010,
					   0b00000000,
					   0b00000000,

					   0b00000000,	//=
					   0b00101000,
					   0b00101000,
					   0b00101000,
					   0b00101000,
					   0b00101000,
					   0b00101000,
					   0b00000000,

					   0b00000000,	// >
					   0b10000010,
					   0b11000110,
					   0b01101100,
					   0b00111000,
					   0b00010000,
					   0b00000000,
					   0b00000000,

					   0b00000100,	//?
					   0b00000110,
					   0b10100010,
					   0b10110010,
					   0b00010010,
					   0b00011110,
					   0b00001100,
					   0b00000000,

					   0b01111100,	//@
					   0b11111110,
					   0b10000010,
					   0b10111010,
					   0b10101010,
					   0b00111110,
					   0b00111100,
					   0b00000000,












					   0b11111000,	//A
			  	  	   0b11111100,
					   0b00100110,
					   0b00100110,
					   0b00100110,
					   0b11111100,
					   0b11111000,
					   0b00000000,

					   0b11111110,
					   0b11111110,	//B
					   0b10010010,
					   0b10010010,
					   0b10010010,
					   0b11111110,
					   0b01101100,
					   0b00000000,

					   0b00111000,
					   0b01111100,	// Char C
					   0b11000110,
					   0b10000010,
					   0b10000010,
					   0b11000110,
					   0b01000100,
					   0b00000000,

					   0b11111110,
					   0b11111110,	// Char D
					   0b10000010,
					   0b10000010,
					   0b11000110,
					   0b01111100,
					   0b00111000,
					   0b00000000,

					   0b11111110,	// E
					   0b11111110,
					   0b10010010,
					   0b10010010,
					   0b10010010,
					   0b10000010,
					   0b10000010,
					   0b00000000,

					   0b11111110,	//F
					   0b11111110,
					   0b00010010,
					   0b00010010,
					   0b00010010,
					   0b00000010,
					   0b00000010,
					   0b00000000,

					   0b00111000,	//G
					   0b01111100,
					   0b11000110,
					   0b10000010,
					   0b10100010,
					   0b11100110,
					   0b11100100,
					   0b00000000,

					   0b11111110,	//H
					   0b11111110,
					   0b00010000,
					   0b00010000,
					   0b00010000,
					   0b11111110,
					   0b11111110,
					   0b00000000,

					   0b00000000,	//I
					   0b00000000,
					   0b00000000,
					   0b11111110,
					   0b11111110,
					   0b00000000,
					   0b00000000,
					   0b00000000,

					   0b01100000,	//J
					   0b11100000,
					   0b10000000,
					   0b10000000,
					   0b10000000,
					   0b11111110,
					   0b01111110,
					   0b00000000,

					   0b11111110,	//K
					   0b11111110,
					   0b00010000,
					   0b00111000,
					   0b01101100,
					   0b11000110,
					   0b11000110,
					   0b00000000,

					   0b11111110, //L
					   0b11111110,
					   0b10000000,
					   0b10000000,
					   0b10000000,
					   0b10000000,
					   0b10000000,
					   0b00000000,

					   0b11111110,	//M
					   0b11111110,
					   0b00011100,
					   0b00111000,
					   0b00011100,
					   0b11111110,
					   0b11111110,
					   0b00000000,

					   0b11111110,	//N
					   0b11111110,
					   0b00001100,
					   0b00011000,
					   0b00110000,
					   0b11111110,
					   0b11111110,
					   0b00000000,

					   0b01111100, //O
					   0b11111110,
					   0b10000010,
					   0b10000010,
					   0b10000010,
					   0b11111110,
					   0b01111100,
					   0b00000000,

					   0b11111110,	//P
					   0b11111110,
					   0b00010010,
					   0b00010010,
					   0b00010010,
					   0b00011110,
					   0b00001100,
					   0b00000000,

					   0b00111100,	//Q
					   0b01111110,
					   0b01000010,
					   0b01100010,
					   0b11100010,
					   0b11111110,
					   0b10111100,
					   0b00000000,

					   0b11111110,	//R
					   0b11111110,
					   0b00010010,
					   0b00010010,
					   0b00110010,
					   0b11111110,
					   0b11001100,
					   0b00000000,

					   0b01001100,	//S
					   0b11011110,
					   0b10011010,
					   0b10010010,
					   0b10110010,
					   0b11110110,
					   0b01100100,
					   0b00000000,

					   0b00000110,	//T
					   0b00000110,
					   0b11111110,
					   0b11111110,
					   0b11111110,
					   0b00000110,
					   0b00000110,
					   0b00000000,

					   0b01111110,	//U
					   0b11111110,
					   0b11000000,
					   0b10000000,
					   0b10000000,
					   0b11111110,
					   0b11111110,
					   0b00000000,

					   0b00111110,	//V
					   0b01111110,
					   0b11100000,
					   0b11000000,
					   0b11100000,
					   0b01111110,
					   0b00111110,
					   0b00000000,

					   0b11111110,	//W
					   0b11111110,
					   0b01100000,
					   0b00110000,
					   0b01100000,
					   0b11111110,
					   0b11111110,
					   0b00000000,

					   0b11000110,	//X
					   0b11101110,
					   0b01111100,
					   0b00111000,
					   0b01111100,
					   0b11101110,
					   0b11000110,
					   0b00000000,

					   0b00000000,	//Y
					   0b00001110,
					   0b00011110,
					   0b11110000,
					   0b11110000,
					   0b00011110,
					   0b00001110,
					   0b00000000,

					   0b10000010,	//Z
					   0b11000010,
					   0b11100010,
					   0b10110010,
					   0b10011010,
					   0b10001110,
					   0b10000110,
					   0b00000000,

					   };

const byte space[8] = {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};



#endif /* ALPABETHIC8X8_HPP_ */
