#!/bin/bash
FILENAME="$(echo $1 | cut -d "." -f 1)"
g++ $1 ../iarduino_I2C_Matrix_8x8.cpp ../WString.cpp ../itoa.c ../dtostrf.cpp -o $FILENAME
