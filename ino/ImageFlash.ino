// Данный пример выводит изображения myImage_1 и myImage_2.      //
                                                                 // Создаём изображение "смайлик", которое хранится не в ОЗУ, а в ПЗУ (FLASH).
const uint8_t  myImage_1[] PROGMEM = { 0b00111100,               //                        ####
                                       0b01000010,               //                       #    #
                                       0b10100101,               //                      # #  # #
                                       0b10000001,               //                      #      #
                                       0b10100101,               //                      # #  # #
                                       0b10011001,               //                      #  ##  #
                                       0b01000010,               //                       #    #
                                       0b00111100 };             //                        ####
                                                                 // Создаём изображение "телевизор", которое хранится не в ОЗУ, а в ПЗУ (FLASH).
const uint8_t  myImage_2[] PROGMEM = { 0b01000100,               //                       #   #  
                                       0b00101000,               //                        # #   
                                       0b00010000,               //                         #    
                                       0b11111111,               //                      ########
                                       0b10000011,               //                      #     ##
                                       0b10000011,               //                      #     ##
                                       0b10000011,               //                      #     ##
                                       0b11111111 };             //                      ########
#include <Wire.h>                                                // Подключаем библиотеку для работы с аппаратной шиной I2C.
#include <iarduino_I2C_Matrix_8x8.h>                             // Подключаем библиотеку для работы с LED матрицей 8x8.
iarduino_I2C_Matrix_8x8 disp(0x09);                              // Объявляем объект disp для работы с LED матрицей 8x8, указывая её адрес на шине I2C.
                                                                 //
void setup(){                                                    //
    delay(500);                                                  // Ждём завершение переходных процессов связанных с подачей питания.
    disp.begin();                                                // Инициируем работу с LED матрицей 8x8.
}                                                                //
                                                                 //
void loop(){                                                     //
    disp.drawImage(myImage_1, X8_IMG_ROM); delay(2000);          // Выводим на дисплей изображение массива myImage_1 хранящегося в ПЗУ (FLASH) и ждём пару секунд.
    disp.drawImage(myImage_2, X8_IMG_ROM); delay(2000);          // Выводим на дисплей изображение массива myImage_2 хранящегося в ПЗУ (FLASH) и ждём пару секунд.
}                                                                //