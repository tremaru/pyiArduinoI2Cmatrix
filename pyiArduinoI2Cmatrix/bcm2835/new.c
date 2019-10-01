#include "bcm2835.h"

int main() 
{
    if (!bcm2835_init())
        return 1;
    bcm2835_i2c_begin();
    bcm2835_i2c_set_baudrate(100000);
}
